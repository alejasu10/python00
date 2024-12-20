# Programa de color
color = input("¿Cúal es tu color favorito?")

if color.lower() == "red":
  print("Lo mio es rojo también")
else:
  print(f"Mi color favorito es rojo, no {color}")

  
# Zara productos
qty = int(input("¿Cúal es la cantidad?"))

if qty <0 or qty > 10:
  print("Error: Introducir una cantidad >= 1 y <= 10")
else:
  print("Acceptado")
  
# Gastos de electricidad
cantidad = 100000

if cantidad > 1000:
  print("Has gastado mucho este mes")
elif cantidad > 500:
  print("Has gastado bastante este mes")
elif cantidad > 100:
  print("Has gastado poco este mes")
else:
  print("No has gastado nada este mes")

# Gastos de electricidad usando match
gasto = float(input("Introduce el gasto de electricidad del cliente en euros: "))

# Usar match para mostrar el mensaje correspondiente según el rango de gasto
match gasto:
    case _ if gasto >= 0 and gasto <= 99:
        print("No has gastado nada este mes.")
    case _ if gasto >= 100 and gasto <= 499:
        print("Has gastado poco este mes.")
    case _ if gasto >= 500 and gasto <= 999:
        print("Has gastado bastante este mes.")
    case _ if gasto >= 1000:
        print("Has gastado mucho este mes.")
    case _:
        print("El valor ingresado no es válido.")

# super poderes
print("Elige un superpoder:")
print("1) Volar")
print("2) Invisibilidad")
print("3) Superfuerza")
poder = input("Introduce tu opción: ")

if poder == "1":
    print("¡Eres un héroe alado!")
elif poder == "2":
    print("¡Eres el Hombre Invisible!")
elif poder == "3":
    print("¡Eres increíblemente fuerte!")
else:
    print("¡Esa no es una opción válida!")


# ----------------------------------------
# carta usando match 
pedido = input("Qué quieres tomar?")

match pedido.lower():
  case "café":
      print("Has seleccionado Café. El precio es $2.50.")
  case "té":
      print("Has seleccionado Té. El precio es $1.80.")
  case "jugo":
      print("Has seleccionado Jugo. El precio es $3.00.")
  case "sándwich":
      print("Has seleccionado Sándwich. El precio es $4.50.")
  case "muffin":
      print("Has seleccionado Muffin. El precio es $2.00.")
  case _:
      print(f"Lo siento, no tenemos {pedido} en el menú.")

# carta usando if 
pedido = input("¿Qué quieres tomar?").lower()

if pedido == "café":
    print("Has seleccionado Café. El precio es $2.50.")
elif pedido == "té":
    print("Has seleccionado Té. El precio es $1.80.")
elif pedido == "jugo":
    print("Has seleccionado Jugo. El precio es $3.00.")
elif pedido == "sándwich":
    print("Has seleccionado Sándwich. El precio es $4.50.")
elif pedido == "muffin":
    print("Has seleccionado Muffin. El precio es $2.00.")
else:
    print(f"Lo siento, no tenemos {pedido} en el menú.")


# respuesta sencilla de actividad con match de la discoteca
edad = 26

match edad:
    case _ if edad< 18 or edad > 65:
        print("Ilegal")
    case _:
        print("Puedes entrar")


# respuesta con función
def comprobar_edad_disco(edad):
    match edad:
        case _ if edad< 18 or edad > 65:
            return False
        case _:
            return True

if __name__=="__main__":
    edad = int(input("Cuantos años tienes"))

    if comprobar_edad_disco(edad):
        print("Puedes entrar")
    else:
        print("No peudes entrar")