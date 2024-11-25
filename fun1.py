# definicion

""" def hola():
    print("hola")

hola()
hola()

for i in range(19):
            print("hola")
 """
#2

""" def hola():
    " esta función imprime hola"

print(help(hola)) #forma 1

print(hola.__doc__) #forma 2

 """

#3
""" def numero(z,y):
    return z/y

x=8
j=5
suma = int(numero(x,j)+5)
print(suma) """

#4 

""" def sobremi(nombre,edad):
    print(f" tu nombre es {nombre}")
    print(f" tu edad es {edad}")
# main program: 

if __name__=="__main__":
    sobremi("felipe",32)
    sobremi("felipe",32)
    sobremi("felipe",32)

 """

# 5
""" def sumar(x,y):
    return x+y

if __name__=="__main__":
    print("programa para hacer matematicas")
    i=int(input("1ª numero: "))
    j=int(input("2ª numero: "))
    res=sumar(i,j)
    print(f"El resultado es: {res}")
     """
#6.. importando desde otro arhivo
""" import mate
if __name__=="__main__":

    print("programa para hacer matematicas")
    print("1. sumar")
    print("2. multiplicar")
    print("3. dividir")
    print("4. restar")
    print("5. raiz cuadrada")
    print("6. salir")
    opcion=int(input("Elija una opcion: "))

    match opcion :
        case 1:
            i=int(input("1ª numero: "))
            j=int(input("2ª numero: "))
            res=mate.sumar(i,j)
            print(f"El resultado es: {res}")
        case 2:
            i=int(input("1ª numero: "))
            j=int(input("2ª numero: "))
            res= mate.multiplicarultiplicar(i,j)
            print(f"El resultado es: {res}")
        case 3:
            i=int(input("1ª numero: "))
            j=int(input("2ª numero: "))
            res=mate.dividir(i,j)
            print(f"El resultado es: {res}")
        case 4:
            i=int(input("1ª numero: "))
            j=int(input("2ª numero: "))
            res=mate.restar(i,j)
            print(f"El resultado es: {res}")
        case 5:
            i=int(input("Ingrese un numero: "))
            res=mate.raiz(i)
            print(f"La raiz cuadrada de {i} es: {res}")
         """

#7. imprimir en m2
""" import mate
if __name__ == "__main__":
    print("calcular m2 de una superficie")
    ancho=float(input("introduza el ancho de la superficie: "))
    largo=float(input("introduzca el largo: "))
    res=mate.m2(largo,ancho)
    print(f"La superficie tiene : {res} m2") """

#8. imprimir precio con impuesto con def
""" 
import mate
comida= [["hamburgesa",18],["papas fritas",10],["pizza",10]]
if __name__ == "__main__":
    for i in range(len(comida)):
        for j in range(len(comida[i])):
            print(f"{comida[i][j]} - {mate.iva(comida[i][1])}") """