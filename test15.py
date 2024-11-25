### cifrar una palabra ejemplo-
""" texto= "hola"
numero=[]
for i in texto:
    print(ord(i) + 1)
    numero.append(ord(i) + 1)
for i in numero:
    print(chr(i-1)) """
####
# pedir al usuario que ingrese una palabra y cifrarla, despues decifrarla.
# prog. de practica
""" def encriptar(texto):
    cifrado = []
    for letra in texto:
        cifrado.append(ord(letra) + 1)
    return cifrado

def descifrar(numeros):
    texto_original = ""
    for num in numeros:
        texto_original += chr(num - 1)
    return texto_original

if __name__ == "__main__":
    # Encriptado
    texto = input("Introduce tu texto para encriptar: ")
    codigo_cifrado = encriptar(texto)
    
    msg = " ".join(map(str, codigo_cifrado))# convierte en string el codigo cifrado con la funcion map
    print("Texto cifrado:", msg)
    
    # Desifrado
    texto_descifrado = descifrar(codigo_cifrado)
    print("Texto descifrado:", texto_descifrado) """
    
# pedir al usuario que ingrese los numeros y decifrarlos
""" def descifrar(numeros):
    texto_original = ""
    for num in numeros:
        texto_original += chr(num - 1)
    return texto_original

if __name__ == "__main__":
    # Desifrado
    numeros = list(map(int, input("Introduce los numeros separados por espacios: ").split()))
    texto_descifrado = descifrar(numeros)
    print("Texto descifrado:", texto_descifrado) """
##########

