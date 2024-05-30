from classPublicacion import Publicacion
class Nodo:
    __publicacion: Publicacion
    __siguiente: object

    def __init__(self, publicacion):
        self.__publicacion = publicacion
        self.__siguiente = None

    def set_siguiente(self, siguiente):
        self.__siguiente =  siguiente
    def get_publicacion(self):
        return self.__publicacion
    def get_siguiente(self):
        return self.__siguiente