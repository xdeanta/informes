from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics.charts.legends import Legend
from reportlab.graphics.shapes import Drawing
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate

guion = []

d = Drawing(300,200)
tarta = Pie()
tarta.x = 65
tarta.y = 15
tarta.width = 170
tarta.height =170
tarta.data = [10,20,30,40,50]
tarta.labels = ['Brave', 'Opera', 'Firefox', 'Chrome', 'Edge']

tarta.slices.strokeWidth = 0.5
tarta.slices[3].popout = 10
tarta.slices[3].strokeWidth = 2
tarta.slices[3].strokeDashArray = [2,2]
tarta.slices[3].labelRadius = 1.75
tarta.slices[3].fontColor = colors.red

tarta.sideLabels = 1

leyenda = Legend()

leyenda.x = 370
leyenda.y = 0

leyenda.dx = 8
leyenda.dy = 8
leyenda.fontName = 'Helvetica'
leyenda.fontSize = 7
leyenda.boxAnchor = 'n'
leyenda.columnMaximum = 10
leyenda.strokeWidth = 1
leyenda.strokeColor = colors.darkgray
leyenda.deltax = 75
leyenda.deltay = 10
leyenda.autoXPadding = 5
leyenda.autoYPadding = 0
leyenda.yGap = 0
leyenda.dxTextSpace = 5
leyenda.alignment= 'right'
leyenda.dividerLines = 1|2|4
leyenda.dividerOffsY=4.5
leyenda.subCols.rpad = 30

colores = [colors.blue, colors.red, colors.green, colors.yellow, colors.pink]
for i, color in enumerate(colores):
    tarta.slices[i].fillColor = color

leyenda.colorNamePairs = [(tarta.slices[i].fillColor,
                           (tarta.labels[i][0:20], '%0.2f' % tarta.data[i])
                           ) for i in range(len(tarta.data))]

d.add(tarta)
d.add(leyenda)
guion.append(d)

doc = SimpleDocTemplate("exemploTarta.pdf", pagesize = A4)
doc.build(guion)