import sqlite3

# Creamos una clase para llamar a la base de datos
class base_datos:
    def __init__(self, id,nombre, apellido,direccion, edad,cargo, salario):
        self.id=id
        self.nombre=nombre
        self.apellido=apellido
        self.direccion=direccion
        self.edad=edad
        self.cargo=cargo
        self.salario=salario
    
    def mostrar(self,conn):
        cursor=conn.cursor()
        sql="SELECT * FROM empleado"# Selecciona todos los campos
        cursor.execute(sql)
        filas=cursor.fetchall()
        empleados=[base_datos(*fila) for fila in filas] # list comprehension, unpacking
        for empleado in empleados:
            print(empleado.id," ",empleado.nombre," ",empleado.apellido," ",empleado.direccion," ",empleado.edad," ",empleado.cargo," ",empleado.salario)