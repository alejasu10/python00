# prubas para crear tablas
""" ListasAlumnos = [['Juan', 'Carmelo', 5, 7, 9, 7], ['Laura', 'Jazmine', 7, 8, 5, 6.66],
 ['Dario', 'Villalobos', 5, 6, 3, 4.66], ['Marito', 'Tasolo', 4, 7, 9, 6.666],
  ['Esteban', 'Quito', 9, 9, 8, 8.66]]
# Tabla = """\
# +---------------------------------------------------------------------+
# | Nombre    Apellido        Primero Segundo Tercero     Promedio anual|
# |---------------------------------------------------------------------|
# {}
# +---------------------------------------------------------------------+\
"""
Tabla = (Tabla.format('\n'.join("| {:<8} {:<10} {:>8} {:>6} {:>7} {:>23} |".format(*fila)
 for fila in ListasAlumnos)))
print (Tabla)
 """

#  2
""" Nombre = input(str("Ingresa tu nombre \n"))
Edad = int(input("Bien, ahora ingresa tu edad \n"))
NombreMascota = input(str("Ingresa el nombre de tu mascota \n"))
print ("Tu nombre es {0} y tienes {1} años. Tu mascota se llama {2}".format(Nombre, Edad, NombreMascota)) """
#3
""" a = 'abra'
b = 'cad'
print('{0:<5}{1:^5}{0:>5}'.format(a, b)) """



ListasAlumnos = [['Juan', 'Carmelo', "a1", "VA077"], ['Laura', 'Jazmine', "c1", "VA077"],]
Tabla = """\
+------------------------------------------------+
| Nombre      Apellido      Asiento       Vuelo  |
|------------------------------------------------|
{}
+------------------------------------------------+\
"""
Tabla = (Tabla.format('\n'.join("| {:<8} {:>11} {:>10} {:>14} |".format(*fila)
 for fila in ListasAlumnos)))
print (Tabla)