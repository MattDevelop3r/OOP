class Cliente:
    __nombre : str
    __apellido : str
    __dni : int
    __numero_cuenta : int
    __saldo_anterior : float

    def __init__(self, nom, ap, dni, num, saldo):
        self.__nombre = nom
        self.__apellido = ap
        self.__dni = dni
        self.__numero_cuenta = num
        self.__saldo_anterior = saldo

    def getNombre(self):
        return self.__nombre
    def getApellido(self):
        return self.__apellido
    def getDNI(self):
        return self.__dni
    def getNumeroCuenta(self):
        return self.__numero_cuenta
    def getSaldoAnterior(self):
        return self.__saldo_anterior
    def actualizarSaldo(self, saldo):
        self.__saldo_anterior = saldo
    
