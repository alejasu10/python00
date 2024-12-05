# Programa para obtener IVA 
# paso 1-El cliente introduce el precio y el IVA.
# paso 2-El Progrma calcula e imprime el recibe con el precio del producto, IVA y Total con IVA.
# Notas: El valor de Precio debe ser positivo, de lo contrario imprime error.
# Notas: El Valor del IVA

""" precio=float(input("introduza el precio: "))
if precio>0:
    iva=float(input("introduce el iva en % : "))
    if iva>0 and iva<=100:
        iva_valor=precio * (iva/100)
        total=precio + iva_valor
        print("\n")
        print("Recibo: ")
        print(f"el precio es: {precio} €")
        print(f"el IVA es : {iva_valor:.2f} €")
        print(f"El precio Total es: {total:.2f} € en total")
    else:
        print("El IVA introducido no es correcto.")
else:
    print("El Precio no puede ser negativo.") """