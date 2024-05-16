from classDepartamento import *
class Edificio:
    __id: int
    __nombre: str
    __direccion: str
    __nom_empresa_constructora: str
    __cant_pisos: int
    __cant_deptos: int
    __lista_departamentos: list

    def __init__(self, id, nom, dir, nomEC, cantp, cantd):
        self.__id = id
        self.__nombre = nom 
        self.__direccion = dir
        self.__nom_empresa_constructora = nomEC 
        self.__cant_pisos = cantp 
        self.__cant_deptos = cantd
        self.__lista_departamentos = []
    
    def get_id(self):
        return self.__id
    def get_nom(self):
        return self.__nombre
    def get_departamentos(self):
        return self.__lista_departamentos

    def agregar_departamento(self, id, nya, numP, numD, cantH, cantB, sup):
        dpto = Departamento(id, nya, numP, numD, cantH, cantB, sup)  # Creación del Departamento dentro del Edificio (COMPOSICION)
        self.__lista_departamentos.append(dpto)
