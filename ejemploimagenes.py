from reportlab.graphics.shapes import Image, Drawing
from reportlab.graphics import renderPDF
from reportlab.lib.pagesizes import A4

imagenes = []

imagen = Image(0, 0, 500, 1000, "/home/dam2a/Imágenes/628px-Ethereum_logo_2014.png")

dibujo = Drawing(30,30)

dibujo.add(imagen)

imagenes.append(dibujo)

documento = Drawing(A4[0], A4[1])

for elemento in imagenes:
    documento.add(elemento)
renderPDF.drawToFile(documento, "segundoinforme.pdf")



