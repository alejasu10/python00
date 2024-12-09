import sqlite3
import empleado as em
from os import system,path
import base_datos as based
import funciones as fn

if __name__ == '__main__':
    menu = True #Bandera del ciclo while, para mantener dentro o salir del ciclo.
    bd = based.base_datos()# Instancia de la clase base_datos.
    # declaramos la ruta de la base de datos.
    db_path = path.join('base_datos', 'empleados.db')
    try:# Intentamos conectar a la base de datos.
        conn = sqlite3.connect(db_path)
        print("\nConexión exitosa a la base de datos")
    except sqlite3.Error as e:# Si no se puede conectar a la base de datos mostramos el error.
        print(f"Error al conectar a la base de datos: {e}")
        exit(1)# Salimos del programa con un código de error 1.
    while menu:# inicio del bucle del menu
        try:# usamos try para capturar el error de la base de datos.
            print("\nSistema de Nominas para empleados") # Menu de inicio del programa.
            print("=================================")
            print("1. Mostrar la nomina de empleados")
            print("2. Buscar empleado por nombre")
            print("3. Agregar un nuevo empleado")
            print("4. Modificar empleado")
            print("5. Eliminar empleado")
            print("6. Salir")
            opcion=input("Elija una opcion: ")
            # evaluamos la opcion del menu.
            if not opcion.isdigit():
                # si la opcion no es un digito, mostramos un mensaje de error.
                print("Por favor ingrese un número válido")
                input("Presione enter para continuar")
                continue
            opcion=int(opcion)# convertimos la opcion a un entero.
            system("cls")
            match opcion:
                case 1:
                    bd.mostrar(conn)
                    input("Presione enter para continuar")
                    system("cls")
                case 2:
                    nombre=input("Ingrese el nombre del empleado a buscar: ")
                    bd.buscar(conn,nombre)
                    salir=input("Presione enter para continuar")
                    system("cls")
                case 3:
                    nuevo_empleado=fn.agregar_empleado()
                    bd.agregar(conn,nuevo_empleado)
                    salir=input("Presione enter para continuar")
                    system("cls")
                case 4:
                    bd.modificar(conn)
                    salir=input("Presione enter para continuar")
                    system("cls")
                case 5:
                    nombre=input("Ingrese el nombre del empleado a eliminar: ")
                    bd.eliminar(conn,nombre)
                    salir=input("Presione enter para continuar")
                    system("cls")
                case 6:
                    menu=False
                    print("Gracias por usar el sistema de nominas")
                    input("Presione enter para salir")
                case _:
                    # si la opcion no esta dentro del menu, mostramos un mensaje de error.
                    print("Opcion no valida")
            if opcion!=6:
                input("Presione enter para continuar")
                system("cls")
        except Exception as e:# si hay un error dentro del menu, mostramos el error y podemos arreglar.
            print(f"Error: {e}")
            input("Presione enter para continuar")
            system("cls")
    conn.close()# cerramos la conexion a la base de datos.