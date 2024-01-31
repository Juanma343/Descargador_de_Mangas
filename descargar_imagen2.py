import os
import requests
from urllib.parse import urlparse

def descargar_y_guardar_imagen(url, carpeta_destino, nombre_archivo):
    try:
        # Realizar la solicitud GET para obtener la imagen
        respuesta = requests.get(url)
        
        # Verificar si la solicitud fue exitosa (código de estado 200)
        if respuesta.status_code == 200:
            # Crear la ruta completa del archivo
            ruta_completa = os.path.join(carpeta_destino, nombre_archivo) + ".jpg"
            
            # Guardar la imagen en la carpeta especificada
            with open(ruta_completa, 'wb') as archivo:
                archivo.write(respuesta.content)
            
            print(f'Imagen descargada y guardada en {ruta_completa}')
        else:
            print(f'Error al descargar la imagen. Código de estado: {respuesta.status_code}')
    except Exception as e:
        print(f'Ocurrió un error: {e}')

def descargar_imagen(imagenes, carpeta_destino='./'):
    n = 1    
    for imagen in imagenes:
        descargar_y_guardar_imagen(imagen, carpeta_destino, n.__str__())
        n += 1


if __name__ == '__main__':
    # Ejemplo de uso
    url_imagen = 'https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiBmZUBwQflswY_RYkMMyPgNYL8K_YZK5eFQMHt0aH9TpDEe9LwFXm7l2koCQYe8uYf_fU09ukv6GAzb4xlIYqCx1w6UXnltK2XPGL4Iwgh_kBhEigesqLK0E9MWrE7mL4Y0D43-rE_hmoFqwU-doU3toOH2dJvWxJVwIbrCXVFAwqLMlZDPawBvhEIg7mf/s1600'
    carpeta_destino = './hola'

    descargar_y_guardar_imagen(url_imagen, carpeta_destino)
