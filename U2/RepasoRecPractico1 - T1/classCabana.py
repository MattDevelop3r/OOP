class Cabana:
    __numero: int
    __cant_hab: int
    __cant_cama_grande: int
    __cant_cama_chica: int
    __importe_dia: float

    def __init__(self, num, cantH, cantCGrande, cantCChica, imp):
        self.__numero = int(num)
        self.__cant_hab = int(cantH)
        self.__cant_cama_grande = int(cantCGrande)
        self.__cant_cama_chica = int(cantCChica)
        self.__importe_dia = float(imp)
    
    def __ge__(self, other):
        return ((self.__cant_cama_grande * 2) + self.__cant_cama_chica) >= other

    def convierte_a_tupla(self):
        return (self.__numero, self.__cant_hab, self.__cant_cama_grande, self.__cant_cama_chica, self.__importe_dia)

    def get_num(self):
        return self.__numero
    def get_cant_hab(self):
        return self.__cant_hab
    def get_cant_cama_grande(self):
        return self.__cant_cama_grande
    def get_cant_cama_chica(self):
        return self.__cant_cama_chica
    def get_importe_dia(self):
        return self.__importe_dia

