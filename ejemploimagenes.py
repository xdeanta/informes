from reportlab.graphics.shapes import Image, Drawing
from reportlab.graphics import renderPDF
from reportlab.lib.pagesizes import A4

imagenes = []

imagen = Image(0, 0, 120, 300, "/home/dam2a/Imágenes/628px-Ethereum_logo_2014.png")

dibujo = Drawing(120,300)

dibujo.translate(50,75)
dibujo.add(imagen)

imagenes.append(dibujo)

dibujo2 = Drawing(300,500)
dibujo2.add(imagen)
dibujo2.rotate(45)
dibujo2.scale(1, 1.5)
dibujo2.translate(500,0)


imagenes.append(dibujo2)

documento = Drawing(A4[0], A4[1])

for elemento in imagenes:
    documento.add(elemento)
renderPDF.drawToFile(documento, "segundoinforme.pdf")



