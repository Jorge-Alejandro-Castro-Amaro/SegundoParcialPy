import os

os.system("cls")

alumnos = []
while True:
    try:
        num = int(input("Cuantos alumnos quieres registrar.? "))
        break
    except ValueError:
        print("Error: Porfavor ingresa un numero entero valido.")