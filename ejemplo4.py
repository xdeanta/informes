import os
from reportlab.platypus import Paragraph
from reportlab.platypus import Image
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from  reportlab.lib import colors

hojaEstilo = getSampleStyleSheet()

doc = []

cabecera = hojaEstilo ['Heading4']
cabecera.pageBreakBefore = 0
cabecera.keepWithNext = 0
cabecera.backColor = colors.ivory
parrafo = Paragraph("Cabecera del documento", cabecera)
doc.append(parrafo)

informe = SimpleDocTemplate("documento2.pdf", pagesize=A4, showBoundary = 0)

informe.build(doc)