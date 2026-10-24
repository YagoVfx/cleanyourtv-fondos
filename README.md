# Fondos de CleanYourTV

Selección personal de fondos para la Philips. Solo las imágenes añadidas aquí formarán
parte del catálogo; no se hacen búsquedas ni descargas de bancos de imágenes.

## Añadir tus fondos

1. Entra en `fondos` y abre la carpeta de la temática.
2. Pulsa **Add file → Upload files** y arrastra hasta cinco imágenes JPEG por categoría. Anime admite hasta 30, cinco por cada una de las seis series seleccionadas.
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
| Coches | `fondos/coches` |
| Pinturas y cuadros | `fondos/pinturas` |

La selección completa contiene 95 imágenes en 14 categorías, contando los 30 fondos de Anime. Para sustituir una imagen,
reemplaza el mismo nombre. Para retirarla, bórrala: el catálogo se regenerará.

## Catálogo del launcher

Dirección estable:

`https://raw.githubusercontent.com/YagoVfx/cleanyourtv-fondos/main/catalogo.json`

El catálogo contiene categoría, ruta, dimensiones, tamaño y huella SHA-256 de cada
JPEG existente. No contiene imágenes externas. Las rutas se resuelven dentro de este
repositorio. Las imágenes se alojan aquí, y la TV conservará solo el fondo descargado
actual además de su fondo inicial incluido.

Desde **2.5-philips-preview11**, la Philips lee este catálogo y descarga solo el fondo que va a mostrar. La colección completa no se almacena en la TV.

Al subir o reemplazar imágenes, GitHub Actions valida los archivos y actualiza `catalogo.json`. Espera a que «Actualizar catálogo de fondos» termine en verde. La TV consultará la colección al cambiar el fondo semanal o al elegir **Cambiar fondo ahora**; no necesita otra APK para sustituir imágenes de las categorías existentes. GitHub puede tardar unos minutos en servir las nuevas versiones.

En la TV, mantén OK sobre **Ajustes** (o pulsa Menú) y entra en **Tema**. Hay 14 categorías y un modo automático por época del año. **Conservar este fondo** pausa el cambio semanal; **Activar cambio semanal** lo reanuda. **Restaurar fondo inicial** vuelve al paisaje incluido y pausa la rotación.

Si no hay conexión o una descarga no supera la validación, se conserva el fondo anterior. Las copias deben seguir siendo JPEG 16:9, de hasta 1920 × 1080 y 2 MiB, con un máximo de cinco por categoría y 30 en Anime.

## Créditos

Conserva autor, enlace de origen y licencia o permiso de las imágenes que añadas en
`CREDITOS.md`. Este repositorio público no concede por sí mismo derechos sobre ellas.
