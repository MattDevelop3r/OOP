class Equipo:
    __id: int
    __nombre: str
    __golesFavor: int
    __golesContra: int
    __diferenciaGoles: int
    __puntos: int

    def __init__(self, id = 0, nombre = '', golesF = 0, golesC = 0, puntos =0):
        self.__id = id
        self.__nombre = nombre
        self.__golesFavor = golesF
        self.__golesContra = golesC
        __diferenciaGoles = golesF - golesC
        __puntos = puntos
    
   
        
        
