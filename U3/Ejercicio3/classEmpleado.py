class Empleado:
    __nombre_apellido: str
    __id_empleado: int
    __puesto: str

    def __init__(self, nya, id, puesto):
        self.__nombre_apellido = nya
        self.__id_empleado = int(id)
        self.__puesto = puesto

    def get_nya(self):
        return self.__nombre_apellido
    def get_id(self):
        return self.__id_empleado
    def get_puesto(self):
        return self.__puesto
    
