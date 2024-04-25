import datetime
class Fecha:
    __fecha: datetime
    __idLoc: int
    __idVis: int
    __golesLoc: int
    __golesVis: int

    def __init__(self, fecha, idLoc, idVis, gL, gV):
        self.__fecha = fecha
        self.__idLoc = idLoc
        self.__idVis = idVis
        self.__golesLoc = gL
        self.__golesVis = gV
    
