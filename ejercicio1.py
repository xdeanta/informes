import sqlite3 as dbapi
from reportlab.platypus import Table
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

fila_init = ["DNI" , "Nombre" , "Direccion", "Edad", "Sexo"]

data = []

data.append(fila_init)

try:
    bbdd = dbapi.connect("baseDatosTreeView.dat")
except dbapi.StandardError as e:
    print(e)
else:
    print("Conexion abierta")

try:
    cursor = bbdd.cursor()
except dbapi.Error as e2:
    print(e2)
else:
    print("Cursor Preparado")

try:
    cursor.execute("select * from usuarios")
    for fila in cursor.fetchall():
        data.append(fila)
        print(data)
        """data.append(fila[0:2])
        data.append(str(fila[3]))
        data.append(fila[4])"""
    tabla = Table(data)

except dbapi.DatabaseError as e3:
    print(e3)
else:
    print("Consulta ejecutada")
finally:
    cursor.close()
    bbdd.close()

doc = [tabla]
documento = SimpleDocTemplate("TablaDB.pdf", pagesize = A4, showBoundary = 0)
documento.build(doc)