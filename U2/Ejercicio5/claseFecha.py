class Fecha:
    __fecha: str
    __idLoc: int
    __idVis: int
    __golesLoc: int
    __golesVis: int

    def __init__(self, fecha, idLoc, idVis, gL, gV):
        self.__fecha = fecha
        self.__idLoc = int(idLoc)
        self.__idVis = int(idVis)
        self.__golesLoc = int(gL)
        self.__golesVis = int(gV)
    
    def get_fecha(self):
        return self.__fecha

    def get_id_local(self):
        return self.__idLoc

    def get_id_visitante(self):
        return self.__idVis

    def get_goles_local(self):
        return self.__golesLoc

    def get_goles_visitante(self):
        return self.__golesVis
    
