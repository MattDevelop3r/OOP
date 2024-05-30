from classInterface import ColeccionInterface
class Coleccion(ColeccionInterface):
    __elementos: list
    def __init__(self):
        self.__elementos = []

    def insertarElemento(self, elemento, posicion):
        try:
            self.__elementos.insert(posicion, elemento)
        except IndexError:
            raise ValueError("\nLa posición no es válida")

    def agregarElemento(self, elemento):
        self.__elementos.append(elemento)

    def mostrarElemento(self, posicion):
        try:
            if posicion < 0:
                raise IndexError("\nLa posición no es válida")
            print("\nElemento en la posición {}: {}".format(posicion + 1, self.__elementos[posicion]))
        except IndexError:
            raise IndexError("\nLa posición no es válida")