import tkinter as Tk

# Creamos la función que se ejecutará al presionar el botón
def saludo():
    label_resultado.config(text="Hola alumnos de Python")  # aquí debe ser "text"

# Creamos la ventana principal
ventana = Tk.Tk()
ventana.title("Ejemplo de Botones")

# Le damos un tamaño a la ventana
ventana.geometry("400x300")

# Crear Botón
boton = Tk.Button(ventana, text="Saludar", command=saludo)
boton.pack(pady=20)

# Creamos una etiqueta vacía que luego se actualizará
label_resultado = Tk.Label(ventana, text="", font=("Arial", 16, "bold"))
label_resultado.pack(pady=20)

# Mostramos la ventana
ventana.mainloop()
