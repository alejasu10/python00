# 1 mostrar un set con correos unicos
# sin duplicar(correos unicos)

# 2 queremos saber quienes son los nuevos suscriptores,osea dave y ellen

empleados= ["alice@example.com", "bob@example.com", "carol@example.com", "bob@example.com","alice@example.com"]
# 3 teniendo una lista de empleados
#queremos sacar los empleados unicos
# en formato lista[] no set
# f1

""" 
empleados_unicos=[]
for empleado in empleados:
    if empleado not in empleados_unicos:
        empleados_unicos.append(empleado)

for i in range(len(empleados_unicos)):
    print(empleados_unicos[i]) """

#f2
""" empleados_unicos= set((empleados))
print(list(empleados_unicos)) """

############################################################################
# funiones con **kwargs/*args, dicionarios
""" def hello(**kwargs):
    print(type(kwargs))#<class 'dict'>
    if "ing" in kwargs:
        print(kwargs["ing"])
    if "esp" in kwargs:
        print(kwargs["esp"])
    if "eus" in kwargs:
        print(kwargs["eus"])
    if "viet" in kwargs:
        print(kwargs["viet"])

hello (ing= "hello",esp="hola",eus="kaixo",viet="xin chao") """

# ejerc.
# f1
""" def enviar_correo(**kwargs):
    if "recipiente" in kwargs:
        print(f"enviando correo a {kwargs['recipiente']}")
    if "asunto" in kwargs:
        print(f"asunto: {kwargs['asunto']}")
    if "cuerpo" in kwargs:
        print(f"cuerpo: {kwargs['cuerpo']}")
    
enviar_correo (recipiente="ckulhan@nazaret.eus",asunto="hola",cuerpo="hola, que tal?")
enviar_correo (recipiente="pablo@nazaret.eus",asunto="hola",cuerpo="hola, que tal?") """


#F2
""" def enviar_correo(**kwargs):
    print(f"enviando correo a {kwargs['recipiente']}")
    if "asunto" in kwargs:
        print(f"asunto: {kwargs['asunto']}")
    if "cuerpo" in kwargs:
        print(f"cuerpo: {kwargs['cuerpo']}")
    
enviar_correo (recipiente="ckulhan@nazaret.eus",asunto="hola",cuerpo="hola, que tal?")
enviar_correo (recipiente="pablo@nazaret.eus",asunto="hola",cuerpo="hola, que tal?") """

#########################################################################
# diccionario con acciones

""" acciones = {"MSFT": 412, "NVDA":143,"REP":9 }
print(type(acciones))#<class 'dict'>

print(acciones["MSFT"])

for k, v in acciones.items():
    print(k,v)# imprime la clave y el valor
print("\n")
for k in acciones.keys():
    print(k)# imprime solo las claves
print("\n")
for k in acciones.values():
    print(k)# imprime solo los valores

acciones["MSFT"] =120
print("\n")
print(acciones["MSFT"])# actualiza la clave
acciones["BBVA"]=130 # si no exites lo agrega
print("\n")
print(acciones["BBVA"])
print(acciones)
acciones.update({"ANA":200,"FX":150})# actualiza y agrega
print("\n")
print(acciones) """

#ejerc.
# Llevar a cabo las siguientes tareas, usando estos datos de acciones en la bolsa española:
# 1- Crear un diccionario para almacenar las acciones en VERDES y su precio actual. 
# 2- Mostrar el valor de BBVA (print())
# 3- Después, usando update(), agregar las acciones en ROJO. 
# 4-Sumar el total de precios y imprimirlo al final
# 5 - Excluir SANtander del cálculo total de compra
# 6 -Imprimir los valores de cada acción en esta lista de acciones:
# acciones = {"MSFT": [91.5, 54.1, 76.4], "REP": [7.91, 5.6, 6.7], "BBVA": [6.9]}
""" acciones ={"MSFT": 143.75,"REP.MC": 14.22,"BBVA":6.34,"SAN.MC":3.324} #1
print(acciones["BBVA"])#2
acciones_2={"OHLA.MC":0.518,"ANE.MC":34.32,"TEF.MC":3.811}
acciones.update(acciones_2)#3
print("\n")
total=0
for k,v in acciones.items():
    if k!="SAN.MC":#5
        total+=v
        print(f"{k}: {v}")
print("\n")
print(f"El Total de las acciones es: {total}")#4

#6
acciones2 = {"MSFT": [91.5, 54.1, 76.4], "REP": [7.91, 5.6, 6.7], "BBVA": [6.9]}
print("\n")

for k,v in acciones2.items():
    for i in v:
        print(f"{k}: {i}") 
        """
    

