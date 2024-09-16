#Construir un programa que muestre una ventana en la cual aparezca su nombre completo y su edad centrados.

from tkinter import *

base = Tk()
miVentana = Frame(base, width=300, height= 300)
miVentana.pack()

miLabel = Label(miVentana, text="Bryan Enrique Torres Alvarez 28 años", )
miLabel.place(x=50, y=50)

base.mainloop()