class caja_de_ahorro: 
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

    def mostrar_datos(self): 
        print('Numero de cuenta:' ,self.__nroCuenta, '\n Cuil: ' ,self.__cuil, '\n Apellido: '  ,self.__apellido, '\n Nombre: ' ,self.__nombre, '\n Saldo: ' ,self.__saldo)
    
    def extraer(self, extraccion):
        aux = self.__saldo
        aux -= extraccion
        if aux >= extraccion:
            self.__saldo - extraccion
            print("Nuevo Saldo: ", self.__saldo)
        else:
            print("Saldo Insuficiente!. Falta $",aux)
    def depositar(self, deposito):
        if deposito > 0:
            self.__saldo += deposito
            print("Nuevo Saldo: ", self.__saldo)
    def validar_CUIL(self, xCUIL):
        cuil_i = xCUIL.split('-')
        cuil_c = self.__cuil.split('-')


