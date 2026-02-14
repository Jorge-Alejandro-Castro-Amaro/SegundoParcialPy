import os

os.system("cls")

ico201 = []
num = int(input("Cuantos alumnos deseas ingresar? "))

for i in range(num):
    alumno = {}  # crear un diccionario nuevo por cada alumno
    
    alumno["nombre"] = input("Nombre del alumno: ")
    alumno["edad"] = int(input("Edad del alumno: "))
    alumno["materia"] = input("Ingrese la materia: ")
    alumno["calificacion"] = float(input("Ingresa la calificacion: "))
    
    ico201.append(alumno)  # guardar el alumno en la lista

# Pedir la materia que queremos consultar
materia_buscada = input("\n¿Qué materia quieres consultar? ")

# Filtrar alumnos por esa materia
busqueda = [alumno["nombre"] for alumno in ico201 if alumno["materia"] == materia_buscada]

print("\nAlumnos en", materia_buscada, ":", busqueda)

# Calcular promedio de esa materia
calificaciones = [alumno["calificacion"] for alumno in ico201 if alumno["materia"] == materia_buscada]

if calificaciones:  # si hay alumnos en esa materia
    promedio = sum(calificaciones) / len(calificaciones)
    print("Promedio en", materia_buscada, ":", promedio)
else:
    print("No hay alumnos en esa materia.")

# Mostrar lista completa de alumnos
print("\nLista de alumnos ingresados:")
for alumno in ico201:
    print(alumno)