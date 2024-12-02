import requests
# ejerci.1 introduce el numero del postque quieres ver e imprime el post y su tituli
""" num=input("introduce el numero del post que deseas ver: ")
url="https://jsonplaceholder.typicode.com/posts/"
rl= url+num
r = requests.get(rl)
datos= r.json()
print(type(datos))
print(datos)
print(datos["title"])
 """
# ejerci.2 muestra todos los posts que hay en la api

""" url="https://jsonplaceholder.typicode.com/posts/"
r = requests.get(url)
datos= r.json()
print(type(datos))
for dato in datos:# imprime todos los posts
    print(dato)
    print("\n")
for dato in datos:# imprime todos los titulos de los posts
    print(dato["title"])
    print("\n") """
# ejr.3 mostrar datos
""" datos_tlf= {}
url="https://api.restful-api.dev/objects"
r = requests.get(url)
datos= r.json()
print(" lista de dispositivos disponibles: ")
print("\n")

for dato in datos:
    print(dato["name"])
    print("\n")
for dato in datos:
    if dato["data"]!=None:
        datos_tlf.update(dato["data"])
for dato in datos_tlf:
    print(dato)
 """
# imcompleto, terminar