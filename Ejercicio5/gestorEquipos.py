import csv
from claseEquipo import Equipo
class GestorEquipos:
    __Equipos: list

    def __init__(self):
        self.__Equipos = []
    
    def addEquipo(self, equipo):
        self.__Equipos.append(equipo)
    def testCargaCSV(self):
        with open('equipos2024.csv', 'a', newline='') as archivo:
            writer = csv.writer(archivo, delimiter=';')
            for equipo in self.__Equipos:
                writer.writerow([equipo.get_id(), equipo.get_nombre(), equipo.get_goles_favor(), equipo.get_goles_contra(), equipo.get_diferencia_goles(), equipo.get_puntos()])
            
        archivo.close()
    def leeCSV(self):
        archivo = open('equipos2024.csv', 'r')
        reader = csv.reader(archivo, delimiter=';')
        for row in reader:
            id = row[0]
            nom = row[1]
            gF = row[2]
            gC = row[3]
            ptos = row[4]
            unEquipo = Equipo(id, nom, gF, gC, ptos)
            self.__Equipos.append(unEquipo)
        archivo.close()
