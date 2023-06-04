import tkinter as tk
from PIL import Image, ImageTk

def fondo():
    canvas.create_image(0, 0, anchor="center", image="bkg2.jpg")

ventana = tk.Tk()
ventana.geometry("1200x800")
ventana.title("Movimiento Rectilineo Uniforme")

screen_width = ventana.winfo_screenwidth()
screen_height = ventana.winfo_screenheight()

canvas = tk.Canvas(ventana, width=screen_width, height=screen_height)
canvas.pack()

def carga_Imagen(sFile):
    image = Image.open(sFile)
    photo = ImageTk.PhotoImage(image)
    return photo

screen_width = ventana.winfo_screenwidth()
screen_height = ventana.winfo_screenheight()
Bkg = carga_Imagen('bkg2.jpg')  # Cargar fondo

fondo()

ventana.mainloop()