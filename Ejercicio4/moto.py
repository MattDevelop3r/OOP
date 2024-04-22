class Moto:
    __patente: str
    __marca: str
    __NyA: str
    __km: int

    def __init__(self):
        self.__patente = ''
        self.__marca = ''
        self.__NyA = ''
        self.__km = 0
    
    def getPatente(self):
        return self.__patente
    def getMarca(self):
        return self.__marca
    def getNyA(self):
        return self.__NyA
    def getKm(self):
        return self.__km