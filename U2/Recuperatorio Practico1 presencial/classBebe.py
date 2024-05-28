class Bebe:
    __dni_mama: str
    __tipo_parto: str
    __fecha_nacimiento: str
    __hora_nacimiento: str
    __peso: float
    __altura: float

    def __init__(self, dniMama, tipoParto, fecha, hora, peso, altura):
        self.__dni_mama = int(dniMama)
        self.__tipo_parto = tipoParto
        self.__fecha_nacimiento = fecha
        self.__hora_nacimiento = hora
        self.__peso = float(peso)
        self.__altura = int(altura)

    def __eq__(self, other):
        bandera = False
        if (self.__dni_mama == other.__dni_mama and self.__fecha_nacimiento == other.__fecha_nacimiento):
            bandera = True
        return bandera

    def get_dni_mama(self):
        return self.__dni_mama
    def get_tipo_parto(self):
        return self.__tipo_parto
    def get_fecha_nacimiento(self):
        return self.__fecha_nacimiento
    def get_hora_nacimiento(self):
        return self.__hora_nacimiento
    def get_peso(self):
        return self.__peso
    def get_altura(self):
        return self.__altura