import sqlite3

# Creamos una clase para llamar a la base de datos
class base_datos:
    def __init__(self, id, nombre, apellido, direccion, edad, cargo, salario):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.edad = edad
        self.cargo = cargo
        self.salario = salario

    @staticmethod
    def mostrar(conn):
        cursor=conn.cursor()
        sql="SELECT * FROM Empleado"# Selecciona todos los campos
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
    def buscar(conn,nombre):
        nombre_buscado=nombre
        cursor=conn.cursor()
        sql="SELECT * FROM Empleado WHERE nombre=?"# Selecciona el campo nombre
        cursor.execute(sql, (nombre_buscado,))
        filas=cursor.fetchall()
        empleados=[base_datos(*fila) for fila in filas]# list comprehension, unpacking
        if not filas:
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
    def agregar(conn,empleado):
        cursor=conn.cursor()
        nuevo_datos=empleado
        nuevos_Datos=(nuevo_datos[0],nuevo_datos[1],nuevo_datos[2],nuevo_datos[3],nuevo_datos[4],nuevo_datos[5])
        sql="INSERT INTO Empleado (nombre,apellido,direccion,edad,cargo,salario) VALUES(?,?,?,?,?,?)"# Selecciona todos los campos
        cursor.execute(sql, nuevos_Datos)
        print("Se ha agregado el empleado")
    def modificar(conn,empleado):
        cursor=conn.cursor()
        nuevo_datos=empleado
        nuevos_Datos=(nuevo_datos[0],nuevo_datos[1],nuevo_datos[2],nuevo_datos[3],nuevo_datos[4],nuevo_datos[5])
        sql="UPDATE empleado SET nombre=?,apellido=?,direccion=?,edad=?,cargo=?,salario=? WHERE id=?"
        cursor.execute(sql, nuevos_Datos)
        print("Se ha modificado el empleado")
    
    def eliminar(conn,nombre):
        cursor=conn.cursor()
        sql="SELECT * FROM Empleado WHERE nombre=?"# Selecciona el campo nombre
        nombre_buscado=nombre
        # comprobamos si el empleado existe
        cursor.execute(sql, (nombre_buscado,))
        filas=cursor.fetchall()
        empleados=[base_datos(*fila) for fila in filas]# list comprehension, unpacking
        if not filas:
            print("No se Encontro el empleado")
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
            print("Ingrese el ID del empleado que desea eliminar")
            id=int(input())
            if id==empleado.id:
                print("¿Desea eliminar el empleado? (S/N)")
                confirmacion=input()
                if confirmacion.lower()=="s":
                    sql="DELETE FROM Empleado WHERE ID=?"
                    cursor.execute(sql,id)
                    print("Se ha eliminado el empleado")
                else:
                        print("Error, ingrese una opcion valida")
            else:
                print("Error, ingrese una opcion valida")