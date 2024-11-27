class perro:
    def __init__(self, nombre,edad,raza):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
    def __str__(self):
        return f"El perro se llama {self.nombre}, tiene {self.edad} años y es de raza {self.raza}"
    def ladrar(self):
        return "Woof!"
    def jugar(self):
        return "Guau!"
    def dormir(self):
        return "ZZZZZ..."
    def comer(self):
        return "Comiendo..."

# Creando objetos de la clase perro
""" lista_perro = [["Jack", 2, "Labrador"],["Mile", 4, "Dalmata"]]
perros=[]

for perro_datos in lista_perro:
    nombre,edad,raza= perro_datos
    perros.append(perro(*perro_datos))

# Mostrando los datos de cada perro

for perro in perros:
    print(perro)
 """
### usando lista de compresion F2
lista_perro = [["Jack", 2, "Labrador"],["Mile", 4, "Dalmata"]]
perros=[perro(*perro_datos) for perro_datos in lista_perro]
for perro in perros:
    print(perro)