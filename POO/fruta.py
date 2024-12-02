class fruta:
    def __init__(self,nombre,precio):
        self.nombre=nombre
        self.precio=precio


respuesta= input("introduce el nombre de la fruta: ")
respuesta2= input("ingrese el precio de la fruta: ")
fruta1=fruta(respuesta,respuesta2)
print(fruta1.nombre)
print(fruta1.precio)