import tkinter as tk
from tkinter import *   
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import ImageTk, Image
import turtle
# Crear la ventana principal con resolución
ventana = tk.Tk()
ventana.geometry('1200x650')
ventana.resizable(False, False)
ventana.title("M.U.R - Movimiento Uniforme rectilineo")

# ESCONDER
show_velocidad = True
numeroesconder = -1


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
ax.set_xlabel('Tiempo')
ax.set_ylabel('Posición')
ax.set_title('Relación entre Posición y Tiempo')
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
    "Velocidad (v) = (x - x₀) / (t - t₀)",
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

#------------------------------------------------------------------------------
#---------------------------- Interfaz Velocidad ------------------------------
#------------------------------------------------------------------------------

def interfaz_velocidad():
    global label_v_xi,label_v_vp , label_v_operador, label_v_xf, label_v_ti, label_v_operador2, label_v_tf, label_v_resultado
    global entry_v_xi,label_v_vp , entry_v_xf, entry_v_ti, entry_v_tf, boton_v_calcular, numeroesconder

    def esconder_velocidad():
        label_v_xi.place_forget()
        label_v_operador.place_forget()
        label_v_xf.place_forget()
        label_v_ti.place_forget()
        label_v_operador2.place_forget()
        label_v_tf.place_forget()
        label_v_resultado.place_forget()
        entry_v_xi.place_forget()
        entry_v_xf.place_forget()
        entry_v_ti.place_forget()
        entry_v_tf.place_forget()
        label_v_vp.place_forget()
        boton_v_calcular.place_forget()
        boton_limpiar.place_forget()
        ventana.update()

    # //Label (etiquetas)://
        #----1° parte operacion---

    boton_limpiar = tk.Button(ventana, text="Esconder", fg="blue", command=esconder_velocidad)
    boton_limpiar.place(x=180 , y= 600)

    numeroesconder = -1 * numeroesconder
    
    label_v_vp = tk.Label(ventana, text="Calcular velocidad promedio: ", fg="red")
    label_v_xi = tk.Label(ventana, text="Posición Final: ", fg="green")
    label_v_operador = tk.Label(ventana, text=" - ", fg="red")
    label_v_xf = tk.Label(ventana, text="Posición Inicial: ", fg="green")
            #----2° parte operacion---
    label_v_ti = tk.Label(ventana, text="Tiempo Final: ", fg="green")
    label_v_operador2 = tk.Label(ventana, text=" - ", fg="red")
    label_v_tf = tk.Label(ventana, text="Tiempo Inicial:", fg="green")
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
    label_v_vp.place(x=191, y=475, width=170)
            # /Place (boton)/

    boton_v_calcular.place(x=490, y=510)

    
    #if numeroesconder == -1:
    #    esconder_velocidad()

#------------------------------------------------------------------------------
#---------------------------- Interfaz Tiempo ---------------------------------
#------------------------------------------------------------------------------

def interfaz_tiempo():
    global label_t_xi, label_t_operador, label_t_xf, label_t_operador2, label_t_v, label_t_resultado
    global entry_t_xi, entry_t_xf, entry_t_v, boton_t_calcular

    def esconder_tiempo():
        label_t_xi.place_forget()
        label_t_operador.place_forget()
        label_t_xf.place_forget()
        label_t_operador2.place_forget()
        label_t_v.place_forget()
        label_t_resultado.place_forget()
        entry_t_xi.place_forget()
        entry_t_xf.place_forget()
        entry_t_v.place_forget()
        boton_t_calcular.place_forget()
        boton_limpiarT.place_forget()
        ventana.update()

    boton_limpiarT = tk.Button(ventana, text="Esconder", fg="blue", command=esconder_tiempo)
    boton_limpiarT.place(x=400, y=600)

#    entry_v_xi.pack_forget() -- FUNCION PARA OCULTAR
    # //Label (etiquetas)://
        #----1° parte operatoria---

    label_t_xi = tk.Label(ventana, text="Posición final: ", fg="green")
    label_t_operador = tk.Label(ventana, text=" - ", fg="red")
    label_t_xf = tk.Label(ventana, text="Posición inicial: ", fg="green")
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

#------------------------------------------------------------------------------
#---------------------------- Interfaz Tiempo ---------------------------------
#------------------------------------------------------------------------------

def interfaz_posicion():
    global label_p_xi, label_p_operador, label_p_vi, label_p_operador2, label_p_ti, label_p_resultado
    global entry_p_xi, entry_p_vi, entry_p_ti, boton_p_calcular
    
    def esconder_posicion():
        label_p_xi.place_forget()
        label_p_operador.place_forget()
        label_p_vi.place_forget()
        label_p_operador2.place_forget()
        label_p_ti.place_forget()
        label_p_resultado.place_forget()
        entry_p_xi.place_forget()
        entry_p_vi.place_forget()
        entry_p_ti.place_forget()
        boton_p_calcular.place_forget()
        boton_esconderP.place_forget()
        ventana.update()

    boton_esconderP = tk.Button(ventana, text="Esconder", fg="blue", command=esconder_posicion)
    boton_esconderP.place(x=250,y=600)
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


#----------------------------------------------------------------------------
#--------------------- Operatorias ------------------------------------------
#----------------------------------------------------------------------------

def operatoria_velocidad():
    global resultado_v
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

#----------------------------------------------------------------------------------------------
#------------------------------- Botones seleccion operatoria ---------------------------------
#----------------------------------------------------------------------------------------------




# Cargar y redimensionar la imagen
imagen1 = Image.open("boton1.png")
imagen1 = imagen1.resize((123, 53), Image.LANCZOS)
imagen1 = ImageTk.PhotoImage(imagen1)

# Crear el botón con la imagen
boton1 = tk.Button(ventana, image=imagen1, command=lambda: [interfaz_velocidad()])

# Asignar la coordenada al botón
boton1.place(x=154, y=409)

#####################################
imagen2 = Image.open("boton2.png")
imagen2 = imagen2.resize((123, 53), Image.LANCZOS)
imagen2 = ImageTk.PhotoImage(imagen2)

# Crear el botón con la imagen
boton2 = tk.Button(ventana, image=imagen2, command=lambda: [interfaz_posicion()])
boton2.place(x=282, y=409)
#####################################################################
# Asignar la coordenada al botón
imagen3 = Image.open("boton3.png")
imagen3 = imagen3.resize((123, 53), Image.LANCZOS)
imagen3 = ImageTk.PhotoImage(imagen3)

# Crear el botón con la imagen
boton3 = tk.Button(ventana, image=imagen3, command=lambda: [interfaz_tiempo()])
boton3.place(x=410, y=409)

def trazar_grafica():
    v_xi = int(entry_v_xi.get())
    v_xf = int(entry_v_xf.get())
    v_ti = int(entry_v_ti.get())
    v_tf = int(entry_v_tf.get())

    posiciones = [v_xi, v_xf]
    tiempos = [v_ti, v_tf]

    ax.clear()
    ax.plot(tiempos, posiciones, marker='o')
    ax.set_xlabel('Tiempo')
    ax.set_ylabel('Posición')
    ax.set_title('Relación entre Posición y Tiempo')
    ax.grid(True)

    lienzo_grafica.draw()

################################################################################
##########Animacion De Pelota##################################################
################################################################################
def animacion_MUR():
    # Función para mover la pelota en MUR
    def mover_pelota():
        # Crear el lienzo de dibujo con la imagen superpuesta
        lienzo = tk.Canvas(ventana, width=659, height=339, highlightthickness=0)
        lienzo.place(x=32, y=40)

        # Crear el objeto Turtle para la flecha
        pelota = turtle.RawTurtle(lienzo)
        pelota.hideturtle()
        pelota.penup()
        pelota.shape("circle")
        pelota.color("red")
        pelota.setposition(-336, 0)
        pelota.penup()
        pelota.showturtle()

        # Definir las coordenadas iniciales de la flecha
        x_inicial = -335  # Coordenada x del borde izquierdo del lienzo
        y_inicial = 0  # Coordenada y del centro del lienzo

        # Definir los límites de movimiento de la flecha
        limite_izquierdo = -335
        limite_derecho = 324

        # Definir la velocidad de la flecha
        velocidad = resultado_v
        while True:
            # Mover la flecha en línea recta
            x_inicial += velocidad
            pelota.goto(x_inicial, y_inicial)

            # Actualizar el lienzo para mostrar los cambios
            lienzo.update()

            # Verificar si la pelota ha alcanzado el límite derecho
            if x_inicial >= limite_derecho:
                pelota.hideturtle()  # Ocultar la pelota
                x_inicial = limite_izquierdo  # Reiniciar la posición de la flecha
                pelota.goto(x_inicial, y_inicial)  # Mover la flecha a la nueva posición sin dibujar
                pelota.showturtle()  # Mostrar la pelota nuevamente

    mover_pelota()

def hacer_click():
    animacion_MUR()

def botonesxd():
    trazar_grafica()
    hacer_click()
##################################################################################################################################
##################################################################################################################################
##################################################################################################################################

"""# Asociar la función hacer_clic al evento de clic del botón
boton_animacionv = tk.Button(ventana, text="Iniciar animación", command=hacer_clic)
boton_animacionv.pack()"""

# Crear el botón para trazar la gráfica
boton_trazar = tk.Button(ventana, text="Trazar Gráfica", command=botonesxd)
boton_trazar.place(x=600, y=550)

#--- Bucle Ventana ---#
ventana.mainloop()