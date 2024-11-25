# ejercicios de list
""" x = [10, 50, 20, "Hola", "Agur", 99]
print(x[2:4])
print(x[::2])
print(x[3::])
print(x[::])
print(x[::-1]) # ejecuta desde el ultimo hasra el el primero """

""" x = [10, 20, 30, 30, 50]
y = [50, 60, 70, 80]
z = x +y
print(z)
print (x+y)
print(id(x))
x+=y
print(id(x))
 """
#imprimir todos los alumnos y despues las alumnas
#1
""" ListaAlumnos=["jon","maria","isabel"]
print(ListaAlumnos)
print(ListaAlumnos[1:])
for i in ListaAlumnos[1:]:
    print(i) """
#2
""" ListaAlumnos=["jon"]
ListaAlumnas=["maria","isabel"]
print(ListaAlumnas)
print(ListaAlumnos + ListaAlumnas)

for i in ListaAlumnas:
    print(i)
 """
#3
""" ListaAlumnos=["jon","maria","isabel"]

for i in ListaAlumnos: #3.1
    if i !="jon":
        print(i) 

    if i == "maria" or i == "isabel":#3.2
        print(i) """

# tiempo que tarda en impimir una lista y un tuple
""" import timeit
print(timeit.timeit(stmt='("red", "green", "blue")', number=1000000000))
print(timeit.timeit(stmt='["red", "green", "blue"]', number=1000000000)) """

# imprimir estacionesdel año

""" estaciones=["invierno","primavera","verano","otoño"]
for i in estaciones:
    print(i)
print(estaciones[2])
 """

#comprobar si es o no una vocal

""" letras= ["k","e","f,","i"]
vocales=["a","e","i","o","u"]

for i in letras:
    if i in vocales:
        print(f"{i} es una vocal")#print(i,true)
    else:
        print(f"{i} no es una vocal")#print(i,false) """





# prog. para mostrar el equipamiento individual y luego grupal

""" maria=["saco","tienda","cantimploira","comida"]
ana=["cantimploira","saco","tienda","agua"]
carlos=["cantimploira","saco","tienda","gps"]
todos = maria+ana+carlos

print("Maria equipo: ")
for i in maria:
    print("*",i)

print("\n")
print("Ana equipo: ")
for i in ana:
    print("*",i)

print("\n")
print("carlos equipo: ")
for i in carlos:
    print("*",i)

print("\n")
print("Todos los equipos juntos: ")

for i in todos:
    print("*",i)

print("\n")

print("el total de tiendas es: ",todos.count("tienda"))



print("\n")

print(",".join(todos))# otra forma de imprimir con "," los elementos
print("\n")

#### contar tienda  2####
#contar_tienda=0
#for i in todos:
# if i =="tienda":
# contar_tienda=contar_tienda+1 """





#prog. para gestiar compras

""" compras = ["platanos","manzanas","leche"]

print("Tu lista de compras es: ","\n")

for i in compras:
    print("*",i)
print("\n")
#agregar y mostrar zumo
print("agregando zumo","\n")
compras.append("zumo")
for i in compras:
    print("*",i)
#agregar y mostrar galletas
print("agregando galetas","\n")
compras.append("galletas")
for i in compras:
    print("*",i)
#mostrar 2do y 3rd elemento
print("\n")
print("mostrar segundo y tercer elemento")
for i in compras[1:3]:
    print("*",i)
#mostrar los ultimos 2 elementos
print("\n")
print("Mostrar ultimos 2 elementos: ","\n")
for i in compras[1:]:
    print("*",i)
print("\n")

compras.remove("zumo")
compras.append("zumo de naranja")

for i in compras:
    print("*",i)
print("\n")

compras.remove(compras[-1])
for i in compras:
    print("*",i)
compras.insert(2,"limones")
print("\n")

for i in compras:
    print("*",i)

print("\n")
compras.sort()
for i in compras:
    print("*",i)

 """




#### programa de tienda


""" producto=["manzana","zumos","leche","platanos","pan"]
precio=[10,10,10,12,15]
x=0

print("\n")
print("Bienvenidos a mi tienda, nuestros especiales son: ","\n")


for i in producto[:3]:
        print("*",i)

print("\n")
print("presiona 1 para ver todos los productos.")
print("presiona 2 para hacer una compra.")
print("presiona 3 para borrar un producto.")
print("presione 4 para agregar un producto")

opcion=int(input("Elige una opcion: "))
print("\n")
x=opcion
while x < 6:


    if opcion==1:
        print("lista de precios y produtcs: ")
        print("\n")
        for i in range(len(producto)):
                print("*",producto[i],"con precio de",precio[i])

    elif opcion==2:
        print("\n")
        print("Productos disponibles: ","\n")
        for i in range(len(producto)):
             print("*",producto[i],"con precio de",precio[i])
        print("\n")
        producto_comprar=input("Escribe el nombre del producto que deseas comprar: ")
        print("\n")
        for i in range(len(producto)):
            if producto_comprar==producto[i]:
                    print("el precio es: ",precio[i])
                    cambio=int(input("ingrese dinero para pagar: "))
                    if cambio>=precio[i]:
                         print("El cambio es: ",cambio-precio[i])
                         print("Compra exitosa")
                         

    elif opcion==3:
        print("\n")
        print("Productos disponibles: ","\n")
        for i in range(len(producto)):
            print("*",producto[i],"con precio de",precio[i])
        producto_borrar=input("Escribe el nombre del producto que deseas borrar: ")
        for i in range(len(producto)):
            if producto_borrar==producto[i]:
                producto.remove(producto[i])
                precio.remove(precio[i])
                print("El producto ha sido borrado exitosamente")

    elif opcion==4:
        print("\n")
        print("Productos disponibles: ","\n")
        for i in range(len(producto)):
            print("*",producto[i],"con precio de",precio[i])
        producto_nuevo=input("Escribe el nombre del producto que deseas agregar: ")
        precio_nuevo=int(input("Escribe el precio del producto: "))
        producto.append(producto_nuevo)
        precio.append(precio_nuevo)
        print("El producto ha sido agregado exitosamente")

    else:
     print("opcion no valida")

    print("\n")
    print("presiona 1 para ver todos los productos.")
    print("presiona 2 para hacer una compra.")
    print("presiona 3 para borrar un producto.")
    print("presione 4 para agregar un producto")
    print("presione 6 para salir")

    opcion=int(input("Elige una opcion: "))
    x=opcion

## fin del programa ### """


## prog. de simulacion de pila de libros

# 1 no terminado

""" libros = ["harry_potter","LOR","hobbit","principito"]

print("\n")
print("presiona 1 para agregar un libro al top.")
print("presiona 2 para quitar un libro del top.")
print("presiona 3 para ver el libro que esta en el top.")
print("presiona 4 para ver la cantidad de libros.")
print("presiona 5 para ver todos los libros en la pila.")
print("presiona 6 para salir.")
print("\n")
opcion=int(input("Elige una opcion: "))
print("\n")

while opcion!=6:
    if opcion==1:
        libro_nuevo=input("Escribe el nombre del libro que deseas agregar: ")
        libros.insert(0,libro_nuevo)
        print("El libro ha sido agregado exitosamente")
        print("\n")
        print("libros en la pila: ","\n")
        for i in libros:
            print("*",i)
        print("\n")
    elif opcion==2:
        if len(libros)>0:
            libros.pop(0)
            print("El libro ha sido quitado exitosamente")
            print("\n")
            print("libros en la pila: ","\n")
            for i in libros:
                print("*",i)
                print("\n")
            else:
                print("No hay libros en la pila")
                print("\n")
    elif opcion==3:
        if len(libros)>0:
            print("El libro que esta en el tope es: ",libros[0])
            print("\n")
        else:
            print("No hay libros en la pila")
            print("\n")
    elif opcion==4:
        print("La cantidad de libros en la pila es: ",len(libros))
        print("\n")
    elif opcion==5:
        print("libros en la pila: ","\n")
        for i in libros:
            print("*",i)
            print("\n")
    print("\n")
    print("presiona 1 para agregar un libro al principio.")
    print("presiona 2 para quitar un libro del principio.")
    print("presiona 3 para ver el libro que esta en el tope.")
    print("presiona 4 para ver la cantidad de libros en la pila.")
    print("presiona 5 para ver todos los libros en la pila.")
    print("presiona 6 para salir.")
    print("\n")
    opcion=int(input("Elige una opcion: "))
    print("\n") 
 """
   # forma 2
""" import time

libros = ["harry_potter","lor","hobbit","principito","gladiador","python"]

for i in libros:
    print("*",i)

print("\n")

print("que libro desea escoger: ")
lib=input(" ")
print("\n")
x="y"
while x =="y":
    if lib in libros:
        for i in libros:
            time.sleep(1)
            print("*",i)
        if i==lib:
            print("\n")
            break
        libros.remove(lib)
        libros.insert(0,lib)
        print("\n")
    for i in libros:
        time.sleep(1)
        print("*",i)
    print("\n")
    y=input(print("desea continuar (y/n): " ))
    if y == "y":
        print("que libro desea escoger: ")
        lib=input(" ")
        x=y
    else:
        x="n" """