# ejercicios de definicon de tuple
""" frutas=("kiwi","manzana","naranja","pera")

for fruta in frutas:
    print(fruta)

x,*y= frutas # la x toma el primer elemento y la *y todo lo demas
print(x)
print(y)
print(type(x))
print(type(y))

x,y,*z= frutas # la x toma el primer elemento, la y toma el 2do y la *z todo lo demas
print(x)
print(y)
print(type(x))
print(type(y))
print(type(z)) """

# ciclo while ####
""" total= 0
while total< 100:
    num=int(input("Total es: "))
    total= total+num
    print(total)
 """
# instanciando ####
""" x= 4.5
print(isinstance(x,int)) """

# prog. preguntar al usuario su salario y devolverlo *10

""" salario=float(input("introduce tu salario: "))

salario_nuevo=salario*10

print(f"Tu nuevo salario seria : {salario_nuevo} Euros si fueras experto en python") """

# prog. de suma de 2 numeros , su tipo y ub. en la memoria y comprobar que no es un string

""" x=2; y=4; z=x+y
print(x)
print(y)
print(z)
print(type(x))
print(type(y))
print(type(z))
print(id(x))
print(id(y))
print(id(z))
if isinstance(x,str):
    print("es string")
else:
    print("no es string")
if isinstance(y,str):
    print("es string")
else:
    print("no es string")
if isinstance(z,str):
    print("es string")
else:
    print("no es string")
 """
#programa de acciones santander
#1
""" x= 3.1456
y= 2.987
z= 3.5
print("los numeros enteros son:",int(x),"/",int(y),"/",int(z))""" 
#2
"""entero=float(input("introduzca el numero: "))

print(f"el resultado entero es: {int(entero)}") """
#3
""" lista=[3.1456,2.987,3.5]
for i in lista:
    print(int(i))
    print(round(i))#rendea el numero """

# fecha
""" import datetime

today=datetime.date.today()
print(today)
print(today.strftime("%A, %d %B %Y")) """

# matemathica

""" import math
x=4.56
y= math.floor(x)
j= math.ceil(3.4)
print(y,j) """

# si una variable comparte el mismo id con otra, no importa si se elimina la variable principal
# las demas continuararn con el mismo id, ya que elimina la variable pero no el conteniudo si se comparte.
""" import gc
a=[1,2,3]
b=a
c=b
print(f"id de a: {id(a)} b: {id(b)} c: {id(c)} ")
del a
gc.collect()
print(f"b: {id(b)} c: {id(c)} ") """