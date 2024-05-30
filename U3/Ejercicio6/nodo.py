from classCalefactor import Calefactor
class Nodo:
    __calefactor: Calefactor
    __siguiente: object

    def __init__(self, calefactor):
        self.__calefactor = calefactor
        self.__siguiente = None
    
    def set_siguiente(self, siguiente):
        self.__siguiente = siguiente

    def get_siguiente(self):
        return self.__siguiente
    
    def get_calefactor(self):
        return self.__calefactor