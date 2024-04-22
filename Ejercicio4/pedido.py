class Pedido:
    __patMoto: str
    __id: int
    __comidas: str
    __tiempoMin: int
    __tiempoReal: int
    __precio: float

    def __init__(self):
        self.__patMoto = ''
        self.__id = 0
        self.__comidas = ''
        self.__tiempoMin = 0
        self.__tiempoReal = 0
        self.__precio = 0
    
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