#formateo de cadenas
texto:str="hola"# es solo visual para ayudar a identificar

print(f"{texto:<10}")# alinea a la izquierda
print(f"{texto:>10}")# alinea a la derecha
print(f"{texto:^10}")# alinea al centro
print(f"{texto:*^10}")# alinea al centro con asteriscos

x=0.6766
print(f"{x:.2f}")
print(f"{x:.2%}")

b=6453869
print(f"{b:,}")