class GestorVentas:
    __ventas : list

    def __init__(self):
        self.__ventas = []
        for i in range(5):
            fila = []
            for j in range(7):
                fila.append(0)
            self.__ventas.append(fila)

    def ingresar_venta(self, dia, sucursal, importe):
        self.__ventas[sucursal][dia] += importe

    def total_facturacion_sucursal(self, sucursal):
        return sum(self.__ventas[sucursal])

    def sucursal_mas_facturo_dia(self, dia):
        max = -1
        for i in range(5):
            if self.__ventas[i][dia] > max:
                max = i
        return max

    def sucursal_menos_facturacion_semana(self):
        min = 10
        for i in range(5):
            if sum(self.__ventas[i]) < min: 
                min = i      
        return min

    def total_facturado_semana(self):
        return sum(sum(sucursal) for sucursal in self.__ventas)