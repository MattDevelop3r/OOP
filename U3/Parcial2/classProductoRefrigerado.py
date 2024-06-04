from classProducto import Producto

class ProductoRefrigerado(Producto):
    __codigo_organismo: str

    def __init__(self, nombre, fechaE, fechaV, temp, pais, num_lote, costo, organismo):
        super().__init__(nombre, fechaE, fechaV, temp, pais, num_lote, costo)
        self.__codigo_organismo = organismo
    
    def get_organismo(self):
        return self.__codigo_organismo
    
    def getImporteVenta(self):
        try: 
            precio_base = self.get_costo_base()
            importe_venta = 0
            mesActual = 5
            anioActual = 2024
            xFechaV = self.get_fecha_vencimiento().split('/')
            mesVencimiento = int(xFechaV[1])
            anioVencimiento = int(xFechaV[0])
            mesesDiferencia = (anioActual * 12 + mesActual) - (anioVencimiento * 12 + mesVencimiento)
            if mesesDiferencia <= 2 and mesesDiferencia > 0:
                importe_venta = precio_base - (precio_base * 0.1)
            elif  mesesDiferencia > 2: 
                importe_venta = precio_base + (precio_base * 0.01)
            else:
                raise AssertionError
        except AssertionError:
            print('Error en la carga de meses')
        finally: 
            return importe_venta



        