""" class fruta:
    def __init__(self,nombre,precio):
        self.nombre=nombre
        self.precio=precio


respuesta= input("introduce el nombre de la fruta: ")
respuesta2= input("ingrese el precio de la fruta: ")
fruta1=fruta(respuesta,respuesta2)
print(fruta1.nombre)
print(fruta1.precio) """

##########

""" frutas= ["MANZANA","pera","NARANJA","kiwi"]

nueva_lista=[fruta for fruta in frutas if fruta.isupper()]

for fruta in frutas:
    if fruta.isupper():
        nueva_lista.append(fruta)

print(nueva_lista)"""

##########

## imprimir las notas de los alumnos solo sim superan los 50 puntos
## usando diccionarios


notas= {"Alicia": 85,"bob": 70,"carlos":95,"diana":45}
notas_aprobadas= {alumno:nota for alumno,nota in notas.items() if nota > 50}

for alumno,nota in notas_aprobadas.items():
    print(f"{alumno} ha aprobado con {nota}")