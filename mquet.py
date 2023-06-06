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

def animacion_flecha_MUR():
    # Función para mover la flecha en MUR
    def mover_flecha():
        # Crear el lienzo de dibujo con la imagen superpuesta
        lienzo = tk.Canvas(ventana, width=659, height=339, highlightthickness=0)
        lienzo.place(x=32, y=40)

        # Crear el objeto Turtle para la flecha
        flecha = turtle.RawTurtle(lienzo)
        flecha.shape("arrow")
        flecha.color("red")

        # Definir las coordenadas iniciales de la flecha
        x_inicial = -335  # Coordenada x del borde izquierdo del lienzo
        y_inicial = 0  # Coordenada y del centro del lienzo

        # Definir la velocidad de la flecha
        velocidad = 3

        # Mover la flecha en línea recta
        while True:
            x_inicial += velocidad
            flecha.goto(x_inicial, y_inicial)

            if x_inicial >= 659:  # Detener la animación después de que la flecha haya recorrido toda la imagen
                break

    mover_flecha()


def hacer_clic():
    animacion_flecha_MUR()

boton = tk.Button(ventana, text="Iniciar", command=hacer_clic, width=53, height=3)
boton.pack()
boton.place(x=153, y=410)

# Fórmulas del movimiento uniforme rectilíneo
formulas = [
    "Posición (x) = x₀ + v * t",
    "Velocidad (v) = (x - x₀) / t",
    "Tiempo (t) = (x - x₀) / v"
]

# Crear un widget Label para cada fórmula
for formula in formulas:
    etiqueta_formula = tk.Label(contenedor_formulas, text=formula)
    etiqueta_formula.pack()

# Ejecutar el bucle principal de la interfaz
ventana.mainloop()