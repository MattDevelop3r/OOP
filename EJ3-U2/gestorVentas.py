class GestorVentas:
    def __init__(self):
        self.ventas = [[0 for _ in range(7)] for _ in range(5)]

    def ingresar_venta(self, dia, sucursal, importe):
        self.ventas[sucursal][dia] += importe

    def total_facturacion_sucursal(self, sucursal):
        return sum(self.ventas[sucursal])

    def sucursal_mas_facturo_dia(self, dia):
        return self.ventas.index(max(self.ventas, key=lambda x: x[dia]))

    def sucursal_menos_facturacion_semana(self):
        return self.ventas.index(min(self.ventas, key=sum))

    def total_facturado_semana(self):
        return sum(sum(sucursal) for sucursal in self.ventas)