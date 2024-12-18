# PREGUNTA 4 desempaquetar

persona = ("Alice", 25, "Engineer")

nombre, edad, rol = persona

# resultado:
print(nombre)        
print(edad)         
print(rol)  

# PREGUNTA 5 desempaquetar
numeros = [1, 2, 3, 4, 5]

primero, *mitad, ultimo = numeros
# resultado:
print(primero)   # Output: 1
print(mitad)  # Output: [2, 3, 4]
print(ultimo)    # Output: 5