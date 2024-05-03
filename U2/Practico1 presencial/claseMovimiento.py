class Movimiento:
    __numero_cuenta : int
    __fecha : str
    __descripcion : str
    __tipo_movimiento : str
    __importe : float

    def __init__(self, num, fecha, desc, tipo, imp):
        self.__numero_cuenta = num
        self.__fecha = fecha
        self.__descripcion = desc
        self.__tipo_movimiento = tipo
        self.__importe = imp

    def __lt__(self, other):
        return self.__numero_cuenta < other.__numero_cuenta
    
    def getNumeroCuenta(self):
        return self.__numero_cuenta
    def getFecha(self):
        return self.__fecha
    def getDescripcion(self):
        return self.__descripcion
    def getTipoMovimiento(self):
        return self.__tipo_movimiento
    def getImporte(self):
        return self.__importe
    
