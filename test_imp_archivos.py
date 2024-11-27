""" f = open("abc.txt", "r")# "r" es read, "w" es write son los parametros de open
print(f.read())# esta leyedo el texto
print(f.encoding)
print(f.name)
f.seek(0) # esta es para volver al principio del archivo
s=f.readline()# lee la 1primera linea
print(s)
for l in f.readlines(): # lee todas las lineas
    print(l)
f.close()
 """
""" # Esta es para escribir en el archivo
f=open("abc.txt", "w")
f.write("Hola mundo!\n")# esta es para escribir en el archivo
f.close()# este cierra el archivo """

# forma mas actualizada, mas facil
""" with open("abc.txt", "r",encoding="utf-8") as f:
    print(f.read())
    print(f.encoding)
    print(f.name)
    f.seek(0)
    s=f.readline()
    print(s)
    for l in f.readlines():
        print(l) """
    
# escribiendo mas actualizada
""" with open("abc.txt", "w") as f:
    f.write("Hola mundo!\n") """
# agregar sin borrar
""" with open("abc.txt", "a") as f:
    f.write("Adiós mundo!\n")
with open("abc.txt", "r") as f: # imprime lo que has agregado
    print(f.read()) """
########################
# ejercicio 1 solo leer y escribir:

""" with open("agatha.txt", "r") as f:# leyendo
    print(f.read())

with open("escribir.txt", "w") as f:
    f.write("The ABC Murders – 1936 The Adventure of the Christmas Pudding – 1960")# escribir nuevo arch

with open("escribir.txt", "r") as f:#leer el archivo nuevo
    print(f.read())
with open("escribir.txt", "a") as f:
    f.write("\nThe Adventure of the Sleeping Beauty – 1950")# añadiendo nuevo texto al archivo

with open("escribir.txt", "r") as f:# leyendo el archivo que escribimos linea por linea
    for line in f.readlines():
        print(line)
 """

# leer un archivo csv, tomar parametros y escribirlo en un archivo nuevo
import csv

with open("addresses.csv", "r", encoding="utf-8") as f, open("escribir_2.txt", "w", encoding="utf-8") as nuevodoc:
    reader = csv.reader(f)# lee el archivo csv
    linea=list(reader)# transforma en lista para poder buscar una linea en especifico
    for  i in linea:
        print("  ".join(i))# imprime todas las lineas de csv en formato de lista
        
    print(" ".join(linea[0]))# imprime la linea 0 del archivo csv, la linea especifica que le pido
    
    nuevodoc.write(" ".join(linea[0]))# escribe en el archivo nuevo con la linea que le doy
