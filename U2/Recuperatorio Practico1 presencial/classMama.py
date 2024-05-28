class Mama:
    __dni: int
    __edad: int
    __apellido_y_nombre: str

    def __init__(self, dni, edad, ayn):
        self.__dni = int(dni)
        self.__edad = int(edad)
        self.__apellido_y_nombre = ayn
    
    def get_dni(self):
        return self.__dni
    def get_edad(self):
        return self.__edad
    def get_ayn(self):
        return self.__apellido_y_nombre