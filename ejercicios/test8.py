# definicon de funciones
""" def numero(z,y):
    return z/y

x=8
j=5
suma = int(numero(x,j)+5)
print(suma)
 """
## tipo de pythom que vemos, basado en c
""" import sys
print(sys.implementation.name) """

#python -m py_compile test8.py
#python -m dis test8.py


# prog. muesta el indice y el valor de la lista
""" x=[1,6,5,8]
for index, i in enumerate(x):
    print(f"{index}, {i} ") """
    
# usar assert para hacer pruebas.. assert condicion, mesanje
# ejemplo
""" x=2
resultado= x*3

assert resultado == 6, "error de Calculo" """

#1
""" x,y = 5,5
z=x*y
assert z==25, "error" """

# ejercicios con while

#1

""" while True:
    print("hola") """
#2
#imprimir numeros desde el 50 hasta el 100

""" total = 50
while total <101:
    print(total)
    total += 1 """

#3 imprime todos los numeros menos el 12

""" total = 5
while total <21:
    if total !=12:
        print(total)
        total += 1
        continue
    total +=1 """
#4 imprime numeros multiplos de 5 del 0 al 100
   

#4 imrime numero dado por el usuario, lo va sumando con cada numero dado por el usuario hasta que salga del prog.

""" total =0
salir=0
while salir !="q":
    num=int(input("introduzca un numero: "))
    total += num
    print(f"total: {total}")
    print("\n")
    salir=input("¿desea salir? (q para salir) ") """

#5 imprimir valores desde 100 hasta 50

""" i=100
while i >= 50:
    print(i)
    i -= 1 """
# 6 imprimir los valores del 0 a 100 con while

""" i=0
while i <= 100:
    print(i)
    i += 1 """

# 7 preguntar la contraseña, si no es correcto, repetir

""" password="1234"
ciclo=0
entrada=input("introduzca la contraseña: ")
while ciclo==0:
    if entrada==password:
        print("Contraseña correcta")
        ciclo=1
    else:
        print("Contraseña incorrecta")
        entrada=input("introduzca de nuevo la contraseña: ") """

# 8 imprimir una piramide

""" ciclo=0
while ciclo<7:
    print("*"*ciclo)
    ciclo+=1
print("----------")
while ciclo>0:
    print("*"*ciclo)
    ciclo-=1
 """

# Matrices

""" a=[[1,2,3,4],[5,6],[7,8,9]]
s= 0
for i in range(len(a)):
    for j in range(len(a[i])):
        s+=a[i][j]
        print(s) """