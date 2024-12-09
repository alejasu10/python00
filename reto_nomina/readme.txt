ejercicio de POO 
RETO: Sistema para calcular las nóminas 
# Acaba de irse de la empresa la programadora que se encargaba del desarrollo del proyecto de nóminas. 
# Ella ya ha creado una clase Sistema_Nominas, y ha hecho los primeros diseños para las clases de Empleados.
# Usando su trabajo ya hecho, termina el programa.

# Codigo Ejemplo
class Sistema_Nominas:  
    #Parametro para una lista de Empleados

    def Calcular_Nomina(self, lista_empleados):
    print("Calculando la nómina...")
    print("========================)

        for empleado in lista_empleados:
        print("Calculando la nómina para: " + empleado.nombre)
        print(empleado.Calcular_Nomina)
        print("========================)

Empleado=[]
# Rellenar la lista de empleados con los datos de los empleados
#jon , Programador de python
# maria,Analista de datos

nominas=Sistema_Nominas
nominas.calcular_nomina(empleados)

#######

# Programa actual:

# Se modifico el codigo para mejorar el programa
# Se creo la clase Empleado
# Se creo la clase Sistema_Nominas
# Se creo un menu
# Se añadio la opcion de nuevo empleado
# Se añadio la opcion de ver empleados
# Se añadio la opcion de eliminar empleado
# Se añadio la opcion de salir

# Los datos se guardan en un archivo de texto
# Los datos guardados se pueden cargar y eliminar
# El archivo donde se guardan tiene por defecto "nomina.txt"

# Se describe lo que hace cada codigo en todas hojas de trabajo