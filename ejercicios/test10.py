# devover la palbra al revez con funcion
""" def reversa(palabra):
    stri=""
    for i in range(len(palabra)-1,-1,-1):
        stri += palabra[i]
    return stri

if __name__ == '__main__':

    lista = ["h","o","l","a"]
    for i in range(len(lista)):
        print( lista[i],"",end="")
    print("\n")
res= reversa(lista)
print(res,"",end="") """


#2

""" def reversa(palabra):
    return palabra[::-1]

if __name__ == '__main__':

    lista = "hola"
    for i in range(len(lista)):
        print( lista[i],"",end="")
    print("\n")
res= reversa(lista)
print(res,"",end="")
     """

     # factorial 
""" def factorial(n):
        if n == 0:
            return 1
        else:
            
            for i in range(n-1,1,-1):
                 n = n*i
            
            return n

if __name__ == "__main__":
    num = int(input("Ingrese un número: "))
    print(f"El factorial de {num} es: {factorial(num)}") """

# factorial 2
""" def factorial(num):
        if num == 0:
            return 1
        else:
            
            
            return num * factorial(num-1)

if __name__ == "__main__":
    num = int(input("Ingrese un número: "))
    print(f"El factorial de {num} es: {factorial(num)}") """
    