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
# Funcion para eliminar un empleado
def eliminar_empleado():
    # Pedir al usuario el nombre del empleado a eliminar y con lower y capitalize lo igualamos y guardamos
    empleado_a_eliminar = input("Ingrese el nombre del empleado a eliminar: ")
    empleado_a_eliminar = empleado_a_eliminar.lower()
    empleado_a_eliminar = empleado_a_eliminar.capitalize()
    # Abrimos el archivo en modo lectura y guardamos los empleados linea por linea
    with open("reto_nomina/nomina.txt", "r") as archivo:
        empleados = archivo.readlines()
    # Buscamos el empleado a eliminar en la lista de empleados
    empleado_encontrado = False
    for empleado in empleados:
        if empleado.split(",")[0] == empleado_a_eliminar:
            empleado_encontrado = True
            break
    # Si el empleado no se encuentra en la lista, mostramos un mensaje de error
    if not empleado_encontrado:
        print("Empleado no encontrado o inexistente")
        print("Intentelo de nuevo, compruebe que el nombre este escrito correctamente")
        return
    # Abrimos el archivo en modo escritura y escribimos las lineas que no sean iguales al empleado a eliminar
    if empleado_encontrado:
        with open("reto_nomina/nomina.txt", "w") as archivo:
            for linea in empleados:
                if linea.split(",")[0] != empleado_a_eliminar:
                    archivo.write(linea)
                    
        print("Empleado eliminado con exito")
        print("================")


# crear un nuevo empleado
def crear_empleado():
        nombre=input("ingrese el nombre del nuevo empleado: ")
        nombre=nombre.lower()
        nombre=nombre.capitalize()
        nuevo_sueldo=float(input("ingrese el sueldo del nuevo empleado: "))
        nuevo_cargo=input("ingrese el cargo del nuevo empleado: ")
        empleados=[nombre,nuevo_sueldo,nuevo_cargo] 
        return empleados
# Verificamos si el empleado es programador o analista para imprimir su sueldo correspondiente
def verificar_tipo_empleado(empleados):
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
    nomina=Nomina(lista_empleados)# llamamos a la funcion nomina para imprimir la tabla
    return nomina
# Buscar un empleado en la lista guardada en el archivo
def buscar_empleado(buscar):
    lista_empleados=[]# lista para almacenar los empleados
    empleados=cargar_nomina()
    empleado_econtrado=False# bandera para verificar si el empleado fue encontrado
    for empleado in empleados:
        if empleado[0]==buscar:# verificamos si el nombre del empleado es igual al que se busca
            empleado_econtrado=True
            break
    if empleado_econtrado:
            print("Empleado encontrado")
            print("================")
            # Verificamos si el empleado es programador o analista para imprimir su sueldo correspondiente
            if empleado[3]=="Programador":
                empleado=em.Programador(empleado[0],empleado[1],empleado[2])
                lista_empleados.append([empleado.nombre, empleado.calculo_del_sueldo(), empleado.cargo])
                nomina=Nomina(lista_empleados)# llamamos a la funcion nomina para imprimir la tabla
                return nomina
            elif empleado[3]=="Analista":
                empleado=em.Analista(empleado[0],empleado[1],empleado[2])
                lista_empleados.append([empleado.nombre, empleado.calculo_del_sueldo(), empleado.cargo])
                nomina=Nomina(lista_empleados)# llamamos a la funcion nomina para imprimir la tabla
                return nomina
    if not empleado_econtrado:
        print("Empleado no encontrado")
        print("================")


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
        # los espacios en blanco son para que la tabla quede alineada
        datos_Nomina = tabla.format("\n        ".join(filas))
        return datos_Nomina