from classCalefactor import Calefactor

class CalefactorElectrico(Calefactor):
    __potencia_maxima: str

    def __init__(self, marca, modelo, pais, precio, formaPago, cantCuotas, promo, potencia):
        super().__init__(marca, modelo, pais, precio, formaPago, cantCuotas, promo)
        self.__potencia_maxima = potencia

    def get_potencia_maxima(self):
        return self.__potencia_maxima

    def calcular_importe_venta(self):
        importe_base = super().calcular_importe_venta()
        if int(self.get_potencia_maxima.split()[0]) > 1000:
            importe_base *= 1.01
        if self.__forma_pago == 'cuotas':
            importe_base *= 1.30
        return importe_base

    def to_dict(self):
        return {
            'tipo': 'electrico',
            'marca': self.get_marca(),
            'modelo': self.get_modelo(),
            'pais_fabricacion': self.get_pais_fabricacion(),
            'precio_lista': self.get_precio(),
            'forma_pago': self.get_forma_pago(),
            'cantidad_cuotas': self.get_cantidad_cuotas(),
            'promocion': self.get_promocion(),
            'potencia_maxima': self.__potencia_maxima
        }