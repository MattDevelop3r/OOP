class GestorMotos: 
    __motos: list

    def __init__(self):
        self.__motos = []
    
    def putMoto(self, Moto):
        self.__motos.append(Moto)
    