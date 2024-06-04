import abc
from abc import ABC
class Producto(ABC):
    __nombre: str
    __fecha_envasado: str
    __fecha_vencimiento: str
    __temp_mantenimiento: float
    __pais_origen: str
    __numero_lote: str
    __costo_base: int

    def __init__(self, nombre, fechaE, fechaV, temp, pais, num_lote, costo):
        self.__nombre = nombre
        self.__fecha_envasado = fechaE
        self.__fecha_vencimiento = fechaV
        self.__temp_mantenimiento = float(temp)
        self.__pais_origen = pais
        self.__numero_lote = num_lote
        self.__costo_base = int(costo)
    
    def get_nombre(self):
        return self.__nombre
    def get_fecha_envasado(self):
        return self.__fecha_envasado
    def get_fecha_vencimiento(self):
        return self.__fecha_vencimiento
    def get_temp_mantenimiento(self):
        return self.__temp_mantenimiento
    def get_pais_origen(self):
        return self.__pais_origen
    def get_numero_lote(self):
        return self.__numero_lote
    def get_costo_base(self):
        return self.__costo_base
    
    @abc.abstractmethod
    def getImporteVenta(self):
        pass

    def mostrar_informacion(self):
        print(f"\n   Nombre: {self.__nombre}")
        print(f"   Pais de origen: {self.__pais_origen}")
        print(f"   Temperatura de mantenimiento recomendada: {self.__temp_mantenimiento}")
        print(f"   Importe de venta: {self.getImporteVenta()}")