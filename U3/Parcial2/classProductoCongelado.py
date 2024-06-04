from classProducto import Producto

class ProductoCongelado(Producto):
    __porc_nitrogeno: int
    __porc_oxigeno: int
    __porc_diox_carb: int
    __porc_vapor_agua: int
    __metodo_congelacion: str

    def __init__(self, nombre, fechaE, fechaV, temp, pais, num_lote, costo, porcNitrogeno, porcOxigeno, porcDioxido, porcVapor, metodo):
        super().__init__(nombre, fechaE, fechaV, temp, pais, num_lote, costo)
        self.__porc_nitrogeno = porcNitrogeno
        self.__porc_oxigeno = porcOxigeno
        self.__porc_diox_carb = porcDioxido
        self.__porc_vapor_agua = porcVapor
        self.__metodo_congelacion = metodo
    
    def get_porc_nitrogeno(self):
        return self.__porc_nitrogeno
    def get_porc_oxigeno(self): 
        return self.__porc_oxigeno
    def get_porc_diox_carb(self):
        return self.__porc_diox_carb
    def get_porc_vapor_agua(self):
        return self.__porc_vapor_agua
    def get_metodo_congelacion(self):
        return self.__metodo_congelacion

    def getImporteVenta(self):
        precio_base = super().get_costo_base()
        importe_venta = 0
        try:
            if self.__metodo_congelacion == 'mecanico' or self.__metodo_congelacion == 'criogenico':
                importe_venta = precio_base + precio_base * 0.15
            else:
                raise AssertionError
        except AssertionError:
            print('Error en el tipo de metodo de congelacion!')
        finally:
            return importe_venta
    