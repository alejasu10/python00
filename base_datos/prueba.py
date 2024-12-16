import sqlite3


conn = sqlite3.connect('base_datos/sqlite.db')

cursor=conn.cursor()
sql="SELECT * FROM Empleado"
cursor.execute(sql)
filas=cursor.fetchall()

for fila in filas:
    print(fila[0]," ",fila[1]," ",fila[2]," ",fila[3]," ",fila[4]," ",fila[5]," ",fila[6])
conn.close()