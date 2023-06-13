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
imagen_fondo1 = imagen_fondo1.resize((1200, 600), Image.LANCZOS)
imagen_superpuesta = Image.open("bkg2.jpg")
imagen_superpuesta = imagen_superpuesta.resize((659, 339), Image.LANCZOS)
imagen_superpuesta = ImageTk.PhotoImage(imagen_superpuesta)


label_fondo = tk.Label(ventana, image=imagen_fondo)
label_fondo.place(x=0, y=0)


label_superpuesta = tk.Label(ventana, image=imagen_superpuesta, borderwidth=0)
label_superpuesta.place(x=32, y=40)

#####################################################################################
fig, ax = plt.subplots(figsize=(4.35, 3.53)) # Crea  una figura con el comando subplot con la libreria mathplotlib, con un tamaño de 5 x 5
x = np.array([1,2,3,4]) # Se crea un arreglo con la libreria numpy asignada a la variable x 
y = np.array([1,2,3,4]) # Se crea un arreglo con la libreria numpy asignada a la variable y
ax.plot(x, y) # Aqui el plot es utilizado para trazar un linea a travez del grafivo con las cordenadas de los arreglos x e y
ax.set_xlabel('x') # Etiqueta para el eje x
ax.set_ylabel('y') # Etiqueta para el eje y
ax.set_title('M.U.R') # Etiqueta para la grafica 
ax.grid(True) # Grid permite ver la cuadricula en la grafica

lienzo_grafica = FigureCanvasTkAgg(fig, master=ventana) # Se crea un lienzo para mostrar la figura fig en la interfaz principal que seria la 'ventana'
lienzo_grafica.draw() # Se dibuja la figura
lienzo_grafica.get_tk_widget().place(x=730, y=122)  # Se le define unas cordenadas a la figura recien dibujada

#Crea una etiqueta con formulas de ejemplo
contenedor_formulas = tk.Frame(ventana, width=400, height=400, bg='grey') # Crea un marco que contiene un label(etiqueta) para ventana, y le asigna sus medidas
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
    etiqueta_formula.pack() # Acomoda el texto dentro del marco 'contenedor_formulas'

# En cada iteracion se agrega una linea de la lista 'formulas' a 'contenedor_formulas'
#######################################################################################


def hacer_clic():
    print("Presionado")

boton = tk.Button(ventana, text="Iniciar", command=hacer_clic, width=53, height=3)
boton.pack()

boton.place(x=153, y=410)




# Ejecutar el bucle principal de la interfaz
ventana.mainloop()
