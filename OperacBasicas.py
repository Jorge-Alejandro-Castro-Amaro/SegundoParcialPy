'''
Docstring for OperacBasicas

realizar 
1- +
2- -
3- *
4- /
5- salir 
'''
import math, os

def suma():
    os.system("cls")
    a = int(input("Ingrese el primer valor a sumar: "))
    b = int(input("Ingrese el segundo valor a sumar: "))
    return a+b

def resta():
    os.system("cls")
    a = int(input("Ingrese el primer valor a restar: "))
    b = int(input("Ingrese el segundo valor a restar: "))
    return a-b

def multiplicacion():
    os.system("cls")
    a = int(input("Ingrese el primer valor a multiplicar: "))
    b = int(input("Ingrese el segundo valor a multiplicar: "))
    return a*b

def division():
    os.system("cls")
    a = int(input("Ingrese el primer valor a dividir: "))
    b = int(input("Ingrese el segundo valor a dividir: "))
    if b == 0:
        return "Error: división entre cero"
    return a/b

def menu():
    opcion = 0
    while opcion != 5:
        print("\n--- MENÚ ---")
        print("1.- suma\n2.- resta\n3.- multiplicacion\n4.- division\n5.- salir")
        opcion = int(input("Seleccione una opcion (1-5): "))

        if opcion == 1:
            print("La suma es:", suma())
        elif opcion == 2:
            print("La resta es:", resta())
        elif opcion == 3:
            print("La multiplicacion es:", multiplicacion())
        elif opcion == 4:
            print("La division es:", division())
        elif opcion == 5:
            print("Saliendo del programa...")
        else:
            print("Opción inválida, intente de nuevo.")

# Ejecutar menú
menu()

'''import math, os

def suma():
    a = int(input("Ingrese el primer valor a sumar: "))
    b = int(input("Ingrese el segundo valor a sumar: "))
    return a+b

def resta():
    a = int(input("Ingrese el primer valor a restar: "))
    b = int(input("Ingrese el segundo valor a restar: "))
    return a-b

def multiplicacion():
    a = int(input("Ingrese el primer valor a multiplicar: "))
    b = int(input("Ingrese el segundo valor a multiplicar: "))
    return a*b  

def division():
    a = int(input("Ingrese el primer valor a dividir: "))
    b = int(input("Ingrese el segundo valor a dividir: "))
    return a/b

def menu():
    print("1.- suma\n2.- resta\n3.- multiplicacion\n4.- division\n5.- salir")
    opcion = int(input("Seleccione una opcion (1-5): "))

    opcion = 0

    while opcion != 5:
        
        if opcion == 1:
            
            print("La suma es: ", suma())
                
        if opcion == 2:
            print("La resta es: ", resta())
            
        if opcion == 3:
            print("La multiplicacion es: ", multiplicacion())
            
        if opcion == 4:
            print("La division es: ", division())       
            
        elif opcion == 5:
                break
'''