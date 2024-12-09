import sqlite3
#creando nueva fila e insertar

conn = sqlite3.connect('base_datos/sqlite.db')

cursor=conn.cursor()

sql=""" INSERT INTO demo(ID,Name,Hint) 
VALUES(?,?,?) """# inserta un nuevo registro, los datos se envian en una tupla

datos=(100,'mick','ferrari')# datos a insertar, pueden ser mas grande
cursor.execute(sql,datos)# enviamos los datos
conn.commit()
conn.close()