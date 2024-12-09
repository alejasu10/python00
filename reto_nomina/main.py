import Empleados as em # Cargamos los datos de la clase Empleado
import archivo_nomina as archivo # Cargamos los datos de la clase archivo_nomina
from os import system # para limpiar la pantalla

# creando el menu de inicio del programa
if __name__ == "__main__":
    main=True # bandera para el ciclo while
    while main:# inicio del bucle del menu
        # mostramos las opciones del menu
        print("\nPrograma para gestionar la nomina de empleados\n")
        print("1. Mostrar la nomina de empleados")
        print("2. Buscar empleado por nombre")
        print("3. Agregar un nuevo empleado")
        print("4. Eliminar empleado")
        print("5. Salir")
        opcion=int(input("Elija una opcion: "))
        system("cls") # limpiamos la pantalla
        # evaluamos la opcion del menu
        match opcion:
            case 1:# cargamos los empleados del archivo
#cargamos los empleados del archivo desde el archivo_nomina.py
                if archivo.cargar_nomina()==None:
                    print("================")
                    print("Desea crear un archivo Nuevo? (1-2)")
                    print("1. Si\n2. No")
                    opcion_archivo=int(input("Elija una opcion: "))
                    if opcion_archivo==1:
                        archivo.crear_archivo()
                        system("cls")
                    else:
                        print("Saliendo del programa")
                        main=False
                else:
                    empleados=archivo.cargar_nomina()
                    print("Nominas de Empleados")
                    print("================")
                    #Enviamos la lista empleados a su verificacion para luego imprimir su sueldo correcto
                    nomina=archivo.verificar_tipo_empleado(empleados)
                    print(nomina)
                    print("================")

            case 2:
                if archivo.cargar_nomina()==None:#comprobamos si el archivo existe
                    print("================")
                    print("Desea crear un archivo Nuevo? (1-2)")
                    print("1. Si\n2. No")
                    opcion_archivo=int(input("Elija una opcion: "))
                    if opcion_archivo==1:
                        archivo.crear_archivo()
                        system("cls")
                    else:
                        print("Saliendo del programa")
                        main=False
                else:
                # buscamos un empleado por su nombre
                    buscar=input("Ingrese el nombre del empleado a buscar: ")
                    buscar=buscar.lower()
                    buscar=buscar.capitalize()
                    empleado=archivo.buscar_empleado(buscar)
                    print(empleado)
                    salir=input("Presione enter para continuar")
                    system("cls")
                    
            case 3:
                nuevo_cate=input("ingrese la categoria del nuevo empleado: \n 1.Programador\n 2.Analista\n")
                nuevo_cate.lower()
                #creamos un nuevo empleado en base a la categoria
                if nuevo_cate==str(1) or nuevo_cate=="programador":
                    cate_ria="Programador"# dato para localizar el sueldo en base a la categoria
                    empleado= archivo.crear_empleado()
                    empleados= [empleado[0],empleado[1],empleado[2],cate_ria]#lista de empleados a guardar
                    archivo.guardar_nomina(empleados)
                    system("cls")
                    print("Empleado agregado con exito")
                    salir=input("Presione enter para continuar")
                    system("cls")
                    
                elif nuevo_cate==str(2) or nuevo_cate=="analista":#creamos un nuevo empleado en base a la categoria
                    cate_ria="Analista"#con este dato podemos sacar su sueldo en base a la categoria
                    empleado= archivo.crear_empleado()
                    empleados= [empleado[0],empleado[1],empleado[2],cate_ria]
                    archivo.guardar_nomina(empleados)
                    system("cls")
                    print("Empleado agregado con exito")
                    salir=input("Presione enter para continuar")
                    system("cls")
                else:#si la categoria no es valida
                    system("cls")
                    print("Categoria no valida")
                    salir=input("Presione enter para continuar")
                    system("cls")
            case 4:
                archivo.eliminar_empleado()
                salir=input("Presione enter para continuar")
                system("cls")
                    
            case 5:
                print("Saliendo del programa")
                main=False