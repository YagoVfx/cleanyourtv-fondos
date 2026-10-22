# Activar el catálogo automático

Si la carpeta .github no se subió con el navegador, en la raíz del repositorio pulsa Add file > Create new file.
Nombre: `.github/workflows/catalogo.yml`. Pega este contenido y pulsa Commit changes:

```yaml
name: Actualizar catálogo de fondos
on:
  push:
    branches: [main]
    paths:
      - 'fondos/**'
      - 'categorias.json'
      - 'scripts/generar_catalogo.py'
      - '.github/workflows/catalogo.yml'
  workflow_dispatch:
permissions:
  contents: write
concurrency:
  group: catalogo-main
  cancel-in-progress: false
jobs:
  catalogo:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          ref: main
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12'
      - name: Validar imágenes y generar catálogo
        run: python scripts/generar_catalogo.py
      - name: Guardar catálogo actualizado
        run: |
          if git diff --quiet -- catalogo.json; then exit 0; fi
          git config user.name 'github-actions[bot]'
          git config user.email '41898282+github-actions[bot]@users.noreply.github.com'
          git add catalogo.json
          git commit -m 'Actualizar catálogo de fondos'
          git push origin HEAD:main
```
