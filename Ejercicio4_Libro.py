import tkinter as tk
from tkinter import messagebox

# Función para leer los datos ingresados de las 3 mascotas
def leer_datos():
    mascota1 = f"Nombre: {entry_nombre1.get()}, Edad: {entry_edad1.get()}, Tipo: {entry_tipo1.get()}"
    mascota2 = f"Nombre: {entry_nombre2.get()}, Edad: {entry_edad2.get()}, Tipo: {entry_tipo2.get()}"
    mascota3 = f"Nombre: {entry_nombre3.get()}, Edad: {entry_edad3.get()}, Tipo: {entry_tipo3.get()}"

    # Validar si se ingresaron todos los datos para las tres mascotas
    if not entry_nombre1.get() or not entry_edad1.get() or not entry_tipo1.get() or \
       not entry_nombre2.get() or not entry_edad2.get() or not entry_tipo2.get() or \
       not entry_nombre3.get() or not entry_edad3.get() or not entry_tipo3.get():
        messagebox.showerror("Error", "Por favor, ingrese todos los datos de las 3 mascotas.")
    else:
        # Mostrar los datos ingresados de las mascotas
        messagebox.showinfo("Datos de las Mascotas", f"Mascota 1: {mascota1}\nMascota 2: {mascota2}\nMascota 3: {mascota3}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Datos de Mascotas")

# Etiqueta para la mascota 1
label_mascota1 = tk.Label(ventana, text="Datos de la Mascota 1:")
label_mascota1.pack(pady=5)

# Campos de entrada para la mascota 1
entry_nombre1 = tk.Entry(ventana, width=30)
entry_nombre1.pack(pady=5)
entry_nombre1.insert(0, "Nombre de la mascota 1")

entry_edad1 = tk.Entry(ventana, width=30)
entry_edad1.pack(pady=5)
entry_edad1.insert(0, "Edad de la mascota 1")

entry_tipo1 = tk.Entry(ventana, width=30)
entry_tipo1.pack(pady=5)
entry_tipo1.insert(0, "Tipo de la mascota 1")

# Etiqueta para la mascota 2
label_mascota2 = tk.Label(ventana, text="Datos de la Mascota 2:")
label_mascota2.pack(pady=5)

# Campos de entrada para la mascota 2
entry_nombre2 = tk.Entry(ventana, width=30)
entry_nombre2.pack(pady=5)
entry_nombre2.insert(0, "Nombre de la mascota 2")

entry_edad2 = tk.Entry(ventana, width=30)
entry_edad2.pack(pady=5)
entry_edad2.insert(0, "Edad de la mascota 2")

entry_tipo2 = tk.Entry(ventana, width=30)
entry_tipo2.pack(pady=5)
entry_tipo2.insert(0, "Tipo de la mascota 2")

# Etiqueta para la mascota 3
label_mascota3 = tk.Label(ventana, text="Datos de la Mascota 3:")
label_mascota3.pack(pady=5)


entry_nombre3 = tk.Entry(ventana, width=30)
entry_nombre3.pack(pady=5)
entry_nombre3.insert(0, "Nombre de la mascota 3")

entry_edad3 = tk.Entry(ventana, width=30)
entry_edad3.pack(pady=5)
entry_edad3.insert(0, "Edad de la mascota 3")

entry_tipo3 = tk.Entry(ventana, width=30)
entry_tipo3.pack(pady=5)
entry_tipo3.insert(0, "Tipo de la mascota 3")
boton_leer = tk.Button(ventana, text="Leer Datos de las Mascotas", command=leer_datos)
boton_leer.pack(pady=20)


ventana.mainloop()
