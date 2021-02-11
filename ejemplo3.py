from reportlab.pdfgen import canvas

cadena = "tipos de letra de ejmplo de ReportLab"

doc = canvas.Canvas("_Tiposdeletra.pdf")
objTexto = doc.beginText(50,100)
for tipo in doc.getAvailableFonts():
    objTexto.setFont(tipo,10)
    objTexto.textLine(tipo+ ":" + cadena)