import csv
from claseFecha import Fecha
class GestorFechas:
    __Fechas: list

    def __init__(self):
        self.__Fechas = []
    
    def addFecha(self, fecha):
        self.__Fechas.append(fecha)
    
    def cargaCSV(self):
        archivo = open('fechasFutbol.csv', 'a')
        writer = csv.writer(archivo, delimiter=',')
        for fecha in self.__Fechas:
            writer.writerow([Fecha.get_fecha, Fecha.get_id_local, Fecha.get_id_visitante, Fecha.get_goles_local, Fecha.get_goles_visitante])
        archivo.close()

    def leeCSV(self):
        archivo = open('fechasFutbol.csv', 'r')
        reader = csv.reader(archivo, delimiter=';')
        for row in reader:
            fec = row[0]
            idL = row[1]
            idV = row[2]
            gL = row[3]
            gV = row[4]
            unaFecha = Fecha(fec, idL, idV, gL, gV)
            self.__Fechas.append(unaFecha)

        archivo.close()