import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import ImageTk, Image
# Crear la ventana principal con resolución
ventana = tk.Tk()
ventana.geometry('1200x650')
ventana.resizable(False, False)
ventana.title("M.U.R - Movimiento Uniforme rectilineo")

# Cargar las imágenes
imagen_fondo = ImageTk.PhotoImage(Image.open("marco.png"))
imagen_fondo1 = Image.open("marco.png")
imagen_fondo1 = imagen_fondo1.resize((1200, 650), Image.ANTIALIAS)
imagen_superpuesta = Image.open("bkg2.jpg")
imagen_superpuesta = imagen_superpuesta.resize((659, 339), Image.ANTIALIAS)
imagen_superpuesta = ImageTk.PhotoImage(imagen_superpuesta)

# Crear un widget Label con la imagen de fondo
label_fondo = tk.Label(ventana, image=imagen_fondo)
label_fondo.place(x=0, y=0)

# Crear un widget Label con la imagen superpuesta
label_superpuesta = tk.Label(ventana, image=imagen_superpuesta, borderwidth=0)
label_superpuesta.place(x=32, y=40)

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

# Fórmulas del movimiento uniforme rectilíneo
formulas = [
    "Posición  (x) = x₀ + v * t",
    "Velocidad (v) = (x - x₀) / t",
    "Tiempo    (t) = (x - x₀) / v"
]

# Crear un widget Label para cada fórmula
for formula in formulas:
    etiqueta_formula = tk.Label(contenedor_formulas, text=formula)
    etiqueta_formula.pack()

###############################################################################
########################### Carlos part 1 #####################################
###############################################################################

###############################################################################

def cal_velocidad():       
    def calcular_resultado():
        xi = int(entry_xi.get())
        xf = int(entry_xf.get())
        ti = int(entry_ti.get())
        tf = int(entry_tf.get())
        resultado = round((xi - xf) / (ti - tf),2)
        label_resultado.config(text="Resultado: " + str(resultado))

    label_xi = tk.Label(ventana, text="Posición inicial: ", fg="green")
    label_xi.place(x=169, y=500)
    entry_xi = tk.Entry(ventana)
    entry_xi.place(x=191, y=525, width=35)

    operador = tk.Label(ventana, text=" - ", fg="red")
    operador.place(x=305, y=511)

    label_xf = tk.Label(ventana, text="Posición final: ", fg="green")
    label_xf.place(x=357, y=500)
    entry_xf = tk.Entry(ventana)
    entry_xf.place(x=377, y=525, width=35)

    label_ti = tk.Label(ventana, text="Tiempo inicial: ", fg="green")
    label_ti.place(x=169, y=550)
    entry_ti = tk.Entry(ventana)
    entry_ti.place(x=191, y=574, width=35)

    operador = tk.Label(ventana, text=" - ", fg="red")
    operador.place(x=305, y=565)

    label_tf = tk.Label(ventana, text="Tiempo final:", fg="green")
    label_tf.place(x=357, y=550)
    entry_tf = tk.Entry(ventana)
    entry_tf.place(x=377, y=574, width=35)

    botoncal = tk.Button(ventana, text="Calcular", fg="blue", command=calcular_resultado)
    botoncal.place(x=490, y=510)

    label_resultado = tk.Label(ventana, text="-")
    label_resultado.place(x=490, y=549)


def cal_posicion():
    def calcular_resultado():
        xi = int(entry_xi.get())
        v = int(entry_vi.get())
        t = int(entry_ti.get())
        resultado = (v * t) + xi
        label_resultado.config(text="resultado: " + str(resultado))

    label_xi = tk.Label(ventana, text="Posición inicial: ", fg="green")
    label_xi.place(x=168, y=500)
    entry_xi = tk.Entry(ventana)
    entry_xi.place(x=191, y=530, width=35)

    operador = tk.Label(ventana, text=" + ", fg="red")
    operador.place(x=277, y=522)

    label_vi = tk.Label(ventana, text="Velocidad: ", fg="green")
    label_vi.place(x=311, y=500)
    entry_vi = tk.Entry(ventana)
    entry_vi.place(x=325, y=530, width=35)

    operador = tk.Label(ventana, text=" * ", fg="red")
    operador.place(x=405, y=522)

    label_ti = tk.Label(ventana, text="Tiempo : ", fg="green")
    label_ti.place(x=440, y=500)
    entry_ti = tk.Entry(ventana)
    entry_ti.place(x=454, y=530, width=35)

    botoncal = tk.Button(ventana, text="calcular", fg="blue", command=calcular_resultado)
    botoncal.place(x=400, y=570)

    label_resultado = tk.Label(ventana, text="-")
    label_resultado.place(x=475, y=590)


def cal_tiempo():
    def calcular_resultado():
        xi = int(entry_xi.get())
        xf = int(entry_xf.get())
        v = int(entry_v.get())
        resultado = (xi - xf) / v
        label_resultado.config(text="resultado: " + str(resultado))

    label_xi = tk.Label(ventana, text="Posición inicial: ", fg="green")
    label_xi.place(x=168, y=500)
    entry_xi = tk.Entry(ventana)
    entry_xi.place(x=191, y=530, width=35)

    operador = tk.Label(ventana, text=" - ", fg="red")
    operador.place(x=277, y=522)

    label_xf = tk.Label(ventana, text="Posición final: ", fg="green")
    label_xf.place(x=311, y=500)
    entry_xf = tk.Entry(ventana)
    entry_xf.place(x=325, y=530, width=35)

    operador = tk.Label(ventana, text=" / ", fg="red")
    operador.place(x=405, y=522)

    label_v = tk.Label(ventana, text="Velocidad: ", fg="green")
    label_v.place(x=440, y=500)
    entry_v = tk.Entry(ventana)
    entry_v.place(x=454, y=530, width=35)

    botoncal = tk.Button(ventana, text="calcular", fg="blue", command=calcular_resultado)
    botoncal.place(x=400, y=570)

    label_resultado = tk.Label(ventana, text="-")
    label_resultado.place(x=475, y=590)


boton = tk.Button(ventana, text="Velocidad", command= cal_velocidad, width=16, height=3)
boton.pack()
boton.place(x=154, y=411)

boton2 = tk.Button(ventana, text="Posición", command= cal_posicion, width=16, height=3)
boton2.pack()
boton2.place(x=282, y=411)

boton3 = tk.Button(ventana, text="Tiempo", command= cal_tiempo, width=16, height=3)
boton3.pack()
boton3.place(x=410, y=411)

###############################################################################
###############################################################################
###############################################################################

# Ejecutar el bucle principal de la interfaz
ventana.mainloop()
