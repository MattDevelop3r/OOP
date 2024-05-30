class ProgramaCapacitacion:
    __nombre: str
    __codigo: str
    __duracion: int

    def __init__(self, nombre, codigo, duracion):
        self.__nombre = nombre
        self.__codigo = codigo
        self.__duracion = int(duracion)
    
    def get_nombre(self):
        return self.__nombre
    def get_codigo(self):
        return self.__codigo
    def get_duracion(self):
        return self.__duracion
