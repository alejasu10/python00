import sqlite3

# Creamos una clase para llamar a la base de datos
class base_datos:
    def __init__(self):
        pass
    #  Mostramos los datos de la Base de Datos
    def mostrar(self,conn):
        cursor=conn.cursor()
        sql="SELECT * FROM empleado"# Selecciona todos los campos
        cursor.execute(sql)
        filas=cursor.fetchall()
        empleados=[base_datos(*fila) for fila in filas] # list comprehension, unpacking
        print("ID"," ","NOMBRE"," ","APELLIDO"," ","DIRECCION"," ","EDAD"," ","CARGO"," ","SALARIO")
        for empleado in empleados:
            # Muestra los datos de la tabla empleado
            print(
                empleado.id," ",
                empleado.nombre," ",
                empleado.apellido," ",
                empleado.direccion," ",
                empleado.edad," ",
                empleado.cargo," ",
                empleado.salario)
    # Buscamos un empleado en la base de datos
    def buscar(self,conn,nombre):
        cursor=conn.cursor()
        sql="SELECT * FROM empleado WHERE nombre=?"# Selecciona el campo nombre
        nombre_buscado=nombre
        cursor.execute(sql, (nombre_buscado,))
        filas=cursor.fetchall()
        empleados=[base_datos(*fila) for fila in filas]# list comprehension, unpacking
        if nombre not in empleados:
            print("No se encontro el empleado")
        else:
            print("ID"," ","NOMBRE"," ","APELLIDO"," ","DIRECCION"," ","EDAD"," ","CARGO"," ","SALARIO")
            for empleado in empleados:
                # Muestra los datos de la tabla empleado
                print(
                    empleado.id," ",
                    empleado.nombre," ",
                    empleado.apellido," ",
                    empleado.direccion," ",
                    empleado.edad," ",
                    empleado.cargo," ",
                    empleado.salario)
    def agregar(self,conn,empleado):
        cursor=conn.cursor()
        nuevo_datos=empleado
        nuevos_Datos=(nuevo_datos[0],nuevo_datos[1],nuevo_datos[2],nuevo_datos[3],nuevo_datos[4],nuevo_datos[5])
        sql="INSERT INTO empleado (nombre,apellido,direccion,edad,cargo,salario) VALUES(?,?,?,?,?,?)"# Selecciona todos los campos
        cursor.execute(sql, nuevos_Datos)
        print("Se ha agregado el empleado")
    def modificar(self,conn,empleado):
        cursor=conn.cursor()
        nuevo_datos=empleado
        nuevos_Datos=(nuevo_datos[0],nuevo_datos[1],nuevo_datos[2],nuevo_datos[3],nuevo_datos[4],nuevo_datos[5])
        sql="UPDATE empleado SET nombre=?,apellido=?,direccion=?,edad=?,cargo=?,salario=? WHERE id=?"
        cursor.execute(sql, nuevos_Datos)
        print("Se ha modificado el empleado")
    
    def eliminar(self,conn,nombre):
        cursor=conn.cursor()
        sql="SELECT * FROM empleado WHERE nombre=?"# Selecciona el campo nombre
        nombre_buscado=nombre
        # comprobamos si el empleado existe
        cursor.execute(sql, (nombre_buscado,))
        filas=cursor.fetchall()
        empleados=[base_datos(*fila) for fila in filas]# list comprehension, unpacking
        if nombre not in empleados:
            print("No se encontro el empleado")
        else:
            eliminar=(nombre,)
            sql="DELETE FROM empleado WHERE nombre=?"
            cursor.execute(sql,eliminar)
            print("Se ha eliminado el empleado")