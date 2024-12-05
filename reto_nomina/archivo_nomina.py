import Empleados as em
# Guardar en un archivo la nomina de un empleado
def guardar_nomina(empleados):
    with open("reto_nomina/nomina.txt", "a") as archivo:
        # Dependiendo de la categoria del empleado se guarda en el archivo
        if empleados[3]=="Programador":
            archivo.write(f"{empleados[0]},{empleados[1]},Prog. {empleados[2]},{empleados[3]}\n")
        elif empleados[3]=="Analista":
            archivo.write(f"{empleados[0]},{empleados[1]},An. {empleados[2]},{empleados[3]}\n")
        archivo.close()
# Cargar la nomina de un archivo
def cargar_nomina():
    empleados = []#lista donde se guardan los empleados extraidos del archivo
    with open("reto_nomina/nomina.txt", "r") as archivo:
        # Leer el archivo línea por línea y agregar los datos a la lista
        for linea in archivo:
            datos = linea.strip().split(",")
            nombre = datos[0]
            sueldo = float(datos[1])
            cargo = datos[2]
            tipo=datos[3]
            empleado = [nombre, sueldo, cargo,tipo]
            empleados.append(empleado)
    return empleados

# crear un nuevo empleado
def crear_empleado():
        nombre=input("ingrese el nombre del nuevo empleado: ")
        nombre=nombre.capitalize()
        nuevo_sueldo=float(input("ingrese el sueldo del nuevo empleado: "))
        nuevo_cargo=input("ingrese el cargo del nuevo empleado: ")
        empleados=[nombre,nuevo_sueldo,nuevo_cargo] 
        return empleados

# crear tabla de nomina
def Nomina(empleados): # imprime la nomina del empleado en una tabla
        tabla = """\
        +-------------------------------------------------+
        | Nombre             Sueldo           Cargo       |
        |-------------------------------------------------|
        {}
        +-------------------------------------------------+\
        """
        # Formato para cada fila de la tabla
        filas = []
        for empleado in empleados:
            fila = "| {:<18} {:<8.2f}$ {:>16}   |".format(empleado[0], empleado[1], empleado[2])
            filas.append(fila)
        
        # Unir las filas con saltos de línea para formar la tabla
        datos_Nomina = tabla.format("\n        ".join(filas))
        return datos_Nomina