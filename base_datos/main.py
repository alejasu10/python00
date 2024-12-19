import sqlite3
import empleado as em
from os import system,path
import base_datos as based
import funciones as fn

if __name__ == '__main__':
    menu = True #Bandera del ciclo while, para mantener dentro o salir del ciclo.# Instancia de la clase base_datos.
    # declaramos la ruta de la base de datos.
    db_path = path.join('base_datos', 'sqlite.db')
    empleado=[]
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
            print("2. Buscar empleado ")
            print("3. Agregar un nuevo empleado")
            print("4. Modificar empleado")
            print("5. Eliminar empleado")
            print("6. Guardar cambios")
            print("7. Guardar y Salir")
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
                    based.base_datos.mostrar(conn)#Mostramos la nomina de empleados.
                    input("Presione enter para continuar")
                    system("cls")
                case 2:# Buscar empleado por nombre.
                    bndera=1
                    buscar=fn.buscar_modificar(bndera)# llamamos a la funcion buscar_empleado.
                    if buscar is None:# si el valor es None, regresamos al menu.
                        print("Regresando al menu...")
                    else:
                        clave,valor=buscar
                        system("cls")
                        empleado=based.base_datos.buscar(conn,clave,valor)# buscamos el empleado por los campos elegidos.
                        if empleado is False:# si el empleado no existe, regresamos al menu.
                            print("Regresando al menu...")
                        else:# si el empleado existe, mostramos el empleado.
                            print("Empleado encontrado...")
                    salir=input("Presione enter para continuar")
                    system("cls")
                case 3:# Agregar un nuevo empleado.
                    nuevo_empleado=fn.agregar_empleado()# llamamos a la funcion agregar_empleado.
                    based.base_datos.agregar(conn,nuevo_empleado)# agregamos el nuevo empleado a la base de datos.
                    salir=input("Presione enter para continuar")
                    system("cls")
                case 4:# Modificar empleado
                    bndera=1
                    buscar=fn.buscar_modificar(bndera)# llamamos a la funcion buscar_empleado para luego modificarlo.
                    if buscar is None:# si el valor es None, regresamos al menu.
                        print("Regresando al menu...")
                    else:
                        clave,valor=buscar
                        system("cls")
                        empleado=based.base_datos.buscar(conn,clave,valor)
                        if empleado is False:# si el empleado no existe, regresamos al menu.
                            print("Regresando al menu...")
                        else:# si el empleado existe, mostramos el empleado.
                            dc=int(input("Elija el ID del empleado a modificar: "))
                            if dc in empleado:#verificamos si el ID existe.
                                system("cls")
                                bndera=2
                                modificar=fn.buscar_modificar(bndera)
                                if modificar is not None:#si el valor es diferente a None, modificamos el empleado.
                                    clave,valor=modificar
                                    based.base_datos.modificar(conn,dc,clave,valor)
                                    print("Empleado modificado...")
                                else:
                                    print("No se pudo modificar el empleado...")
                            else:# si el ID no existe, regresamos al menu.
                                print("Empleado no encontrado...")
                    salir=input("Presione enter para continuar")
                    system("cls")
                case 5:# Eliminar empleado.
                    nombre=input("Ingrese el nombre del empleado a eliminar: ")
                    based.base_datos.eliminar(conn,nombre)
                    salir=input("Presione enter para continuar")
                    system("cls")
                case 6:# Guardar cambios.
                    print("Desea Guardar los cambios? (s/n): ")
                    guardar=input()# pedimos al usuario si desea guardar los cambios.
                    if guardar=="s":
                        print("Guardando cambios...")
                        conn.commit()# Guardamos los cambios en la base de datos
                    elif guardar=="n":
                        print("Regresando al menu...")
                    else:
                        print("Opcion no valida")
                case 7:# Guardar y salir.
                    print("Desea Guardar los cambios? (s/n): ")
                    guardar=input()# pedimos al usuario si desea guardar los cambios.
                    if guardar=="s":
                        print("Guardando cambios...")
                        conn.commit()# Guardamos los cambios en la base de datos
                        conn.close()# cerramos la conexion a la base de datos.
                        menu=False# salimos del menu.
                        print("Gracias por usar el sistema de nominas")
                        input("Presione enter para salir")
                    elif guardar=="n":# si el usuario no desea guardar los cambios, cerramos la conexion a la base de datos.
                        print("Gracias por usar el sistema de nominas")
                        input("Presione enter para salir")
                        conn.close()# cerramos la conexion a la base de datos.
                        menu=False# salimos del menu.
                    else:
                        print("Opcion no valida")
                case _:
                    # si la opcion no esta dentro del menu, mostramos un mensaje de error.
                    print("Opcion no valida")
        except Exception as e:# si hay un error dentro del menu, mostramos el error y podemos arreglar.
            print(f"Error: {e}")
            input("Presione enter para continuar")
            system("cls")
