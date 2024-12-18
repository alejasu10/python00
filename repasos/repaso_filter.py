# PREGUNTA 3
# usar el comando filter para filtrar y presentar solo los clientes menos de edad (adulto)
clientes = [
    {"nombre": "Alice", "edad": 15},
    {"nombre": "Bob", "edad": 35},
    {"nombre": "Charlie", "edad": 13},
    {"nombre": "David", "edad": 40}
]

x = list(filter(lambda x: x["edad"] < 18,clientes))
for i in x:
    print(i["nombre"]," " ,i["edad"])