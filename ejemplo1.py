from reportlab.pdfgen import canvas

documento = canvas.Canvas("PrimerInforme.pdf")

documento.drawString(0,0, "Posicion(X,Y) = (0,0)")
documento.drawString(50,100, "Posicion(X,Y) = (50,100)")
documento.drawString(150,40, "Posicion(X,Y) = (150,40)")
documento.drawImage("/home/dam2a/Imágenes/628px-Ethereum_logo_2014.png",400,500,400,500)

documento.showPage()
documento.save()