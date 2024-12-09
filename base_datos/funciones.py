import empleado as em

def agregar_empleado():
    categoria=input("Ingrese la categoria del empleado (Programador o Analista): ")
    if categoria.lower() == "programador":
        nombre = input("Ingrese el nombre del empleado: ")
        apellido = input("Ingrese el apellido del empleado: ")
        direccion = input("Ingrese la dirección del empleado: ")
        edad = input("Ingrese la edad del empleado: ")
        cargo = categoria.capitalize()
        sueldo = float(input("Ingrese el salario del empleado: "))
        salario = em.Programador.calculo_del_sueldo(sueldo)
        nuevo_empleado = em.Programador(nombre, apellido, direccion, edad, cargo, salario)
        return nuevo_empleado
    elif categoria.lower() == "analista":
        nombre = input("Ingrese el nombre del empleado: ")
        apellido = input("Ingrese el apellido del empleado: ")
        direccion = input("Ingrese la dirección del empleado: ")
        edad = input("Ingrese la edad del empleado: ")
        cargo = categoria.capitalize()
        sueldo = float(input("Ingrese el salario del empleado: "))
        salario = em.Analista.calculo_del_sueldo(sueldo)
        nuevo_empleado = em.Analista(nombre, apellido, direccion, edad, cargo, salario)
        return nuevo_empleado
    else:
        print("La categoria ingresada no es valida")