import csv
from classReserva import Reserva
class GestorReservas:
    __reservas: list

    def __init__(self):
        self.__reservas = []
    
    def agregar_reserva(self, una_reserva):
        self.__reservas.append(una_reserva)
    
    def lee_csv(self):
        with open('Reservas.csv', newline='') as archivo:
            reader = csv.reader(archivo, delimiter=';')
            bandera = True
            for fila in reader:
                if bandera:
                    bandera = False
                else: 
                    numRes = int(fila[0])
                    nom = fila[1]
                    numCab = fila[2]
                    fecha = fila[3]
                    cantH = fila[4]
                    cantD = fila[5]
                    imp = fila[6]
                    una_reserva = Reserva(numRes, nom, numCab, fecha, cantH, cantD, imp)
                    self.agregar_reserva(una_reserva)
        archivo.close()
    
    def esta_reservada(self, numCab):
        bandera = False
        i = 0
        while i < len(self.__reservas) and not bandera:
            if self.__reservas[i].get_numero_cabana() == numCab:
                bandera = True
            i += 1
        return bandera
    
    def emitir_listado(self, gestorCabañas, fechaI):
        i = 0
        print('N° de Cabaña --- Importe Diario --- Cantidad dias --- Seña --- Importe a cobrar')
        while i < len(self.__reservas):
            if fechaI == self.__reservas[i].get_fecha_inicio():
                nro_cab = self.__reservas[i].get_numero_cabana()
                imp_diario = gestorCabañas.buscar_importe_cabaña(nro_cab)
                cant_dias = self.__reservas[i].get_cant_dias()
                imp_sena = self.__reservas[i].get_importe_sena()
                importe_a_cobrar = cant_dias * imp_diario - imp_sena
                print('{} --- {} --- {} --- {} --- {}'.format(nro_cab, imp_diario, cant_dias, imp_sena, importe_a_cobrar))
            i+=1

    def get_reservas(self):
        return self.__reservas