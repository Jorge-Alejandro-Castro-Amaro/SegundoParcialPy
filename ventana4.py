import tkinter as Tk
from tkinter import ttk

def mostrar_texto():
    texto = entrada.get()
    label_resultado.config(text=f"Escribiste: {texto}")
    
ventana = Tk.Tk()
ventana.title("Ejemplo con Entry")
ventana.geometry("400x300")

#Creamos la entrada del texto
entrada = Tk.Entry(ventana, font=("Arial", 14))
entrada.pack(pady=20)

boton= ttk.Button(ventana, text="Enviar", command = mostrar_texto)
boton.pack()

label_resultado = ttk.Label(ventana, text="")
label_resultado.pack(pady = 20)

ventana.mainloop()