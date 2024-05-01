class Caja_de_ahorro: 
    __nroCuenta : str
    __cuil : str
    __apellido : str
    __nombre : str
    __saldo : float
    def __init__(self, nroCuenta = '', cuil = '', apellido = '', nombre = '', saldo= 0):
        self.__nroCuenta = nroCuenta
        self.__cuil = cuil
        self.__apellido = apellido
        self.__nombre = nombre
        self.__saldo = saldo

    def obtenerCuil(self):
        return self.__cuil
    def obtenerNombre(self):
        return self.__nombre
    def obtenerApellido(self):
        return self.__apellido
    def obtenerSaldo(self):
        return self.__saldo
        

