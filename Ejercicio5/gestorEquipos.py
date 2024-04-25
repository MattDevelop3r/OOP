import csv

class GestorEquipos:
    __Equipos: list

    def __init__(self):
        self.__Equipos = []
    
    def addEquipo(self, equipo):
        self.__Equipos.append(equipo)
    def cargaCSV(self):
        archivo = open('equipos2024.csv', 'a')
        writer = csv.writer(archivo, delimiter=',')
        for equipo in self.__Equipos:
            pass
        archivo.close()
    def leeCSV(self):
        archivo = open('equipos2024.csv', 'r')
        reader = csv.reader(archivo, delimiter=',')
        for row in reader:
            print(', '.join(row))
        archivo.close()
