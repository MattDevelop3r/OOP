from tkinter import ttk, messagebox, Tk, Canvas, IntVar, PhotoImage
from tkinter import *
import time
import random

class Aplicacion:
    __ventana: object
    __canvas: object
    __boton_verde: object
    __boton_rojo: object
    __boton_amarillo: object
    __boton_azul: object
    __puntaje: object
    __botones_habilitados: bool
    __ancho = 500
    __alto = 700
     #COLORES      VERDE     ROJO      AMARILLO     AZUL
    __colores = ['#00DD00', '#FF0000', '#FFFF00', '#0000FF']
    __secuencia: list
    __indice_actual: int
    __puntaje: IntVar
    __imagen: object

    def __init__(self):
        self.__botones_habilitados = True
        self.__ventana = Tk()
        self.__ventana.geometry(f"{self.__ancho}x{self.__alto}")
        self.__ventana.title("Simon Game - JugateYa")
        self.__ventana.configure(bg='#BBCCDD')
        self.__canvas = Canvas(self.__ventana, width=self.__ancho, height=self.__alto)
        self.__canvas.pack()
        self.__imagen = PhotoImage(file='Ej1/image.png')    
        self.__imagen = self.__imagen.zoom(3, 3)
        self.__canvas.create_image(0, 0, image=self.__imagen, anchor='nw')
        self.__puntaje = IntVar(value=0)
        self.__secuencia = []
        self.__indice_actual = 0
        # Mostrar puntaje
        style = ttk.Style()
        style.configure("Puntaje.TFrame", background="#000000")
        
        self.__frame_puntaje = ttk.Frame(self.__ventana, padding="10 10 10 10", style="Puntaje.TFrame")
        self.__frame_puntaje.grid(row=0, column=0, columnspan=2, sticky="ew")

        self.__frame_puntaje.grid_columnconfigure(0, weight=1)
        self.__frame_puntaje.grid_columnconfigure(1, weight=1)

        self.__puntaje_texto = ttk.Label(self.__frame_puntaje, text="Puntaje", font=('Noto Sans', 16), background='#000000', foreground='#FFFFFF')
        self.__puntaje_texto.grid(row=0, ipadx=100, column=0, sticky="e")

        self.__puntaje_label = ttk.Label(self.__frame_puntaje, textvariable=self.__puntaje, font=('Noto Sans', 16), background='#000000', foreground='#FFFFFF')
        self.__puntaje_label.grid(row=0, ipadx=20, column=1, sticky="w")

        # Declarar botones
        self.__boton_verde = Canvas(self.__ventana, bg=self.__colores[0], width=200, height=200)
        self.__boton_rojo = Canvas(self.__ventana, bg=self.__colores[1], width=200, height=200)
        self.__boton_amarillo = Canvas(self.__ventana, bg=self.__colores[2], width=200, height=200)
        self.__boton_azul = Canvas(self.__ventana, bg=self.__colores[3], width=200, height=200)
        self.__boton_verde.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        self.__boton_rojo.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)
        self.__boton_amarillo.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)
        self.__boton_azul.grid(row=2, column=1, sticky="nsew", padx=10, pady=10)

        self.__boton_verde.bind("<Button-1>", lambda event: self.apretar_boton(self.__colores[0]))
        self.__boton_rojo.bind("<Button-1>", lambda event: self.apretar_boton(self.__colores[1]))
        self.__boton_amarillo.bind("<Button-1>", lambda event: self.apretar_boton(self.__colores[2]))
        self.__boton_azul.bind("<Button-1>", lambda event: self.apretar_boton(self.__colores[3]))

        self.__ventana.grid_rowconfigure(1, weight=1)
        self.__ventana.grid_rowconfigure(2, weight=1)
        self.__ventana.grid_columnconfigure(0, weight=1)
        self.__ventana.grid_columnconfigure(1, weight=1)
        
        #self.agregar_a_secuencia()
    
    def apretar_boton(self, color):
        if color == self.__secuencia[self.__indice_actual] and self.__botones_habilitados:
            self.__indice_actual += 1
            if self.__indice_actual == len(self.__secuencia):
                self.__puntaje.set(self.__puntaje.get() + 1)
                self.__indice_actual = 0
                self.__ventana.after(1000, self.agregar_a_secuencia)
        elif color != self.__secuencia[self.__indice_actual]:
            messagebox.showinfo("GAME OVER", f"Puntaje obtenido: {self.__puntaje.get()}")
            self.__ventana.destroy()

    def agregar_a_secuencia(self):
        self.__secuencia.append(random.choice(self.__colores))
        self.mostrar_secuencia(self.__secuencia)
    
    def mostrar_secuencia(self, secuencia):
        boton: object
        self.__botones_habilitados = False
        for i, color in enumerate(secuencia):
            boton = self.obtener_boton_por_color(color)
            self.__ventana.after(i * 1000, lambda b=boton, c=color: self.cambiar_color(b, c))
        self.__botones_habilitados = True

    def cambiar_color(self, boton, color):
        boton: object
        boton.config(bg='white')
        self.__ventana.after(500, lambda b=boton, c=color: b.config(bg=c))

    def obtener_boton_por_color(self, color):
        boton: object
        if color == '#00FF00':
            boton = self.__boton_verde
        elif color == '#FF0000':
            boton = self.__boton_rojo
        elif color == '#FFFF00':
            boton = self.__boton_amarillo
        elif color == '#0000FF':
            boton = self.__boton_azul
        return boton

    def ejecutar(self):
        self.__ventana.mainloop()
