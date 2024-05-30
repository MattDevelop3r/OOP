from classCalefactor import Calefactor

class CalefactorGas(Calefactor):
    __matricula: str
    __calorias: str

    def __init__(self, marca, modelo, pais, precio, formaPago, cantCuotas, promo, matricula, calorias):
        super().__init__(marca, modelo, pais, precio, formaPago, cantCuotas, promo)
        self.__matricula = matricula
        self.__calorias = calorias
    
    def get_matricula(self):
        return self.__matricula

    def get_calorias(self):
        return self.__calorias
    
    def calcular_importe_venta(self):
        importe_base = super().calcular_importe_venta()
        if int(self.get_calorias.split('kilocalorias')[0]) > 3000:
            importe_base *= 1.01
        if self.__forma_pago == 'cuotas':
            importe_base *= 1.40
        return importe_base
    
    def to_dict(self):
        return {
            'tipo': 'gas natural',
            'marca': self.get_marca(),
            'modelo': self.get_modelo(),
            'pais_fabricacion': self.get_pais_fabricacion(),
            'precio_lista': self.get_precio(),
            'forma_pago': self.get_forma_pago(),
            'cantidad_cuotas': self.get_cantidad_cuotas(),
            'promocion': self.get_promocion(),
            'matricula': self.__matricula,
            'calorias': self.__calorias
        }