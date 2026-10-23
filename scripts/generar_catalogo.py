"""Indexa exclusivamente los JPEG de las carpetas elegidas; no descarga imágenes."""
import hashlib
import json
from pathlib import Path
import struct

ROOT = Path(__file__).resolve().parents[1]
MAX_BYTES = 2 * 1024 * 1024


def jpeg_size(data):
    if data[:2] != b'\xff\xd8':
        raise ValueError('El archivo no es JPEG')
    offset = 2
    while offset < len(data):
        if data[offset] != 255:
            raise ValueError('Cabecera JPEG incorrecta')
        while offset < len(data) and data[offset] == 255:
            offset += 1
        marker = data[offset]
        offset += 1
        if marker in (0xD9, 0xDA):
            break
        if marker in (0x01, *range(0xD0, 0xD9)):
            continue
        length = struct.unpack_from('>H', data, offset)[0]
        if length < 2 or offset + length > len(data):
            raise ValueError('Segmento JPEG incorrecto')
        if marker in (0xC0, 0xC1, 0xC2):
            if length < 8:
                raise ValueError('Dimensiones JPEG incorrectas')
            height, width = struct.unpack_from('>HH', data, offset + 3)
            return width, height
        offset += length
    raise ValueError('No se encontraron dimensiones JPEG compatibles')


def build():
    categories = json.loads((ROOT / 'categorias.json').read_text(encoding='utf-8'))
    result = {'schema_version': 1, 'categories': []}
    for category in categories:
        folder = ROOT / category['folder']
        if folder.resolve().parent != (ROOT / 'fondos').resolve() or not folder.is_dir():
            raise ValueError('Carpeta de categoría incorrecta')
        images = []
        files = sorted(p for p in folder.iterdir() if p.is_file() and not p.name.startswith('.') and p.name != 'README.md')
        limit = 30 if category['id'] == 'anime' else 5
        if len(files) > limit:
            raise ValueError(f'{folder.name}: máximo {limit} imágenes')
        for path in files:
            if path.suffix.lower() not in ('.jpg', '.jpeg'):
                raise ValueError(f'{path.name}: utiliza JPEG (.jpg)')
            if path.is_symlink() or path.stat().st_size > MAX_BYTES:
                raise ValueError(f'{path.name}: máximo 2 MiB por imagen')
            data = path.read_bytes()
            width, height = jpeg_size(data)
            if not (960 <= width <= 1920 and 540 <= height <= 1080 and abs(width / height - 16 / 9) <= .03):
                raise ValueError(f'{path.name}: utiliza 16:9, recomendado 1920 × 1080')
            images.append({'path': path.relative_to(ROOT).as_posix(), 'bytes': len(data),
                           'width': width, 'height': height, 'sha256': hashlib.sha256(data).hexdigest()})
        result['categories'].append({'id': category['id'], 'label': category['label'], 'images': images})
    return result


if __name__ == '__main__':
    catalog = build()
    (ROOT / 'catalogo.json').write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f"Catálogo: {sum(len(c['images']) for c in catalog['categories'])} fondos en {len(catalog['categories'])} categorías")
