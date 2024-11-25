import os

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

clear()

#2


from os import system

system("cls")