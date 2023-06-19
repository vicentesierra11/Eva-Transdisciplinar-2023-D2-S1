import tkinter as tk, turtle
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
imagen_fondo1 = imagen_fondo1.resize((1200, 650), Image.LANCZOS)
imagen_superpuesta = Image.open("bkg2.jpg")
imagen_superpuesta = imagen_superpuesta.resize((659, 339), Image.LANCZOS)
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

# Botones seleccion operatoria
boton1 = tk.Button(ventana, text="Velocidad", command=lambda: [interfaz_velocidad()], width=16, height=3)
boton1.pack()
boton1.place(x=154, y=411)

boton2 = tk.Button(ventana, text="Posición", command=lambda: [interfaz_posicion()], width=16, height=3)
boton2.pack()
boton2.place(x=282, y=411)

boton3 = tk.Button(ventana, text="Tiempo", command=lambda: [interfaz_tiempo()], width=16, height=3)
boton3.pack()
boton3.place(x=410, y=411)

# interfaces
def interfaz_velocidad():
    global label_v_xi, label_v_operador, label_v_xf, label_v_ti, label_v_operador2, label_v_tf, label_v_resultado
    global entry_v_xi, entry_v_xf, entry_v_ti, entry_v_tf, boton_v_calcular
    # //Label (etiquetas)://
        #----1° parte operacion---
    label_v_xi = tk.Label(ventana, text="Posición final: ", fg="green")
    label_v_operador = tk.Label(ventana, text=" - ", fg="red")
    label_v_xf = tk.Label(ventana, text="Posición inicial: ", fg="green")
        #----2° parte operacion---
    label_v_ti = tk.Label(ventana, text="Tiempo final: ", fg="green")
    label_v_operador2 = tk.Label(ventana, text=" - ", fg="red")
    label_v_tf = tk.Label(ventana, text="Tiempo inicial:", fg="green")
        #----resultado-----------
    label_v_resultado = tk.Label(ventana, text="-")

    # //Entry (campos de entrada):// 
        #----1° parte operacion---
    entry_v_xi = tk.Entry(ventana)
    entry_v_xf = tk.Entry(ventana)
        #----2° parte operacion---
    entry_v_ti = tk.Entry(ventana)
    entry_v_tf = tk.Entry(ventana)

    # //Boton //
    boton_v_calcular = tk.Button(ventana, text="Calcular", fg="blue", command=operatoria_velocidad)

    # //Places (cordenadas: (x,y))://
        # /Places (etiquetas)/
        #---- 1° parte operacion----
    label_v_xi.place(x=169, y=500)
    label_v_operador.place(x=305, y=511)
    label_v_xf.place(x=357, y=500)
        #-----2° parte operacion---
    label_v_ti.place(x=169, y=550)
    label_v_operador2.place(x=305, y=565)
    label_v_tf.place(x=357, y=550)
        #-------reultado-----------
    label_v_resultado.place(x=490, y=549)

        # /Places (campos de entradas)/
    entry_v_xi.place(x=191, y=525, width=35)
    entry_v_xf.place(x=377, y=525, width=35)
        #------------------------
    entry_v_ti.place(x=191, y=574, width=35)
    entry_v_tf.place(x=377, y=574, width=35)

        # /Place (boton)/
    boton_v_calcular.place(x=490, y=510)

def interfaz_tiempo():
    global label_t_xi, label_t_operador, label_t_xf, label_t_operador2, label_t_v, label_t_resultado
    global entry_t_xi, entry_t_xf, entry_t_v, boton_t_calcular

    entry_v_xi.pack_forget()
    # //Label (etiquetas)://
        #----1° parte operatoria---
    label_t_xi = tk.Label(ventana, text="Posición inicial: ", fg="green")
    label_t_operador = tk.Label(ventana, text=" - ", fg="red")
    label_t_xf = tk.Label(ventana, text="Posición final: ", fg="green")
        #----2° parte operatoria----
    label_t_operador2 = tk.Label(ventana, text=" / ", fg="red")
    label_t_v = tk.Label(ventana, text="Velocidad: ", fg="green")
        #-------resultado--- 
    label_t_resultado = tk.Label(ventana, text="-")
    
    # // Entry (campos de entrada)//
        #---- 1° parte operatoria---
    entry_t_xi = tk.Entry(ventana)
    entry_t_xf = tk.Entry(ventana)
        #-----2° parte operatoria---
    entry_t_v = tk.Entry(ventana)
    
    # //Boton//
    boton_t_calcular = tk.Button(ventana, text="calcular", fg="blue", command=operatoria_tiempo)
    
    # //Places (coordenadas: (x,y))//
        # /places (etiquetas)/
        #---1° parte operatoria----
    label_t_xi.place(x=168, y=500)
    label_t_operador.place(x=277, y=522)
    label_t_xf.place(x=311, y=500)
        #---2° parte operatoria---
    label_t_operador2.place(x=405, y=522)
    label_t_v.place(x=440, y=500)
        #------resultado-----
    label_t_resultado.place(x=475, y=590)
    
        # /places (campos de entrada)/
        #---- 1° parte operatoria----
    entry_t_xi.place(x=191, y=530, width=35)
    entry_t_xf.place(x=325, y=530, width=35)
        #-----2° parte operatoria----
    entry_t_v.place(x=454, y=530, width=35)
    
        # /place (boton)/
    boton_t_calcular.place(x=400, y=570)

def interfaz_posicion():
    global label_p_xi, label_p_operador, label_p_vi, label_p_operador2, label_p_ti, label_p_resultado
    global entry_p_xi, entry_p_vi, entry_p_ti, boton_p_calcular
    
    # //Label (etiquetas)//
        #----1° parte operatoria---
    label_p_xi = tk.Label(ventana, text="Posición inicial: ", fg="green")
    label_p_operador = tk.Label(ventana, text=" + ", fg="red")
    label_p_vi = tk.Label(ventana, text="Velocidad: ", fg="green")
        #----2° parte operatoria---
    label_p_operador2 = tk.Label(ventana, text=" * ", fg="red")
    label_p_ti = tk.Label(ventana, text="Tiempo : ", fg="green")
        #-----resultado-----
    label_p_resultado = tk.Label(ventana, text="-")
    
    # //Entry (campos de entrada)///
        #---1° parte operatoria---
    entry_p_xi = tk.Entry(ventana)
    entry_p_vi = tk.Entry(ventana)
        #---2° parte operatoria---
    entry_p_ti = tk.Entry(ventana)
    
    # //Boton//
    boton_p_calcular = tk.Button(ventana, text="calcular", fg="blue", command=operatoria_posicion)
    
    # //Places (cordenadas(x,y))//
        # /places (etiquetas)/
        #---1° parte operatoria---
    label_p_xi.place(x=168, y=500)
    label_p_operador.place(x=277, y=522)
    label_p_vi.place(x=311, y=500)
        #---2° parte operatoria---
    label_p_operador2.place(x=405, y=522)
    label_p_ti.place(x=440, y=500)
        #------resultado-------
    label_p_resultado.place(x=475, y=590)
    
        # /places (campos de entrada)/
        #---1° parte operatoria----
    entry_p_xi.place(x=191, y=530, width=35)
    entry_p_vi.place(x=325, y=530, width=35)
        #---2° parte operatoria----
    entry_p_ti.place(x=454, y=530, width=35)
    
        # /places (boton)/
    boton_p_calcular.place(x=400, y=570)

# operatorias matematicas
def operatoria_velocidad():
    v_xi = int(entry_v_xi.get())
    v_xf = int(entry_v_xf.get())
    #-------------------------------
    v_ti = int(entry_v_ti.get())
    v_tf = int(entry_v_tf.get())
    #-------------------------------
    resultado_v = round((v_xi - v_xf) / (v_ti - v_tf),2)
    label_v_resultado.config(text="Resultado: " + str(resultado_v))

def operatoria_tiempo():
    t_xi = int(entry_t_xi.get())
    t_xf = int(entry_t_xf.get())
    t_v = int(entry_t_v.get())
    resultado_t = (t_xi - t_xf) / t_v
    label_t_resultado.config(text="resultado: " + str(resultado_t))

def operatoria_posicion():
    p_xi = int(entry_p_xi.get())
    p_v = int(entry_p_vi.get())
    p_t = int(entry_p_ti.get())
    resultado_p = (p_v * p_t) + p_xi
    label_p_resultado.config(text="resultado: " + str(resultado_p))

###############################################################################
###############################################################################
###############################################################################

def animacion_flecha_MUR():
    # Función para mover la flecha en MUR
    def mover_flecha():
        # Crear el lienzo de dibujo con la imagen superpuesta
        lienzo = tk.Canvas(ventana, width=658, height=339, highlightthickness=0)
        lienzo.place(x=32, y=40)

        # Crear el objeto Turtle para la flecha
        flecha = turtle.RawTurtle(lienzo)
        flecha.shape("arrow")
        flecha.color("blue")

        # Definir las coordenadas iniciales de la flecha
        x_inicial = -335  # Coordenada x del borde izquierdo del lienzo
        y_inicial = 0  # Coordenada y del centro del lienzo

        # Definir los límites de movimiento de la flecha
        limite_izquierdo = -335
        limite_derecho = 324
        # Definir la velocidad de la flecha
        velocidad = 3

        # Mover la flecha en línea recta
        while True:
            # Mover la flecha en línea recta
            x_inicial += velocidad
            flecha.goto(x_inicial, y_inicial)

            # Verificar si la flecha ha alcanzado los límites de movimiento
            if x_inicial >= limite_derecho or x_inicial <= limite_izquierdo:
                velocidad *= -1  # Invertir la dirección de movimiento

            # Actualizar el lienzo para mostrar los cambios
            lienzo.update()

    mover_flecha()


def hacer_clic():
    animacion_flecha_MUR()

boton = tk.Button(ventana, text="Iniciar", command=hacer_clic)
boton.pack()
boton.place(x=315, y=470)

# Ejecutar el bucle principal de la interfaz
ventana.mainloop()