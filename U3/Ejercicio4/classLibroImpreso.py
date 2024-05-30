from classPublicacion import Publicacion
class LibroImpreso(Publicacion):
    __nombre_autor: str
    __fecha_edicion: str
    __cant_paginas: int
    __importe_venta: float

    def __init__(self, titulo, categoria, precioBase, nomAutor, fecha, cantP):
        super().__init__(titulo, categoria, precioBase)
        self.__nombre_autor = nomAutor
        self.__fecha_edicion = fecha
        self.__cant_paginas = int(cantP)
        self.__importe_venta = float(self.calcula_importe_venta())

    def calcula_importe_venta(self):
        actual_year = 2024
        xfecha = self.__fecha_edicion.split("/")
        antiguedad = actual_year - int(xfecha[2])
        importeVenta = self.get_precio_base()
        for _ in range(antiguedad):
            importeVenta *= 0.99
        return round(importeVenta, 2)

    def get_nombre_autor(self):
        return self.__nombre_autor
    def get_fecha_edicion(self):
        return self.__fecha_edicion
    def get_cant_paginas(self):
        return self.__cant_paginas       
    def get_importe_venta(self):
        return self.__importe_venta
        