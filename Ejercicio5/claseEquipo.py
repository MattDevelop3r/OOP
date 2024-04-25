class Equipo:
    __id: int
    __nombre: str
    __golesFavor: int
    __golesContra: int
    __diferenciaGoles: int
    __puntos: int

    def __init__(self, id = 0, nombre = '', golesF = 0, golesC = 0, puntos =0):
        self.__id = int(id)
        self.__nombre = nombre
        self.__golesFavor = int(golesF)
        self.__golesContra = int(golesC)
        self.__diferenciaGoles = int(golesF) - int(golesC)
        self.__puntos = int(puntos)
    
    def get_id(self):
        return self.__id

    def get_nombre(self):
        return self.__nombre

    def get_goles_favor(self):
        return self.__golesFavor

    def get_goles_contra(self):
        return self.__golesContra

    def get_diferencia_goles(self):
        return self.__diferenciaGoles

    def get_puntos(self):
        return self.__puntos

   
        
        
