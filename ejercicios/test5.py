# prog. para estudiar listas

""" a= {10,20,30,40} 
b={30,40,50,60}
print(a.union(b)) """# union

""" a= {10,20,30,40}
b={30,40,50,60}
print(a.intersection(b)) """ # intersection

""" a= {10,20,30,40}
b={30,40,50,60}
print(a.difference(b)) """ # difference

""" a= {10,20,30,40}
b={30,40,50,60}
print(a.symmetric_difference(b)) """ # symmetric difference

#lista con range

""" x= range(10)
print(x)
print(list(x))

b= range(10,16)
print(list(b))

c= range(12,22,3)
print(list(c))

d= range(100,-1,-1)
print(list(d))
 """

# lista , tuple ,set
""" x = [6,7,"hola",True] # lista,mutable,con orden
y = (6,7,"hola",True) #tuple,inmutable, con orden
z = {6,7,"hola",True,} # set,inmutable,sin orden, sin duplicado
print(type(x))
print(type(y))
print(type(z)) """

 # lista

""" x = [6,7,"hola",True,6]
print(x)
x.append(4)
x.append("mario")
print(x)
print(x[2])
print(x[-1])#imprime el ultimosea cual sea el final
print(dir(x))# muestra todo lo que se puede hacer con la lista

print(x[:3])#imprime del 0 hasta el 3
print(x[2:5])# imprime del 2do al 5to
print(x[1:6:2])# imprime del 1 al 6 saltando de 2 en 2

y = x[3:6] # guarda una lista y con los parametros de x
print(y)
z = x+y #une las 2 lista, agrega al final
print(z) """

# lista con for

""" frutas = ["kiwia","manzanas","naranjas"]
for i in frutas:
    print(" ",i,end="") """

""" return n * factorial(n-1) """

# set
""" par= set({2,4,6,8,9,10,11,12,13,14})
impar= {1,3,5,7,9}
print(1 in impar)
impar.add(11)#no hace nada
impar.remove(11)#no hace nada
print(impar)
impar.discard(11)# borra el numero
impar.discard(11)
print(impar)

for i in impar:
    print(i)
    
x= par|impar# el | es la union de los 2 sets
print(x)
j= par.union(impar)# union
print(j)

impar.update({30,40,50})#agrega, se actualiza el set
print(impar)
 """