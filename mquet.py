import tkinter as tk
import numpy as np
import turtle
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import ImageTk, Image

# Crear la ventana principal con resolución
ventana = tk.Tk()
ventana.geometry('1200x700')
ventana.resizable(False, False)

# Cargar las imágenes
imagen_fondo = ImageTk.PhotoImage(Image.open("marco.png"))
imagen_fondo1 = Image.open("marco.png")
imagen_fondo1 = imagen_fondo1.resize((1200, 600), Image.ANTIALIAS)
imagen_superpuesta = Image.open("bkg2.jpg")
imagen_superpuesta = imagen_superpuesta.resize((659, 339), Image.ANTIALIAS)
imagen_superpuesta = ImageTk.PhotoImage(imagen_superpuesta)

# Crear un widget Label con la imagen de fondo
label_fondo = tk.Label(ventana, image=imagen_fondo)
label_fondo.place(x=0, y=0)

# Crear un widget Label con la imagen superpuesta
label_superpuesta = tk.Label(ventana, image=imagen_superpuesta, borderwidth=0)
label_superpuesta.place(x=32, y=40)
ventana.mainloop()

# Crear el lienzo de la gráfica
fig, ax = plt.subplots(figsize=(4.38, 3.53))
x = np.array([1, 2, 3, 4])
y = np.array([1, 2, 3, 4])
ax.plot(x, y)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('M.U.R')
ax.grid(True)

# Crear el widget de lienzo de la gráfica
lienzo_grafica = FigureCanvasTkAgg(fig, master=ventana)
lienzo_grafica.draw()
lienzo_grafica.get_tk_widget().place(x=730, y=122)  # Ajustar las coordenadas según sea necesario

# Crear el contenedor de las fórmulas
contenedor_formulas = tk.Frame(ventana, width=400, height=400, bg='grey')
contenedor_formulas.place(x=780, y=530)  # Ajustar las coordenadas según sea necesario