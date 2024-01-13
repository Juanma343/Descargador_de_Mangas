import os
import requests

def descargar_imagen(url, carpeta_destino='.'):
    try:
        # Realizar la solicitud HTTP
        respuesta = requests.get(url, stream=True)
        respuesta.raise_for_status()

        # Extraer el nombre del archivo de la URL
        nombre_archivo = os.path.join(carpeta_destino, url.split("/")[-1])

        # Guardar la imagen en el archivo local
        with open(nombre_archivo, 'wb') as archivo:
            for fragmento in respuesta.iter_content(chunk_size=8192):
                archivo.write(fragmento)

        print(f'Imagen descargada: {nombre_archivo}')
    except requests.exceptions.RequestException as e:
        print(f'Error al descargar la imagen: {e}')

if __name__ == '__main__':
    # Ejemplo de uso
    url_imagen = 'https://example.com/ejemplo_imagen.jpg'
    carpeta_destino = 'carpeta_destino'

    # Crear la carpeta de destino si no existe
    if not os.path.exists(carpeta_destino):
        os.makedirs(carpeta_destino)

    # Descargar la imagen
    descargar_imagen(url_imagen, carpeta_destino)


