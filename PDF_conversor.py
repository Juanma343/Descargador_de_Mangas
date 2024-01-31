import os
import img2pdf

def convertir_imagenes_a_pdf(imagenes, archivo_salida):
    if not imagenes:
        print("No se encontraron imágenes en la carpeta.")
        return

    imagenes.sort()  # Ordena las imágenes alfabéticamente

    with open(archivo_salida, "wb") as pdf:
        imagenes_pdf = []
        for imagen in imagenes:
            imagenes_pdf.append(imagen)

        pdf.write(img2pdf.convert(imagenes_pdf))

    print(f"Se ha creado el archivo PDF: {archivo_salida}")


if __name__ == "__main__":
    carpeta_entrada = "ruta/a/tu/carpeta"  # Reemplaza con la ruta de tu carpeta de imágenes
    archivo_salida = "resultado.pdf"  # Nombre del archivo PDF resultante

    convertir_imagenes_a_pdf(carpeta_entrada, archivo_salida)
