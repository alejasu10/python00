### este programa sirve para convertir grados de C a F y viceversa """
x= float(input("introduzca el grado a convertir: "))
y= int(input("que deseas conevrtir: 1 = C a F, 2 = F a C"))

if y == 1:
    fahrenheit = x* 1.8 + 32
    print(f"fahrenheit {fahrenheit: .1f}")
elif y == 2:
    c = (x -32) / 1.8
    print(f"fahrenheit {c: .1f}")

else:
    print(f"error")