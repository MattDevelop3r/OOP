from classPublicacion import Publicacion
class AudioLibro(Publicacion):
    __tiempo_reproduccion: int
    __nombre_narrador: str
    __importe_venta: float

    def __init__(self, titulo, categoria, precioBase, tiempoR, nombreN):
        super().__init__(titulo, categoria, precioBase)
        self.__tiempo_reproduccion = int(tiempoR)
        self.__nombre_narrador = nombreN
        self.__importe_venta = float(self.calcula_importe_venta())

    def calcula_importe_venta(self):
        importeVenta = self.get_precio_base() + self.get_precio_base() * 0.1
        return round(importeVenta, 2)

    def get_importe_venta(self):
        return self.__importe_venta

