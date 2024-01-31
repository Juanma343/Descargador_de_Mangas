import os
import wget

def descargar_imagen(imagenes, carpeta_destino='./'):
    for imagen in imagenes:
        print(carpeta_destino)      
        wget.download(imagen, carpeta_destino)

if __name__ == '__main__':
    # Ejemplo de uso
    url_imagen = ['https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjDeiZQ42F4dpgpTNADE1viIetOwSJXEGrvId7tZ0Iob8rKxRTlraeFLUnP82tM70l1AGtAZs9cds1E5yo9U9vIWifn312egwyti-tZ-or1syc3WMM52R4GYmnBp7q1vUtGWIw4bPT3OlxpXuM7Y6CbtR2vomAMfSsqhIaSk3vEkSeTtug0AmII3vDun_FP/s1600']
    carpeta_destino = r'./temp'
    # Crear la carpeta de destino si no existe
    if not os.path.exists(carpeta_destino):
        os.makedirs(carpeta_destino)

    # Descargar la imagen
    descargar_imagen(url_imagen, carpeta_destino)


