import csv
class GestorFechas:
    __Fechas: list

    def __init__(self):
        self.__Fechas = []
    
    def addFecha(self, fecha):
        self.__Fechas.append(fecha)
    
    def cargaCSV(self):
        archivo = open('fechasFutbol.csv', 'a')
        writer = csv.writer(archivo, delimiter=',')
        writer.writerow(self.__Fechas)
        archivo.close()

    def leeCSV(self):
        archivo = open('fechasFutbol.csv', 'a')
        reader = csv.reader(archivo, delimiter=',')
        for row in reader:
            print(', '.join(row))
        archivo.close()