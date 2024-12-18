# PREGUNTA 2 - map
numeros = [1, 2, 3, 4, 5]
# usando map, conseguir el siguiente output (resultado)
Resultado: [2, 4, 6, 8, 10]
#F1
print(list(map(lambda x: x*2, numeros)))
#F2
x = list(map(lambda x: x*2, numeros))
print(x)