import tkinter as tk
from tkinter import messagebox

# Función para leer el nombre y la cédula ingresados
def leer_datos():
    nombre = entry_nombre.get()  # Obtener el nombre completo
    dui = entry_dui.get()  # Obtener el número de cédula
    
    # Validar si los campos están vacíos
    if not nombre or not dui:
        messagebox.showerror("Error", "Por favor, ingrese todos los datos.")
    else:
        # Mostrar los datos ingresados en una ventana emergente
        messagebox.showinfo("Datos Ingresados", f"Nombre: {nombre}\nDUI: {dui}")


ventana3 = tk.Tk()
ventana3.title("Introducir datos persoaneles")
label_nombre = tk.Label(ventana3, text="Ingrese su nombre:")
label_nombre.pack(pady=10)
entry_nombre = tk.Entry(ventana3, width=40)
entry_nombre.pack(pady=10)
label_dui = tk.Label(ventana3, text="Ingrese su número de DUI:")
label_dui.pack(pady=10)
entry_dui = tk.Entry(ventana3, width=40)
entry_dui.pack(pady=10)

ventana3.mainloop()