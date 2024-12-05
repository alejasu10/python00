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
        print("4. Salir")
        opcion=int(input("Elija una opcion: "))
        system("cls") # limpiamos la pantalla
        # evaluamos la opcion del menu
        match opcion:
            case 1:# cargamos los empleados del archivo
#cargamos los empleados del archivo desde el archivo_nomina.py
                empleados=archivo.cargar_nomina()
                print("Nominas de Empleados")
                print("================")
                lista_empleados=[]# lista para almacenar los empleados
                for empleado in empleados:# mostramos la nomina de los empleados
                    # verificamos si es programador o analista, luego creamos el empleado
                    if empleado[3]=="Programador":
                        empleado=em.Programador(empleado[0],empleado[1],empleado[2])
                        lista_empleados.append([empleado.nombre, empleado.calculo_del_sueldo(), empleado.cargo])
                        # agregamos el empleado a la lista
                    elif empleado[3]=="Analista":
                        empleado=em.Analista(empleado[0],empleado[1],empleado[2])
                        lista_empleados.append([empleado.nombre, empleado.calculo_del_sueldo(), empleado.cargo])
                nomina=archivo.Nomina(lista_empleados)# llamamos a la funcion nomina para imprimir la tabla
                print(nomina)
                print("================")

            case 2:# buscamos un empleado por su nombre
                lista_empleados=[]# lista para almacenar los empleados
                buscar=input("Ingrese el nombre del empleado a buscar: ")
                buscar=buscar.lower()
                buscar=buscar.capitalize()
                empleados=archivo.cargar_nomina()
                for empleado in empleados:
                    if empleado[0]==buscar:
                        print("Empleado encontrado")
                        print("================")
                        if empleado[3]=="Programador":
                            empleado=em.Programador(empleado[0],empleado[1],empleado[2])
                            lista_empleados.append([empleado.nombre, empleado.calculo_del_sueldo(), empleado.cargo])
                            nomina=archivo.Nomina(lista_empleados)# llamamos a la funcion nomina para imprimir la tabla
                            print(nomina)
                            print("================")
                        elif empleado[3]=="Analista":
                            empleado=em.Analista(empleado[0],empleado[1],empleado[2])
                            lista_empleados.append([empleado.nombre, empleado.calculo_del_sueldo(), empleado.cargo])
                            nomina=archivo.Nomina(lista_empleados)# llamamos a la funcion nomina para imprimir la tabla
                            print(nomina)
                            print("================")
            case 3:
                nuevo_cate=int(input("ingrese la categoria del nuevo empleado: \n 1.Programador\n 2.Analista\n"))
                #creamos un nuevo empleado en base a la categoria
                if nuevo_cate==1:
                    cate_ria="Programador"# dato para localizar el sueldo en base a la categoria
                    empleado= archivo.crear_empleado()
                    empleados= [empleado[0],empleado[1],empleado[2],cate_ria]#lista de empleados a guardar
                    archivo.guardar_nomina(empleados)
                    system("cls")
                    print("Empleado agregado con exito")
                    salir=input("Presione enter para continuar")
                    system("cls")
                    
                elif nuevo_cate==2:#creamos un nuevo empleado en base a la categoria
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
                print("Saliendo del programa")
                main=False