#Programacion Orientada a Objetos

class Persona:
    
    def inicializar(self, nom):
        self.nombre = nom 
        
    def imprimir(self):
        print("Nombre", self.nombre)
        
        
#Bloque Principal

persona1 = Persona() #Creando un objeto
persona1.inicializar("Pedro") #Asignar el nombre
persona1.imprimir() #Imprimir el nombre

persona2 = Persona() #Creando un objeto
persona2.inicializar("Carla")
persona2.imprimir()

#Definir el objeto
class operasBas:
    n1 = 0
    n2 = 0
    res = 0
    def sumar(self, a,b):
        return a+b
    
#Pedir numeros con variable def y self
    def pedirNumeros(self): #Es parte de la clase y siempre debe estar entre ()
        self.n1 = int(input("n1: "))
        self.n2 = int(input("n2: "))
        print("La suma es:", self.sumar(self.n1, self.n2))
        
obj = operasBas()

obj.pedirNumeros()

