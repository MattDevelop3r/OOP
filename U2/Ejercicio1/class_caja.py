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

    def mostrar_datos(self): 
        print('Numero de cuenta:' ,self.__nroCuenta, '\n Cuil: ' ,self.__cuil, '\n Apellido: '  ,self.__apellido, '\n Nombre: ' ,self.__nombre, '\n Saldo: ' ,self.__saldo)
    
    def extraer(self, extraccion):
        
        if self.__saldo >= extraccion:
            self.__saldo -= extraccion
            print("Nuevo Saldo: ", self.__saldo)
        else:
            aux = self.__saldo - extraccion
            print("Saldo Insuficiente!. Falta ${}".format(aux))
            return aux

    def depositar(self, deposito):
        if deposito > 0:
            self.__saldo += deposito
            print("Nuevo Saldo: ", self.__saldo)

    def validar_CUIL(self):
        cuil_i = self.__cuil.split('-')
        bandera = True
        if len(cuil_i[0]) != 2:
            print("ERROR! tipo invalido")
            bandera = False
        if len(cuil_i[1]) != 8:
            print("ERROR! DNI invalido")
            bandera = False
        if cuil_i[0] != '20' and cuil_i[0] != '27' and cuil_i[0] != '30' and cuil_i[0] != '23':
            print("ERROR! tipo invalido")
            bandera= False
        return bandera
        

