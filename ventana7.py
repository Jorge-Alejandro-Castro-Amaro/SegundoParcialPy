import tkinter as tk 
from tkinter import messagebox
from PIL import Image, ImageTk

'''
instalar pip install pillow
from PIL Image, ImageTk
'''

root = tk.Tk()
root.title("Cerrar con confirmacion")
root.geometry("500x400")
def cerrar():
    respuesta = messagebox.askyeso("Salir", "Desea cerrar la aplicacion")
    