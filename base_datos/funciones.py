import empleado as em
#"NOMBRE"," ","APELLIDO"," ","DIRECCION"," ","EDAD"," ","CARGO"," ","SALARIO"
def agregar_empleado():
    nombre_a = input("Ingrese el Nombre y Apellido del empleado: (Se parado por el espacio) ")
    nombre,apellido=nombre_a.split(" ")
    direccion = input("Ingrese la dirección del empleado: ")
    edad = input("Ingrese la edad del empleado: ")
    categoria = input("Ingrese la categoria del empleado: ")
    cargo = categoria.lower()
    sueldo = float(input("Ingrese el salario del empleado: "))
    nuevo_empleado = (nombre, apellido, direccion, edad, cargo, sueldo)
    return nuevo_empleado