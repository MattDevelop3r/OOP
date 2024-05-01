class Moto:
    __patente: str
    __marca: str
    __nombre: str
    __apellido: str
    __km: int

    def __init__(self, pat, mar, nom, ap, km):
        self.__patente = pat
        self.__marca = mar
        self.__nombre = nom
        self.__apellido = ap
        self.__km = 0
    
    def getPatente(self):
        return self.__patente
    def getMarca(self):
        return self.__marca
    def getNombre(self):
        return self.__nombre
    def getApellido(self):
        return self.__apellido
    def getKm(self):
        return self.__km