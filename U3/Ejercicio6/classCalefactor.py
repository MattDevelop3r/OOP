class Calefactor:
    __marca: str
    __modelo: str
    __pais_fabricacion: str
    __precio_lista: float
    __forma_pago: str
    __cantidad_cuotas: int
    __promocion: str
    __importe_venta: float

    def __init__(self, marca, modelo, pais, precio, formaPago, cantCuotas, promo):
        self.__marca = marca
        self.__modelo = modelo
        self.__pais_fabricacion = pais
        self.__precio_lista = precio
        self.__forma_pago = formaPago
        self.__cantidad_cuotas = cantCuotas
        self.__promocion = promo
    
    def get_marca(self):
        return self.__marca

    def get_modelo(self):
        return self.__modelo
    
    def get_pais_fabricacion(self):
        return self.__pais_fabricacion

    def get_precio(self):
        return self.__precio_lista

    def get_forma_pago(self):
        return self.__forma_pago

    def get_cantidad_cuotas(self):
        return self.__cantidad_cuotas

    def get_promocion(self):
        return self.__promocion

    def calcular_importe_venta(self):
        if self.__promocion == 'Si':
            return self.__precio_lista * 0.85
        else:
            return self.__precio_lista
    
    def to_dict(self):
        pass