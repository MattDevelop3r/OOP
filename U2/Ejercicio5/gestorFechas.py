import csv
from claseFecha import Fecha
class GestorFechas:
    __Fechas: list

    def __init__(self):
        self.__Fechas = []

    def leeFechasCSV(self):
        archivo = open('Ejercicio5\\fechasFutbol.csv')
        reader = csv.reader(archivo, delimiter=',')
        bandera = True
        for row in reader:
            if bandera:
                bandera = False
            else:
                fec = row[0]
                idL = row[1]
                idV = row[2]
                gL = row[3]
                gV = row[4]
                unaFecha = Fecha(fec, idL, idV, gL, gV)
                self.__Fechas.append(unaFecha)
        archivo.close()


        