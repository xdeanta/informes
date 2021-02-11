from reportlab.pdfgen import canvas

cancion = ["En el patio de mi casa", "es particular", "cuando llueve se moja" , "como los demas"]

doc = canvas.Canvas("docTexto.pdf")

objTexto = doc.beginText()
objTexto.setTextOrigin(100,400)
objTexto.setFont('Courier', 14)
for estrofa in cancion:
    objTexto.textLine(estrofa)
objTexto.setFillGray(0.5)
textoLargo = """Esto es un texto largo 
como una serpiente de 5ms de largo.
enrollado en un arbol 
con cocos en la copa donde 
pega el sol radiante"""
objTexto.textLines(textoLargo)

doc.drawText(objTexto)

doc.showPage()
doc.save()

