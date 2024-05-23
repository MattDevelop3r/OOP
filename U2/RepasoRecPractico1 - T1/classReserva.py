class Reserva:
    __numero_reserva: int
    __nombre_reservante: str
    __numero_cabana: int
    __fecha_inicio: str
    __cant_huespedes: int
    __cant_dias: int
    __importe_sena: float

    def __init__(self, numRes, nom, numCab, fecha, cantH, cantD, imp):
        self.__numero_reserva = int(numRes)
        self.__nombre_reservante = nom
        self.__numero_cabana = int(numCab)
        self.__fecha_inicio = fecha
        self.__cant_huespedes = int(cantH)
        self.__cant_dias = int(cantD)
        self.__importe_sena = float(imp)

    def get_numero_reserva(self):
        return self.__numero_reserva
    def get_nombre_reservante(self):
        return self.__nombre_reservante
    def get_numero_cabana(self):
        return self.__numero_cabana
    def get_fecha_inicio(self):
        return self.__fecha_inicio
    def get_cant_huespedes(self):
        return self.__cant_huespedes
    def get_cant_dias(self):
        return self.__cant_dias
    def get_importe_sena(self):
        return self.__importe_sena