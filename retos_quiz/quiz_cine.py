import random
from os import system

# Diccionario con preguntas y respuestas - key son preguntas, values son respuestas correctas
quiz_data = {
    "¿En qué película aparece la frase 'Yo soy tu padre'?": "Star Wars",
    "¿Qué película tiene el récord de ser la más taquillera de todos los tiempos (hasta 2024)?": "Avatar",
    "¿Quién dirigió la película 'El laberinto del fauno'?": "Guillermo del Toro",
    "¿Qué película presenta al personaje 'Jack Sparrow'?": "Piratas del Caribe",
    "¿Qué película animada está ambientada en el Día de los Muertos?": "Coco",
}

print("🎥 ¡Bienvenido al Quiz de Películas! 🎥")
print("Responde las siguientes preguntas para poner a prueba tu conocimiento sobre películas.")
print("-" * 50)
enter=input("presioene una tecla para continuar para continuar")
system("cls")


preguntas = list(quiz_data.keys()) # convertir los keys en una lista
# usar un método de random para barajar las preguntas
random.shuffle(preguntas)

num_correctas = 0 # contador de preguntas correctas
for pregunta in preguntas: # bucle para iterar por todas las preguntas
    print(pregunta)
    respuesta = input("introduce tu respuesta:  ")# preguntar al usuario por su respuesta
    if respuesta.lower() == quiz_data[pregunta].lower():# usar .lower() para comprarar 
        num_correctas += 1 # aumentar el contador de preguntas correctas
        print("Respuesta correcta!")
    # si su respuesta es igual que la del quiz_data, es correcto!
    else: # si su respuesta es incorrecta
        print(f"Respuesta incorrecta! La respuesta correcta era: {quiz_data[pregunta]}")
    print("-" * 50)
    enter=input("presiona una tecla para continuar para continuar")
    system("cls")
match num_correctas:
    case 0:
        print("Vives en un bunquer, no sabes nada del mundo cinematografico!")
        print(f"El numero de respuestas correctas Fueron: {num_correctas}")
    case 1:
        print("Esta fue de suerte o Que, Sal al Cine!")
        print(f"El numero de respuestas correctas Fueron: {num_correctas}")
    case 2:
        print("Sabes muy poco, ponte a ver Peliculas!")
        print(f"El numero de respuestas correctas Fueron: {num_correctas}")
    case 3:
        print("Se ve que sabes, ve un poco mas de peliculas.!")
        print(f"El numero de respuestas correctas Fueron: {num_correctas}")
    case 4:
        print("uff casi completas todo perfecto!")
        print(f"El numero de respuestas correctas Fueron: {num_correctas}")
    case 5:
        print("Felicidades Completaste todo con exito!")
        print("eres todo un guru del cine")
    

# al final, mostrar los numeros correctos
