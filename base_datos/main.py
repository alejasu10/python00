import sqlite3
from os import system
import base_datos as bd

if __name__ == '__main__':
    menu=True # bandera para el ciclo while
    conn= sqlite3.connect('base_datos/sqlite.db')# establecemos la conexion con la base de datos
    while menu:
        print("\nSistema de Nominas para empleados") # Menu de inicio del programa
        print("=================================")
        print("1. Mostrar la nomina de empleados")
        print("2. Buscar empleado por nombre")
        print("3. Agregar un nuevo empleado")
        print("4. Eliminar empleado")
        print("5. Salir")
        opcion=int(input("Elija una opcion: "))
        system("cls") # limpiamos la pantalla
        # evaluamos la opcion del menu
        match opcion:
            case 1:
                bd.mostrar(conn)
                salir=input("Presione enter para continuar")
                system("cls")
            case 2:
                bd.buscar_empleado(conn)
                salir=input("Presione enter para continuar")
                system("cls")
            case 3:
                bd.crear_empleado(conn)
                salir=input("Presione enter para continuar")
                system("cls")
            case 4:
                bd.eliminar_empleado(conn)
                salir=input("Presione enter para continuar")
                system("cls")
            case 5:
                menu=False


    conn.close()