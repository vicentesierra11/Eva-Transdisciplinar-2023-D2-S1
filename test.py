import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import ImageTk, Image


ventana = tk.Tk()
ventana.geometry('1200x700')
ventana.resizable(False, False)

imagen_fondo = ImageTk.PhotoImage(Image.open("marco.png"))
imagen_fondo1 = Image.open("marco.png")
imagen_fondo1 = imagen_fondo1.resize((1200, 600), Image.ANTIALIAS)
imagen_superpuesta = Image.open("bkg2.jpg")
imagen_superpuesta = imagen_superpuesta.resize((659, 339), Image.ANTIALIAS)
imagen_superpuesta = ImageTk.PhotoImage(imagen_superpuesta)


label_fondo = tk.Label(ventana, image=imagen_fondo)
label_fondo.place(x=0, y=0)


label_superpuesta = tk.Label(ventana, image=imagen_superpuesta, borderwidth=0)
label_superpuesta.place(x=32, y=40)

#####################################################################################
fig, ax = plt.subplots(figsize=(4.38, 3.53))
x = np.array([1, 2, 3, 4])
y = np.array([1, 2, 3, 4])
ax.plot(x, y)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('M.U.R')
ax.grid(True)

lienzo_grafica = FigureCanvasTkAgg(fig, master=ventana)
lienzo_grafica.draw()
lienzo_grafica.get_tk_widget().place(x=730, y=122)  # Ajustar las coordenadas según sea necesario

#Crear 
contenedor_formulas = tk.Frame(ventana, width=400, height=400, bg='grey')
contenedor_formulas.place(x=780, y=530)  # Se asignan las coordenadas

# Se crea una lista donde se almacenan las formulas.
formulas = [
    "Posición (x) = x₀ + v * t",
    "Velocidad (v) = (x - x₀) / t",
    "Tiempo (t) = (x - x₀) / v"
]

# Se itera fila por fila de la lista que contiene las formulas
for formula in formulas:
    etiqueta_formula = tk.Label(contenedor_formulas, text=formula)
    etiqueta_formula.pack()
#######################################################################################


def hacer_clic():
    print("Presionado")

boton = tk.Button(ventana, text="Iniciar", command=hacer_clic, width=53, height=3)
boton.pack()

boton.place(x=153, y=410)




# Ejecutar el bucle principal de la interfaz
ventana.mainloop()
