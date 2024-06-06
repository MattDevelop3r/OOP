from tkinter import ttk, messagebox, Tk, Button, IntVar
import random

class Aplicacion:
    __ventana: object
    __boton_rojo: object
    __boton_verde: object
    __boton_azul: object
    __boton_amarillo: object
    __puntaje: object
    __ancho = 500
    __alto = 700
    __colores = ['green', 'red', 'yellow', 'blue']
    __secuencia: list
    __indice_actual: int
    __puntaje: IntVar

    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.geometry(f"{self.__ancho}x{self.__alto}")
        self.__ventana.title("Simon Game - JugateYa")
        self.__ventana.configure(bg='#BBCCDD')

        self.__puntaje = IntVar(value=0)
        self.__secuencia = []
        self.__indice_actual = 0

        # Frame para contener el texto 'Puntaje' y el valor del puntaje
        self.__frame_puntaje = ttk.Frame(self.__ventana, padding="10 10 10 10", style="TFrame")
        self.__frame_puntaje.grid(row=0, column=0, columnspan=2, sticky="ew")
        
        self.__frame_puntaje.grid_columnconfigure(0, weight=1)
        self.__frame_puntaje.grid_columnconfigure(1, weight=1)

        self.__puntaje_texto = ttk.Label(self.__frame_puntaje, text="Puntaje", font=('Noto Sans', 16), background='#FFFFFF', foreground='#000000')
        self.__puntaje_texto.grid(row=0, ipadx=100, column=0, sticky="e")

        self.__puntaje_label = ttk.Label(self.__frame_puntaje, textvariable=self.__puntaje, font=('Noto Sans', 16), background='#FFFFFF', foreground='#000000')
        self.__puntaje_label.grid(row=0, ipadx=20, column=1, sticky="w")

        self.__boton_verde = Button(self.__ventana, command=lambda: self.apretar_boton(self.__colores[0]), bg=self.__colores[0])
        self.__boton_rojo = Button(self.__ventana, command=lambda: self.apretar_boton(self.__colores[1]), bg=self.__colores[1])
        self.__boton_amarillo = Button(self.__ventana, command=lambda: self.apretar_boton(self.__colores[2]), bg=self.__colores[2])
        self.__boton_azul = Button(self.__ventana, command=lambda: self.apretar_boton(self.__colores[3]), bg=self.__colores[3])
        
        self.__boton_verde.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        self.__boton_rojo.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)
        self.__boton_amarillo.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)
        self.__boton_azul.grid(row=2, column=1, sticky="nsew", padx=10, pady=10)

        self.__ventana.grid_rowconfigure(1, weight=1)
        self.__ventana.grid_rowconfigure(2, weight=1)
        self.__ventana.grid_columnconfigure(0, weight=1)
        self.__ventana.grid_columnconfigure(1, weight=1)

        self.jugar_juego()

    def apretar_boton(self, color):
        if color == self.__secuencia[self.__indice_actual]:
            self.__indice_actual += 1
            if self.__indice_actual == len(self.__secuencia):
                self.__puntaje.set(self.__puntaje.get() + 1)
                self.__indice_actual = 0
                self.__ventana.after(1000, self.jugar_juego)
        else:
            messagebox.showinfo("GAME OVER", f"Puntaje obtenido: {self.__puntaje.get()}")
            self.__ventana.destroy()

    def jugar_juego(self):
        self.__secuencia.append(random.choice(self.__colores))
        self.mostrar_secuencia()

    def mostrar_secuencia(self):
        for i, color in enumerate(self.__secuencia):
            self.__ventana.after(i * 1000, lambda c=color: self.cambiar_color_boton(c))
        self.__ventana.after(len(self.__secuencia) * 1000, self.restablecer_botones)

    def cambiar_color_boton(self, color):
        boton = self.obtener_boton_por_color(color)
        boton.config(bg='white')
        self.__ventana.after(500, lambda b=boton, c=color: b.config(bg=c))

    def restablecer_botones(self):
        for color in self.__colores:
            boton = self.obtener_boton_por_color(color)
            boton.config(bg=color)

    def obtener_boton_por_color(self, color):
        if color == 'green':
            return self.__boton_verde
        elif color == 'red':
            return self.__boton_rojo
        elif color == 'yellow':
            return self.__boton_amarillo
        elif color == 'blue':
            return self.__boton_azul

    def ejecutar(self):
        self.__ventana.mainloop()
