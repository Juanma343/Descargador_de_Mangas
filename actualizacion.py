import requests
import bs4
from bs4 import BeautifulSoup

import descargar_imagen
import PDF_conversor

url = "https://www.anzmangashd.com/manga/tales-of-demons-and-gods/461/1"
recuest_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

res = requests.get(url, headers=recuest_headers)
soup = BeautifulSoup(res.text, "html.parser")

tag = soup.find("div", id="all")

# for child in tag.children:
#     print(child['data-scr'])
#     descargar_imagen.descargar_imagen(child['data-scr'], "imagenes")
#     print("Imagen descargada")

print('hola')
print('hola')

#Uso en lista
print(tag.contents[1]['data-src'].strip())

#Como userlos en un vucle
for child in tag.children:
    if isinstance(child, bs4.element.Tag):
        print(child['data-src'].strip())