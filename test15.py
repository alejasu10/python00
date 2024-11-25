###
def incriptar(texto):
    
    for letra in texto:
        print(ord(letra) + 1," ",end="")
        
def decriptar(texto):
    
    for letra in texto:
        print(chr(letra-1))


if __name__ == "__main__":
    texto=input("Intruce tu texto para incriptar:  ")
    palabra=[]
incriptar(texto) 
palabra.append(incriptar(texto))
print(palabra)

# no terminado


""" texto= "hola"
numero=[]
for i in texto:
    print(ord(i) + 1)
    numero.append(ord(i) + 1)
for i in numero:
    print(chr(i-1)) """

