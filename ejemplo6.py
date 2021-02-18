from reportlab.platypus import Table
from reportlab.platypus import  SimpleDocTemplate
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

fila1 = ["", "Lunes", "Martes" , "Miercoles" , "Jueves", "Viernes" ,"Sabado", "Domingo"]
fila2 = ["Mañana", "Clase", "Clase" , "Clase" , "Clase", "Clase", "Piscina", "Vermú"]
fila3 = ["Tarde", "Adiestramiento", "Instrumento" , "Trabajo" , "Trabajo", "Adiestramiento", "Trabajo", "-"]
fila4 = ["Noche", "-", "Trabajo" , "-" , "-", "Trabajo", "-", "-"]

tabla = Table([fila1,fila2,fila3,fila4])

tabla.setStyle([('TEXTCOLOR',(1, -4), (7,-4), colors.red),('TEXTCOLOR', (0,0), (0,3), colors.blue)])
tabla.setStyle([('BACKGROUND',(1,1),(-1,-1), colors.aliceblue)])
tabla.setStyle([('INNERGRID', (1,1), (-1,-1), 0.25, colors.darkgray)])

doc = [tabla]

documento = SimpleDocTemplate("informeTabla.pdf", pagesize = A4, showBoundary = 0)
documento.build(doc)