# agregando a la lista con funciones
""" lista_precios=[1,2,3]

def cambiar_lista_precios(lista_precios):
    lista_precios.append(3)
    print ("lista_precios")
    return lista_precios
cambiar_lista_precios(lista_precios)
print(lista_precios) """

#prog para entrar a la disco
#1
""" def saber_edad(edad):
    if edad < 18:
        return print("Eres menor, no puedes entrar")
    elif edad >= 18 and edad < 65:
        return print("puedes entrar, disfruta")
    elif edad >= 65:
        return print("es un sitio copn mucho ruido, se le aconseja que no entre")
    else:
        return print("Introduce una edad valida")


if __name__ == "__main__":
    edad=int(input("Introduce tu edad: "))
    saber_edad(edad) """

#2 usando match

""" def saber_edad(edad):

    match edad:
        case _ if edad<18:
            return print("Eres menor, no puedes entrar")
        case _ if edad>=18 and edad<65:
            return print("puedes entrar, disfruta")
        case _ if edad>=65 :
            return print("es un sitio copn mucho ruido, se le aconseja que no entre")

if __name__ == "__main__":
    edad=int(input("Introduce tu edad: "))
    saber_edad(edad) """

# prog. de lista de compras
 
""" lista_compras=[["pan",False],["leche",True],["carne",False]]

def listacompras(lista):
    for i in range(len(lista)):
            print(lista[i][0],"",end="")

def añadir(lista):
    print("\n")
    producto=input("Introduce el producto: ")
    compra=input("¿Debe comprar este producto? (True/False): ")
    lista.append([producto,compra])
    print("\n")
    listacompras(lista)

def no_comprado(lista):
    for i in range(len(lista)):
        if lista[i][1]==False:
            print(lista[i][0],"",end="")

def verificar(lista):
    print("\n")
    producto=input("Introduce el producto que compro: ")
    for i in range(len(lista)):
        if lista[i][0]==producto:
            lista[i][1]=True
            print("\n")
    print("FALTA POR COMPRAR")
    no_comprado(lista)
    

if __name__ == "__main__":
    print("presiona 1 para ver la lista de compras.")
    print("presiona 2 para añadir un producto a la lista.")
    print("presiona 3 para ver los productos que no han sido comprados.")
    print("presiona 4 para marcar el producto comprado.")
    print("presiona 5 para salir")
    print("\n")
    opcion=int(input("Elige una opcion: "))
    
    match opcion:
        case 1:
            listacompras(lista_compras)
        case 2:
            añadir(lista_compras)
        case 3:
            no_comprado(lista_compras)
        case 4:
            verificar(lista_compras) """


# adivinanza de numero

""" from os import system
import random
def adivinar(numero):
    
    objetivo = int(random.randrange(0, numero*10))
    match numero:
        case _ if numero == objetivo :
            system("cls")
            return print("Has acertado!"),
        case _ if numero < objetivo:
            system("cls")
            return print("El numero que estoy pensando es mayor")

        case _ if numero > objetivo:
          system("cls")
          return print("El numero que estoy pensando es menor")


if __name__ == '__main__':
    intentos=3
    while intentos>0:
        print("\n")
        num=int(input("introduzca el numero que crea que estoy pensando:"))
        adivinar(num)
        intentos -= 1
        print("\n")
        print("Intentos restantes: ", intentos)
        if intentos==0:
            print("Has perdido!")
            ad=input("Quieres volver a adivinar:    (s/n)")
            if ad.lower()=="s":
                intentos=3
            else: 
                print("Adiós!") """

    
    



