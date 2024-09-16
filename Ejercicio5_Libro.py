import tkinter as tk
from tkinter import messagebox

# Función para leer los datos ingresados
def leer_datos():
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    genero = entry_genero.get()
    direccion = entry_direccion.get()
    telefono = entry_telefono.get()
    correo = entry_correo.get()
    estado_civil = entry_estado_civil.get()
    profesion = entry_profesion.get()
    nacionalidad = entry_nacionalidad.get()
    identificacion = entry_identificacion.get()

    # Validar que todos los campos estén llenos
    if not (nombre and edad and genero and direccion and telefono and correo and estado_civil and profesion and nacionalidad and identificacion):
        messagebox.showerror("Error", "Por favor, ingrese todos los datos.")
    else:
        # Mostrar los datos ingresados en un mensaje emergente
        messagebox.showinfo("Datos Ingresados", f"Nombre: {nombre}\nEdad: {edad}\nGénero: {genero}\n"
                                                f"Dirección: {direccion}\nTeléfono: {telefono}\nCorreo: {correo}\n"
                                                f"Estado Civil: {estado_civil}\nProfesión: {profesion}\n"
                                                f"Nacionalidad: {nacionalidad}\nIdentificación: {identificacion}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Datos Personales")

# Crear etiquetas y campos de entrada para los 10 datos
tk.Label(ventana, text="Nombre Completo:").pack(pady=5)
entry_nombre = tk.Entry(ventana, width=40)
entry_nombre.pack(pady=5)

tk.Label(ventana, text="Edad:").pack(pady=5)
entry_edad = tk.Entry(ventana, width=40)
entry_edad.pack(pady=5)

tk.Label(ventana, text="Género:").pack(pady=5)
entry_genero = tk.Entry(ventana, width=40)
entry_genero.pack(pady=5)

tk.Label(ventana, text="Dirección:").pack(pady=5)
entry_direccion = tk.Entry(ventana, width=40)
entry_direccion.pack(pady=5)

tk.Label(ventana, text="Número de Teléfono:").pack(pady=5)
entry_telefono = tk.Entry(ventana, width=40)
entry_telefono.pack(pady=5)

tk.Label(ventana, text="Correo Electrónico:").pack(pady=5)
entry_correo = tk.Entry(ventana, width=40)
entry_correo.pack(pady=5)

tk.Label(ventana, text="Estado Civil:").pack(pady=5)
entry_estado_civil = tk.Entry(ventana, width=40)
entry_estado_civil.pack(pady=5)

tk.Label(ventana, text="Profesión:").pack(pady=5)
entry_profesion = tk.Entry(ventana, width=40)
entry_profesion.pack(pady=5)

tk.Label(ventana, text="Nacionalidad:").pack(pady=5)
entry_nacionalidad = tk.Entry(ventana, width=40)
entry_nacionalidad.pack(pady=5)

tk.Label(ventana, text="Número de Identificación:").pack(pady=5)
entry_identificacion = tk.Entry(ventana, width=40)
entry_identificacion.pack(pady=5)

# Botón para leer los datos
boton_leer = tk.Button(ventana, text="Leer Datos", command=leer_datos)
boton_leer.pack(pady=20)

# Ejecutar el bucle principal de la ventana
ventana.mainloop()
