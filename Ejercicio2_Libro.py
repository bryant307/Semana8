#Contruir un programa que muestre una ventana y que lea una clase secreta sin mostrar los caracteres que la componen

import tkinter as tk
from tkinter import messagebox

ventana1 = tk.Tk()
ventana1.title("Ejercicio #2")

def leer_clave():
    clave = introClave.get()  # Obtiene el texto del campo de entrada
    messagebox.showinfo("Clave Secreta", "La clave fue ingresada correctamente")

labelClave = tk.Label(ventana1, text="Ingrese la clave secreta:")
labelClave.pack(pady=10)
introClave = tk.Entry(ventana1, show="*")
introClave.pack(pady=10)

boton_leer = tk.Button(ventana1, text="Leer Clave", command=leer_clave)
boton_leer.pack(pady=10)

ventana1.mainloop()