from reportlab.pdfgen import canvas
from PIL import Image

def convertir_a_pdf(rutas_imagenes, nombre_pdf="output.pdf"):
    c = canvas.Canvas(nombre_pdf)

    for ruta_imagen in rutas_imagenes:
        # Añadir una página para cada imagen
        c.showPage()

        # Abrir la imagen y obtener sus dimensiones
        imagen = Image.open(ruta_imagen)
        ancho, alto = imagen.size

        # # Ajustar el tamaño de la imagen para que se ajuste a la página (opcional)
        # if ancho > alto:
        #     imagen = imagen.resize((600, int(600 * alto / ancho)))
        # else:
        #     imagen = imagen.resize((int(600 * ancho / alto), 600))

        # Dibujar la imagen en el lienzo PDF
        c.drawInlineImage(imagen, 0, 0)

    # Guardar el PDF
    c.save()

if __name__ == "__main__":
    # Lista de rutas de imágenes
    rutas_imagenes = ["imagen1.jpg", "imagen2.png", "imagen3.jpeg"]

    # Nombre del archivo PDF de salida
    nombre_pdf_salida = "output.pdf"

    # Llamar a la función para convertir a PDF
    convertir_a_pdf(rutas_imagenes, nombre_pdf_salida)

    print(f"Se ha creado el archivo PDF: {nombre_pdf_salida}")
