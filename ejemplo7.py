from reportlab.platypus import Table
from reportlab.platypus import  SimpleDocTemplate
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.barcharts import VerticalBarChart

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

d = Drawing(400,400)
gb = VerticalBarChart()
gb.x = 50
gb.y = 50
gb.height = 125
gb.width = 300
gb.data = listaDatosEdade
gb.strokeColor = colors.black
gb.valueAxis.valueMin = 0
gb.valueAxis.valueMax = 100
gb.valueAxis.valueStep = 10
gb.categoryAxis.labels.boxAnchor = 'ne'
gb.categoryAxis.labels.dx = 8
gb.categoryAxis.labels.dy = -2
gb.categoryAxis.labels.angle = 30
gb.categoryAxis.categoryNames = listaDatosNome
gb.groupSpacing = 10
gb.barSpacing = 2

d.add (gb)

doc.append(d)

documento = SimpleDocTemplate("informeTabla.pdf", pagesize = A4, showBoundary = 0)
documento.build(doc)