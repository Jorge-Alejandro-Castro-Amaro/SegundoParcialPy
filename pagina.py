import tkinter as Tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Precio unitario del boleto
boleto = 14

def procesar():
    try:
        nombre = entry_nombre.get()
        num_personas = int(entry_personas.get())
        num_boletos = int(entry_boletos.get())
        usa_cineco = var_cineco.get()  # 1 si usa tarjeta, 0 si no

        # Validaciones de límite por personas
        if num_personas == 1 and num_boletos > 7:
            messagebox.showerror("Error", "No puedes comprar más de 7 boletos.")
            return
        elif num_personas == 2 and num_boletos > 14:
            messagebox.showerror("Error", "No puedes comprar más de 14 boletos.")
            return
        elif num_personas >= 3 and num_boletos > 21:
            messagebox.showerror("Error", "No puedes comprar más de 21 boletos.")
            return
        elif num_personas < 1:
            messagebox.showerror("Error", "El número de personas debe ser al menos 1.")
            return

        # Calcular subtotal
        subtotal = num_boletos * boleto

        # Descuento por cantidad de boletos
        if num_boletos > 5:
            descuento = subtotal * 0.15
        elif 3 <= num_boletos <= 5:
            descuento = subtotal * 0.10
        else:
            descuento = 0

        total = subtotal - descuento

        # Descuento adicional por tarjeta CINECO
        if usa_cineco == 1:  # checkbox marcado
            descuento_cineco = total * 0.10
            total -= descuento_cineco
            messagebox.showwarning("Advertencia", 
                "Se aplicó un 10% adicional por pagar con tarjeta CINECO.")
        else:
            descuento_cineco = 0
            messagebox.showinfo("Información", 
                "No se aplicó descuento adicional por tarjeta CINECO.")

        # Mostrar total en el campo de la interfaz
        total_var.set(f"{total:.2f}")

    except ValueError:
        messagebox.showerror("Error", "Debes ingresar valores numéricos válidos.")

# Creación de ventana
ventana = Tk.Tk()
ventana.title("Cinepolis")
ventana.geometry("900x450")

# Fondo
img = Image.open("cinepolis.png")
img = img.resize((900, 450))
imagen = ImageTk.PhotoImage(img)

label_fondo = Tk.Label(ventana, image=imagen)
label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

# Panel izquierdo (datos)
frame_izq = Tk.Frame(ventana, bg="#081A41", bd=5)
frame_izq.pack(side="left", padx=20, pady=20)

Tk.Label(frame_izq, text="Nombre", fg="white", bg="#081A41").grid(row=0, column=0, padx=10, pady=5)
entry_nombre = Tk.Entry(frame_izq)
entry_nombre.grid(row=0, column=1, padx=10, pady=5)

Tk.Label(frame_izq, text="Cantidad de Compradores", fg="white", bg="#081A41").grid(row=1, column=0, padx=10, pady=5)
entry_personas = Tk.Entry(frame_izq)
entry_personas.grid(row=1, column=1, padx=10, pady=5)

Tk.Label(frame_izq, text="Cantidad de Boletos", fg="white", bg="#081A41").grid(row=2, column=0, padx=10, pady=5)
entry_boletos = Tk.Entry(frame_izq)
entry_boletos.grid(row=2, column=1, padx=10, pady=5)

# Checkbox tarjeta CINECO
var_cineco = Tk.IntVar()
Tk.Checkbutton(frame_izq, text="Pago con tarjeta CINECO", fg="white", variable=var_cineco, bg="#081A41").grid(row=3, column=0, columnspan=2, pady=5)

# Panel derecho (total)
frame_der = Tk.Frame(ventana, bg="#081A41", bd=5)
frame_der.pack(side="right", padx=20, pady=20)

Tk.Label(frame_der, text="Total a Pagar", fg="white", bg="#081A41").grid(row=0, column=0, padx=10, pady=5)
total_var = Tk.StringVar()
entry_total = Tk.Entry(frame_der, textvariable=total_var, state="readonly")
entry_total.grid(row=0, column=1, padx=10, pady=5)

# Frame inferior para botones
frame_deba = Tk.Frame(ventana, bg="#081A41", bd=5)
frame_deba.pack(side="bottom", pady=20)

Tk.Button(frame_deba, text="Procesar", command=procesar).grid(row=0, column=0, padx=10, pady=10)
Tk.Button(frame_deba, text="Salir", command=ventana.quit).grid(row=0, column=1, padx=10, pady=10)

ventana.mainloop()