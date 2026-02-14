alumno = {
    "nombre": "Ana",
    "edad": 21,
    "carrera": "ingenieria"
}

alumno1 = {
    "nombre": "",
    "edad": 0,
    "carrera": ""
}

icco201={alumno1, alumno1, alumno1, alumno1}

print(type(alumno))
print(alumno)

print("print(alumno['nombre']) = ", alumno["nombre"])
print("print(alumno.get('edad') = ", alumno.get("edad"))

#Agregar o modificar valores

alumno["promedio"] = 9.2
print(alumno)
alumno["edad"] = 22
print(alumno)   

#Eliminar un par de clave-valor
del alumno["carrera"]
print(alumno)

#Recorrer un diccionario
for clave in alumno:
    print(clave, ":", alumno [clave])
    
#Funciones utiles para diccioanrios

print("Cantidad de pares clave-valor: ", len(alumno))
print("Claves del diccionario: ", alumno.keys())
print("Valores del diccionario: ", alumno.values())
print("Pares clave-valor: ", alumno.items())

