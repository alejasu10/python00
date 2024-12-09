import sqlite3
class Demo:
    def __init__(self,id,name,hint):
        self.id=id
        self.nombre=name
        self.edad=hint


conn = sqlite3.connect('base_datos/empleados.db')

cursor=conn.cursor()
sql="SELECT * FROM empleado"# Selecciona todos los campos
cursor.execute(sql)
filas=cursor.fetchall()

demos=[Demo(*fila) for fila in filas] # list comprehension, unpacking

for demo in demos:
    print(demo.id," ",demo.nombre," ",demo.edad)# Muestra los datos de la tabla demo
conn.close()