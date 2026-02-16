'''
Docstring for 08-Funciones
Las funciones en python son bloques de codigos reutilizabeles que realizan una tarea especifica.
Sirven para organizar, reutilizar y hacer mas claro el codigo.

Para que sirven?

*Evitan Repetir codigo
*permite dividir un problema grande en partes pequeñas.
*Hacen el programa mas facil de mantener.
*Mejoran la legilibidad.

#En python se definen con la palabra def:
# 
# de nombre_funcion(parametros):
#    #Bloque de codigo.
#    return valor
# 
'''

def nombre(): #Funcion que no recibe nada ni regresa nada.
    print("Hola Mundo")
nombre() 

def suma():
    a = 6
    print("Dentro de la funcion: ", a)
    
    b = 7
    c = a + b
    return c

print("la suma es: ", suma())
a = 3
print("Fuera de la funcion: ", a)
b = 7
c = a + b


def multiplicacion(a,b):
    return a*b

print("La multiplicacion es: ",multiplicacion(6, 7 ))