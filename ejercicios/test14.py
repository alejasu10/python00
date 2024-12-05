#ejercicio de diccionario
""" import statistics as s
temperaturas = {
    "Enero": 5,
    "Febrero": 7,
    "Marzo": 10,
    "Abril": 18,
    "Mayo": 20,
    "Junio": 25,
    "Julio": 28,
    "Agosto": 28,
    "Septiembre": 22,
    "Octubre": 18,
    "Noviembre": 12,
    "Diciembre": 8
}
# Acceder a la temperatura de un mes específico
print("La temperatura para Diciembre es : ",temperaturas["Diciembre"])  # Imprimirá: 8

for k,v in temperaturas.items():#2 imprime solo los meses de verano
    if k in ("Junio", "Julio","Agosto"): # if k == "Junio" or k == "Julio" or k == "Agosto": otra forma.
        print(k,v)


temperaturas.pop("Marzo")#3 Borra el mes de marzo

print("\nTemperaturas después de borrar Marzo:")
for k,v in temperaturas.items():
    print(k,":",v," / ",end="")

#4 imprimir los que no estan duplicados
temperaturas_unicas = set(temperaturas.values())
print("\nTemperaturas únicas:",temperaturas_unicas)

#5 calcular la media

media = s.mean(temperaturas_unicas)
print(f"\nla temperatura media es: {media:.2f}")
 """

#########################
""" import json
accion =' {"nombre" : "repsol","precio" : 5}'
print(type(accion))

a = json.loads(accion)
print(a)
print(type(a))
x= str(a)
print(x)
print(type(x))
b=json.dumps({"nombre": "hola"})
print(type(b))
print(b)

 """

##############
# prog. para imprimir solo string de una lista.

"""s=[122,"Python","es",64,"un",777,"lenguaje",222,"de",55,66,"programación"]


d=[]
g="http://www.nazaret.eus"
y="ooooo Mi nombre es felipe y  mi correo es fe.suarez@aulanz.net  oooo "
for i in range(len(s)):
    if isinstance(s[i], str):
        d.append(s[i])
        print(s[i]," ",end="")# si son strings los imprime
print("\n")

for i in range(len(d)):
    f=str(d[i])
    print(f.upper()," ",end="")#mayuscula todo

print("\n")

for i in range(len(d)):
    f=str(d[i])
    print(f.split()," ",end="")# separa todo en letras, en este caso siendo una lista la separa en palabras

print("\n")

for i in range(len(d)):
    f=str(d[i])
    print(f.capitalize()," ",end="")# transforma en mayuscula solo la primera letra de las palabra

print("\n")

print(g.strip("htp:/.eus"))# qita los espacios/strip("letra") quita la letra
print(g.lstrip("htp:/").rstrip(".eus"))# qita los espacios/lstrip("letra") quita la letra del principipo y rstrip el final

y.replace("aulanz","nazaret")# reemplaza la palabra
print(y)
print(y[10:20]+y[25:30])# concadena la oracion, indica desde conde empezare y terminar """

######

""" s= "javier martinez ruiz"
lista=s.split() # converte en una lista
print(lista)
for i in range(len(lista)):
    print(lista[i])

g= " ".join(lista)# convierte nuevamente en u  strings
print(g)
 """
######### F2

""" s= "    122,python,es,64,un,777,lenguaje,222,de,55,66,programación  " 
a=s.strip()
print(a)
b= a.split(",")
print(b)
print("\n")
c=[]
for i in b:
    if not i.isnumeric():# hace a un lado los datos numericos
        c.append(i)
        print(i," ",end="")
print("\n")
print(c)
d= " ".join(c)
e=d.capitalize()
print(d.upper())
print(e) """

# ejerc.3

""" texto = "    Lo más importante que nos ha mantenido en Python... bueno, hay 2 cosas importantes. Uno son las bibliotecas. La otra cosa que nos mantiene en Python, y esto es lo más importante, es facil de leer y entender. Cuando contratamos nuevos empleados. Solo digo, 'todo lo que escribas debe estar en python'. Sólo para que pueda leerlo. Y es increíble porque puedo ver desde el otro lado de la habitación, mirando su pantalla, si su código es bueno o malo. Porque un buen código de Python tiene una estructura muy obvia. Y eso hace que mi vida sea mucho más fácil        "
print("\n")
print(texto.count("Python"))
print(texto.count("python"))
print(texto.count("PYTHON"))
print(texto.find("Python"))
print(texto.find("Python",47))
print(texto[46:54])
print(texto.replace("Python","PYTHON"))
print(texto.strip())
print(texto.swapcase()) """