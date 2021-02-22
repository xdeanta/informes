from reportlab.platypus import Table
from reportlab.platypus import  SimpleDocTemplate
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

datos = [
            ['Arriba/Izquierda', '', '02', '03','04'],
            ['', '', '12', '13','14'],
            ['20', '21', '22', 'Abajo/Derecha',''],
            ['30', '31', '32', '','']
]

estilo = [
            ('GRID', '', '', '',''),
            ('VALIGN', '', '', '',''),
            ('', '', '', '',''),
            ('', '', '', '',''),
]

tabla = Table()

tabla.setStyle([('TEXTCOLOR',(1, -4), (7,-4), colors.red),('TEXTCOLOR', (0,0), (0,3), colors.blue)])
tabla.setStyle([('BACKGROUND',(1,1),(-1,-1), colors.aliceblue)])
tabla.setStyle([('INNERGRID', (1,1), (-1,-1), 0.25, colors.darkgray)])

doc = [tabla]

documento = SimpleDocTemplate("informeTabla.pdf", pagesize = A4, showBoundary = 0)
documento.build(doc)