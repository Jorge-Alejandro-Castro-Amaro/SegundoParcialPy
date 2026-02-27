import tkinter as Tk
import os
from tkinter import ttk
from tkinter import messagebox

#El proceso de operacion, definimos las variables para que al llamar solo la funcion, ejetute correctamente la operacion de suma
def suma():
    try:
        os.system("cls")
        a = float(entrada1.get())
        b = float(entrada2.get())
        resultado = a + b
        etiqueta_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa un numero valido")
        
#Creamos la ventana, con nombre, la geometria o tamano de la ventana
ventana = Tk.Tk()
ventana.title("Calculadora de suma")
ventana.geometry("400x300")

#Crear etiqueta para mostrar que debes ingresar
Tk.Label(ventana, text="Ingrese el primer valor").grid(row=0, column=0, padx=5, pady=5)
#Agregar el cuadro para ingresar el numero
entrada1 = Tk.Entry(ventana)

#Para que los valores que metan en el recuadro se guarden y podamos hacer la operacion
entrada1.grid(row=0, column=1, padx=5, pady=5)

#Crear etiqueta para mostrar que debes ingresar
Tk.Label(ventana, text="Ingrese el segundo valor").grid(row=1, column=0, padx=5, pady=5)
#Agregar el cuadro para ingresar el numero
entrada2 = Tk.Entry(ventana)
#Para que los valores que metan en el recuadro se guarden y podamos hacer la operacion
entrada2.grid(row=1, column=1, padx=5, pady=5)

#Creamos el boton, para que cuando se presione ejecute la operacion y muestre el resultado
Tk.Button(ventana, text="Calcular", command=suma).grid(row=2, column=0, columnspan=2, pady=10)

#Crear la etiqueta 
etiqueta_resultado = ttk.Label(ventana, text="")
etiqueta_resultado.grid(row=2, column=1, columnspan=2, pady=10)

#Mostrar la ventana
ventana.mainloop()