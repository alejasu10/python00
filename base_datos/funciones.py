import empleado as em
#"NOMBRE"," ","APELLIDO"," ","DIRECCION"," ","EDAD"," ","CARGO"," ","SALARIO"
def agregar_empleado():#creamos un empleado
    print(" Los campos marcados con * son obligatorios")
    print("Ingrese el Nombre y Apellido del empleado: (Se parado por el espacio)  *")
    nombre_a = input()
    nombre,apellido=nombre_a.split(" ")
    direccion = input("Ingrese la dirección del empleado: ")
    edad = input("Ingrese la edad del empleado: *   ")
    categoria = input("Ingrese la categoria del empleado: ")
    cargo = categoria.lower()
    sueldo = input("Ingrese el salario del empleado: ")
    if not sueldo.isdigit():#si el sueldo no es un digito, lo convertimos en 0
        sueldo = 0
        sueldo=float(sueldo)
    #dependiendo del cargo, creamos el objeto empleado
    if cargo == "programador":
        #instanciamos el objeto empleado
        empleado = em.Programador(nombre,apellido,direccion,edad,cargo,sueldo)
        salario = empleado.calculo_del_sueldo()
    elif cargo == "analista":
        empleado = em.Analista(nombre,apellido,direccion,edad,cargo,sueldo)
        salario = empleado.calculo_del_sueldo()
    else:
        empleado = em.Empleado(nombre,apellido,direccion,edad,cargo,sueldo)
        salario = empleado.sueldo
        #creamos la variable nuevo_empleado con los datos del empleado para luego agregar a la base de datos
    nuevo_empleado = (empleado.nombre, empleado.apellido, empleado.direccion, empleado.edad, empleado.cargo, salario)
    return nuevo_empleado

def buscar_modificar(bndera):#buscamos o modificamos los datos del empleado
    buscar=" buscar"
    modi=" modificar"
    texto=""
    if bndera==1:
        texto=buscar
    elif bndera==2:
        texto=modi
    
    print(f"Elija el campo a {texto}: (1/2/3/4/5/6)")
    print("1. Nombre     2. Apellido     3. Direccion     4. Edad     5. Cargo     6. Salario")
    campo_a_modificar = int(input(f"Ingrese el numero del campo a {texto}: "))
    match campo_a_modificar:
        case 1:
            clave = "nombre"
            nombre = input(f"Ingrese el nombre a {texto}: ")
            return clave, nombre
        case 2:
            clave = "apellido"
            apellido = input(f"Ingrese el apellido a {texto}: ")
            return clave, apellido
        case 3:
            clave = "direccion"
            direccion = input(f"Ingrese la direccion a {texto}: ")
            return clave, direccion
        case 4:
            clave = "edad"
            edad = input(f"Ingrese la edad a {texto}: ")
            return clave, edad
        case 5:
            clave = "cargo"
            cargo = input(f"Ingrese el cargo a {texto}: ")
            return clave, cargo
        case 6:
            clave = "salario"
            salario = float(input(f"Ingrese el salario a  {texto}: "))
            return clave, salario
        case _:
            print("Opcion no valida")
            return None