class Pedido:
    __patMoto: str
    __id: int
    __comidas: str
    __tiempoMin: int
    __tiempoReal: int
    __precio: float

    def __init__(self, pat, id, com, tMin, tReal, prec):
        self.__patMoto = pat
        self.__id = id
        self.__comidas = com
        self.__tiempoMin = tMin
        self.__tiempoReal = tReal
        self.__precio = prec
    
    def __lt__(self, other):
        return self.__patMoto < other.__patMoto

    def getPatMoto(self):
        return self.__patMoto
    def getID(self):
        return self.__id
    def getComidas(self):
        return self.__comidas
    def getTiempoMin(self):
        return self.__tiempoMin
    def getTiempoReal(self):
        return self.__tiempoReal
    def getPrecio(self):
        return self.__precio
    def modTR(self, t):
        self.__tiempoReal = t