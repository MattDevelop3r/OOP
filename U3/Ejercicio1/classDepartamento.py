class Departamento:
    __id: int
    __nya_propietario: str
    __numero_piso: int
    __numero_departamento: int
    __cantidad_habitaciones: int
    __cantidad_baths: int
    __superficie_cubierta: float

    def __init__(self, id, nya, numP, numD, cantH, cantB, sup):
        self.__id = id
        self.__nya_propietario = nya
        self.__numero_piso = numP
        self.__numero_departamento = numD
        self.__cantidad_habitaciones = cantH
        self.__cantidad_baths = cantB
        self.__superficie_cubierta = sup
    
    def get_id(self):
        return self.__id
    def get_sup(self):
        return self.__superficie_cubierta
    def get_num_piso(self):
        return self.__numero_piso
    def get_num_dpto(self):
        return self.__numero_departamento
    def get_cant_hab(self):
        return self.__cantidad_habitaciones
    def get_cant_bath(self):
        return self.__cantidad_baths
    def get_nombre_propietarios(self):
        return self.__nya_propietario
