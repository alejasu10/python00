# PREGUNTA 6 list comprehension
# Usando list comprehension...
nombres = ["Ana", "Luis", "Carlos", "Maria", "Pedro"]

primeras_letras = [nombre[0] for nombre in nombres]

print(primeras_letras)  # Salida: ['A', 'L', 'C', 'M', 'P']
# avanzado: seleccionar solo los nombres de Luis, Carlos y Maria.

avanzado = [x for x in nombres if x in ["Luis", "Carlos", "Maria"]]
print(avanzado)