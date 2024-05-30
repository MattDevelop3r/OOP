import abc
from abc import ABC
import numpy as np
import math
class Cuerpo(ABC):
    __altura: int
    def __init__(self, altura):
        self.__altura=altura
        
    @abc.abstractmethod
    def superficieBase():
        pass 
    def volumen(self):
        return self.superficieBase()*self.__altura
    def getAltura(self):
        return self.__altura