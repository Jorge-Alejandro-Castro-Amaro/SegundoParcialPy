import tkinter as Tk

# Creamos la ventana principal

ventana = Tk.Tk()   # Aquí debe ser Tk.Tk(), no Tk.TK()

# Le damos un título a la ventana
ventana.title("Mi primera aplicación")

# Le damos un tamaño a la ventana
ventana.geometry("400x300")

# Creamos una etiqueta
etiqueta = Tk.Label(ventana, text="Hola mundo", font=("Arial", 16, "bold"))
# El argumento correcto es "text", no "tex"
# En la fuente, "bold" debe ir en minúsculas

etiqueta.pack(pady=20)

# Mostramos la etiqueta en la ventana
ventana.mainloop()
