# test de random
""" import random
nombres= ['Arturo','Julio','Dani','Aurora','Roberto','Martina']
x=random.choice(nombres)
print(x) """

# 2
""" import random
nombres= ['Arturo','Julio','Dani','Aurora','Roberto','Martina']
x=random.choices(nombres,[0,10,0,0,0,0])
print(x) """

# prog de mate
""" 
import math as m

x= 15.6547

print(m.ceil(x))#redondea hacia arriba
print(m.floor(x))#redondea hacia abajo
print(m.pow(4,3))# numero elevado
print(m.gcd(6,9))#imprie el divisor comun
print(m.factorial(4))#imprime el factorial
print(m.e)#valor del exponencial
print(m.pi)#valor de pi """

# estadistica
""" import statistics as st

notas=[2,6,7,3,7]
print(st.mean(notas))#media
print(st.median(notas))#valor medio
 """
#lista de compresion

""" x=[i**2 for i in range(10) if i%2==0] 
print(x) """ # ejemplo de una lista de compresion

# ejerc1
# prog para sacar los numeros positivos de una lista de varios numeros
# usando lista de compresion

""" numeros=[3,54,-12,4,-67,99,120]
x=[i for i in numeros if i>0]
print(x)

for i in range(len(x)):
    print(x[i]," ",end="") """

# ejerc2
#numero par conlista de compresion

""" numero=[2,6,7,3,4,8]
x=[i for i in numero if i%2==0]
print(numero)
print(x)
for i in range(len(x)):
    print(x[i]," ",end="") """
#ejr.3
# imprimir par o impar
numero=[1,2,3,4,5,6,7,8,9]
letras=["par" if i%2==0 else "impar" for i in numero]
print(letras)
x=[i for i in numero if i%2==0 ]
print("numeros pares:",x)
y=[i for i in numero if i%2!=0]
print("numeros impares:",y)
j=["par" for i in numero if i%2==0 ]
print(j)