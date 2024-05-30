from abc import ABC, abstractmethod

class ColeccionInterface(ABC):
    
    @abstractmethod
    def insertarElemento(self, elemento, posicion):
        pass

    @abstractmethod
    def agregarElemento(self, elemento):
        pass

    @abstractmethod
    def mostrarElemento(self, posicion):
        pass