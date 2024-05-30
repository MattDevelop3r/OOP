from classProfesor import Profesor
class Nodo:
    __profesor: Profesor
    __siguiente: object
    def __init__(self, profesor):
        self.__profesor=profesor
        self.__siguiente=None

    def setSiguiente(self, siguiente):
        self.__siguiente=siguiente
    def getSiguiente(self):
        return self.__siguiente
    def getDato(self):
        return self.__profesor