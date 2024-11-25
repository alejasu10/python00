# prog. para comprar asientos de avion.
import random

asi= [["a1", "a2", "a3","a4"],["b1", "b2", "b3", "b4"],["c1", "c2", "c3", "c4"]]
nombre=[]
comp2=[]
compra=input("desea comprar tickets de avion:  (s/n)",)


if compra=="s":
    boletos=int(input("Cuantos tickets desea comparar: "))
    asientos=input("Desea escoger los asientos:   (s/n)",)
    if asientos=="s":
        for i in range(len(asi)):
            for j in range(len(asi[i])):
                print(f"Asiento disponibles: {asi[i][j]}")
            print("\n")

        for i in range(boletos):
            nombre.append(input(f"Nombre del {i+1}º pasajero: "))    
            comp=input("escoja el asiento: ")
            comp2.append(comp)
            for i in range(len(asi)):
                for j in range(len(asi[i])):
                    if comp==asi[i][j]:
                        asi[i][j]="ocupado"
                        print("Compra exitosa ")
                        print("\n")
             
        for i in range(len(asi)):
            for j in range(len(asi[i])):
                if asi[i][j]!="ocupado":
                    print(f"Asientos disponibles: {asi[i][j]}")

        print("\n")
        print("Asientos ocupados: ")
        for i in range(len(nombre)):
            print(f"{nombre[i]} - {comp2[i]}")

    elif asientos=="n":

        for i in range(len(asi)):
            for j in range(len(asi[i])):
                print(f"Asiento disponibles: {asi[i][j]}")
        print("\n")

        for i in range(boletos):
            nombre.append(input(f"Nombre del {i+1}º pasajero: "))    
            comp= random.choice(asi[i])
            comp2.append(comp)
            
            for i in range(len(asi)):
                for j in range(len(asi[i])):
                    if comp==asi[i][j]:
                        asi[i][j]="Ocupado"
                        print("Compra exitosa ")
                        break
            print("\n")
            
        for i in range(len(asi)):
                for j in range(len(asi[i])):
                    if asi[i][j]!="Ocupado":
                        print(f"Asientos disponibles: {asi[i][j]}")
        
        print("Asientos ocupados: ")
        for i in range(len(nombre)):
            print(f"{nombre[i]} - {comp2[i]}")

    else:
        print("Opción invalida")
    
else:
    print("Compra cancelada")
           