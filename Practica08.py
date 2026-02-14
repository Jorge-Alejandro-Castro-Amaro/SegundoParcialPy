import os

os.system("cls")

alumno1 = {
    "nombre": "",
    "edad": 0,
    "carrera": ""
}

ico201 = []
num = int(input("Cuantos alumnos deseas ingresar.? "))

for i in range(num):
    nombre = input("Nombre del alumno: ")
    edad = int(input("Edad del alumno: "))
    carrera = input("Carrera del alumno: ")
    
    alumno1["nombre"] = nombre
    alumno1["edad"] = edad
    alumno1["carrera"] = carrera
    
    ico201.append(alumno1.copy())
    
print("Lista de alumnos ingresados: ")
for alumno in ico201:
    print(alumno)