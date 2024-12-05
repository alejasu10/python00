# prog. convierte dato float en int
""" x = float(3.145)
y = int(x)
print (y)

z = 5.67e4
print (z) """

## prog. para calcular la propina dada por el usuario y devolver la cuenta total"""

""" x= float(input("introduzca el total de su cuenta : $"))
y = float(input("si desea agregar propina , intruzca el porcentaje que desea dejar : "))

propina = x * y / 100

total = x + propina

print(f"su cuenta total con propina es : {total: .2f} $") """

#prog. devuelve none si el valor es negativo
""" x= int(input("introducir un numero : "))
if x < 0:
    print(None)
else :
    print("es positivo") """

# imprimir el rango de 0 a 100
""" for i in range(0,101):
    print(f"numero : {i}") """

# saber si un numero es par con boolean

""" x= int(input("introduzca un numero para saber si es PAR : "))
if x % 2 != 0:
    print(False)
else:
  print(True) """

# prog. para logear un usuario

""" usuario = "admin"
password ="password123"

user_name = input("nombre de usuario: ")
user_password = input("contraseña: ")

log_in = user_name == usuario and user_password == password
   
if log_in:
    print(log_in)
else:
    print("incorrecto")
 """

#imprimir hola 5 veces
""" x = "hola"
for i in range(5):
    print(x) """

# imprimir el rango de 0 a 100

""" for i in range(100):
    print(f"numero : {i+1}")
 """

# imprimir el rango de 0 a 60 de 2 en 2
""" for i in range(0,60,2):
    print(f"numero : {i}") """

# imprimir el rango de 10 a 20 de 2 en 2

""" for i in range(10,20,2):
    print(i) """

#prog. para imprimir tu nombre 50 veces

""" nombre = input("introduce tu nombre: ")

for i in range(50):
    print(nombre) """

#prog. para multiplication

""" numero= int(input("que tabla desea multiplicar:"))

for i in range(0,10):
    print(f"{numero} x {i+1} = {numero * (i+1)}") """

# imprimir todas las tablas 


""" for i in range(0,10):
        print("       ") 
        for j in range(1,10):
            print(f"{j} x {i+1} = {j * (i+1)}", end="  ") 
           

 """
#prog. para saber la ganancia de un producto

""" previ=int(input("ventas previstas: "))
produ= 10.51

for i in range(0,previ):

    print(f"las ganacias para {i+1} ventas es : {produ*(i+1)} ") """

    # programa para contar

""" import time

accion = input("introduce el texto 'up' para contar positivo desde cero y 'down' para contar en negativo hasta cero ")


if accion == "up" or accion == "down":
 
 numero_de_veces=int(input("veces a contar: "))

 if accion == "up":
    
    for i in range(0,numero_de_veces):
        time.sleep(0.5)
        print(i+1)
 elif accion == "down":
    
  for i in range(numero_de_veces,-1,-1):
        time.sleep(0.5)
        print(i)

else:
 print("error") """

# programa para aimacion de un carro
""" 
import time

car = "\U0001F697"
distancia = 10

for i in range(distancia,0,-1):
    print("  " *i,car,end=" \r") 
    time.sleep(0.2) """

# prog. para contar el tiempo que tarda en ejecutar un texto 10_000_000
""" import time
x= "hola"
start = time.perf_counter()
print(time.localtime())
for i in range(100_000_000):
    pass
end = time.perf_counter()
print(f"elapsed time: {end - start}")
print(time.localtime()) """
#2

""" import time
import timeit
x= "hola"
start = timeit.timeit(time.localtime)
print(start)
for i in range(100_000_000):
    pass
end = timeit.timeit(time.localtime)
print(f"elapsed time: {end}") """

#prog. de cohete

""" import time
   
for i in range(10,0,-1):
    time.sleep(1)
    print(i) 
    if i == 1:
        time.sleep(1)
        print("lanzando...") """


# prog. cohete 2

""" import time
distancia = 10
rocket = "🚀"
fire = "💥"   

for i in range(10,0,-1):
    time.sleep(1)
    print(i) 
    if i == 1:
        time.sleep(1)
        print("lanzando...")

for i in range(0,distancia):
    time.sleep(0.5)
    print("  " *i,fire,end=" \r")
    if i == 9:
        time.sleep(0.5)
        print(" " *22,rocket)
     """

