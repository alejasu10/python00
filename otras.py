## ejemplo con e
""" x = 45.65e2
print(x) """

## comprobar si es un entero
""" x = 356
print(isinstance(x,int))
 """
# opcion 2
""" x = 235

i = isinstance(x,int)

loggedin = True
if loggedin :
    print("sesion iniciada") """

# mutable, inmtable

""" x = 1000
print(id(x))
x = 2000
print(id(x)) """
#"2810661479024
#"2810665027184

""" import gc
x = 1000
print("id de x: ", id(x))
del x # es un candidato para la coleccion de basura
gc.collect() #desencadenar manualmente la recoleccion de basura
print("garbage collection triggered") """

""" a = 10
print(id(a))
b = 10
print(id(b))
# 140717451175112
# 140717451175112 """

#mutables

""" lista = [15,9,4,6]
print(id(lista))
lista.append(22)
print(id(lista))
print(lista) """
# 3049477005376
# 3049477005376