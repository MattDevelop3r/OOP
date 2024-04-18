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
        if self.__saldo >= extraccion:
            self.__saldo - extraccion
            print("Nuevo Saldo: ", self.__saldo)
            return self.__saldo
        else:
            aux = self.__saldo - 
            print("Saldo Insuficiente!. Falta $",)
    def depositar(self, deposito):
        if deposito > 0:
            self.__saldo += deposito
            print("Nuevo Saldo: ", self.__saldo)
    def validar_CUIL(self, xCUIL):
        cuil_i = xCUIL.split('-')
        if len(cuil_i[0]) != 2:
             return print("ERROR! tipo invalido")
        if len(cuil_i[1]) != 8:
             return print("ERROR! DNI invalido")
        if cuil_i[0] != '20' or cuil_i[0] != '27' or cuil_i[0] != '30':
            return print("ERROR! tipo invalido")
        aux = cuil_i[0] + cuil_i[1]
        acum = 0
        acum += int(aux[0]) * 5
        acum += int(aux[1]) * 4
        acum += int(aux[2]) * 3
        acum += int(aux[3]) * 2
        acum += int(aux[4]) * 7
        acum += int(aux[5]) * 6
        acum += int(aux[6]) * 5
        acum += int(aux[7]) * 4
        acum += int(aux[8]) * 3
        acum += int(aux[9]) * 2
        aux[0]
        return True

