# Fondos de CleanYourTV

Selección personal de fondos para la Philips. Solo las imágenes añadidas aquí formarán
parte del catálogo; no se hacen búsquedas ni descargas de bancos de imágenes.

## Añadir tus fondos

1. Entra en `fondos` y abre la carpeta de la temática.
2. Pulsa **Add file → Upload files** y arrastra hasta cinco imágenes JPEG por categoría.
3. Usa nombres sencillos: `01.jpg`, `02.jpg`, `03.jpg`, `04.jpg` y `05.jpg`.
4. Pulsa **Commit changes** en la rama `main`.
5. En **Actions**, comprueba que «Actualizar catálogo de fondos» termina en verde.
   El archivo `catalogo.json` se actualiza automáticamente; no tienes que editarlo.

Prepara las imágenes en Squoosh a **1920 × 1080**, JPEG, calidad aproximada 80–85.
Objetivo orientativo: 200–500 KB por imagen; máximo admitido: **2 MiB**.
También se admiten tamaños menores entre 960 × 540 y 1920 × 1080 manteniendo 16:9.

Si una imagen no cumple el formato, Actions marca el error y conserva el catálogo
anterior. Corrige la imagen y vuelve a subirla. Las carpetas vacías están permitidas
y no generan enlaces a imágenes inexistentes. El archivo `.gitkeep` solo conserva la carpeta.

| Categoría | Carpeta |
|---|---|
| Navidad | `fondos/navidad` |
| Carnaval | `fondos/carnaval` |
| Halloween | `fondos/halloween` |
| Verano | `fondos/verano` |
| Otoño | `fondos/otono` |
| Primavera | `fondos/primavera` |
| Bielorrusia | `fondos/bielorrusia` |
| Fondos nevados | `fondos/nevados` |
| Fondos nocturnos | `fondos/nocturnos` |
| Fondos montañosos | `fondos/montanosos` |
| Estrellas | `fondos/estrellas` |
| Anime | `fondos/anime` |
| Pinturas y cuadros | `fondos/pinturas` |

No hace falta completar las 65 imágenes para empezar. Para sustituir una imagen,
reemplaza el mismo nombre. Para retirarla, bórrala: el catálogo se regenerará.

## Catálogo del launcher

Dirección estable:

`https://raw.githubusercontent.com/YagoVfx/cleanyourtv-fondos/main/catalogo.json`

El catálogo contiene categoría, ruta, dimensiones, tamaño y huella SHA-256 de cada
JPEG existente. No contiene imágenes externas. Las rutas se resuelven dentro de este
repositorio. Las imágenes se alojan aquí, y la TV conservará solo el fondo descargado
actual además de su fondo inicial incluido.

**La versión del launcher instalada antes de crear este repositorio todavía usa el
proveedor anterior. Crear el repositorio no cambia la TV: falta adaptar el launcher
para que lea este catálogo.**

## Créditos

Conserva autor, enlace de origen y licencia o permiso de las imágenes que añadas en
`CREDITOS.md`. Este repositorio público no concede por sí mismo derechos sobre ellas.
