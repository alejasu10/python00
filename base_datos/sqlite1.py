# incorporando base de datos
import sqlite3
# F1
""" conn = sqlite3.connect('base_datos/sqlite.db')

cursor=conn.cursor()
sql="SELECT * FROM demo"
cursor.execute(sql)
filas=cursor.fetchall()
print(type(filas))
for fila in filas:
    print(fila[0]," ",fila[1]," ",fila[2])
conn.close() """

# F2 Usando objetos

class Demo:
    def __init__(self,id,name,hint):
        self.id=id
        self.nombre=name
        self.edad=hint


conn = sqlite3.connect('base_datos/sqlite.db')

cursor=conn.cursor()
sql="SELECT * FROM demo"# Selecciona todos los campos
cursor.execute(sql)
filas=cursor.fetchall()

demos=[Demo(*fila) for fila in filas] # list comprehension, unpacking

for demo in demos:
    print(demo.id," ",demo.nombre," ",demo.edad)# Muestra los datos de la tabla demo
conn.close()