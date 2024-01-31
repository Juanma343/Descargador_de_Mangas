import requests
import bs4
from bs4 import BeautifulSoup

import os

import descargar_imagen
import PDF_conversor

url = "https://www.anzmangashd.com/manga/tales-of-demons-and-gods/461/1"
recuest_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

res = requests.get(url, headers=recuest_headers)
soup = BeautifulSoup(res.text, "html.parser")

tag = soup.find("div", id="all")

# Crea una carpeta temporal para guardar las imagenes
if not os.path.exists('./temp'):
    os.mkdir('./temp')

# Extrae url de las imagenes
imagenes = []
for child in tag.children:
    if isinstance(child, bs4.element.Tag):
        imagenes.append(child['data-src'].strip())

# Descarga las imagenes
descargar_imagen.descargar_imagen(imagenes, "./temp")

# Convierte las imagenes a PDF
imagenes = [os.path.join("./temp", imagen) for imagen in os.listdir("./temp") if imagen.endswith(('.png', '.jpg', '.jpeg'))]
PDF_conversor.convertir_imagenes_a_pdf(imagenes, "resultado.pdf")

# Eliminar las imágenes después de convertirlas a PDF
for imagen in imagenes:
    os.remove(imagen)
    print(f"Se ha eliminado la imagen: {imagen}")

if os.path.exists('./temp'):
    os.rmdir('./temp')
