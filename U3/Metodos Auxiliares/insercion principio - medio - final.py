
from nodo import Nodo

class Coleccion:
    __comienzo: Nodo
    __actual: Nodo
    __indice: int
    __tope: int

    def __init__(self):
        self.__comienzo = None
        self.__actual = None
        self.__indice = 0
        self.__tope = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice += 1
            calefactor = self.__actual.get_calefactor()
            self.__actual = self.__actual.get_siguiente()
            return calefactor
        

def agregar_al_principio(self, calefactor):
        nodo = Nodo(calefactor)
        nodo.set_siguiente(self.__comienzo)
        self.__comienzo=nodo
        self.__actual=nodo
        self.__tope+=1

def agregar_al_final(self, calefactor):
    nodo = Nodo(calefactor)
    # Si la lista está vacía, se agrega el primer nodo.
    if self.__comienzo is None:
        self.__comienzo = nodo
        self.__actual = nodo
    else:
        # Si no está vacía, recorre la lista hasta el último nodo.
        aux = self.__comienzo
        while aux.get_siguiente() is not None:
            aux = aux.get_siguiente()
        # Inserta el nuevo nodo al final de la lista.
        aux.set_siguiente(nodo)
    self.__tope += 1

def insertar_en_medio(self):
        calefactor = self.pide_datos()
        nodo = Nodo(calefactor)
        band = True
        while band:
            try: 
                pos = int(input('Ingrese la posicion donde insertar: '))
                if pos <= 0 or pos > self.__tope + 1:
                    raise ValueError
                band = False
            except ValueError:
                print('Posicion invalida, ingrese nuevamente')
        if pos == 1:
            nodo.set_siguiente(self.__comienzo)
            self.__comienzo = nodo
        else:
            aux = self.__comienzo
            for i in range(1, pos - 1):
                aux = aux.get_siguiente()
            nodo.set_siguiente(aux.get_siguiente())
            aux.set_siguiente(nodo)
        self.__tope += 1