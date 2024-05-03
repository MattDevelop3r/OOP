import csv
from claseEquipo import Equipo
class GestorEquipos:
    __Equipos: list

    def __init__(self):
        self.__Equipos = []
    
    def leeEquiposCSV(self):
        archivo = open('Ejercicio5\\equipos2024.csv')
        reader = csv.reader(archivo, delimiter=',')
        bandera = True
        for row in reader:
            if bandera:
                bandera = False
            else: 
                id = row[0]
                nom = row[1]
                gF = row[2]
                gC = row[3]
                ptos = row[4]
                unEquipo = Equipo(id, nom, gF, gC, ptos)
                self.__Equipos.append(unEquipo)
        archivo.close()
    
    def listarEquipo(self, nom):
        print('Equipo --- GOLES A FAVOR --- GOLES EN CONTRA --- DIFERENCIA DE GOLES --- PUNTOS')
        for equipo in self.__Equipos:
            if equipo.get_nombre() == nom:
                print(f'{nom} --- {equipo.get_goles_favor()} --- {equipo.get_goles_contra()} --- {abs(equipo.get_goles_favor() - equipo.get_goles_contra())} --- {equipo.get_puntos()} ')
    
    def ordenaLista(self):
        self.__Equipos.sort()
    
    def cargaCSV(self):
        archivo = open('Ejercicio5\\tabla.csv', 'w', newline = '')
        writer = csv.writer(archivo, delimiter=',')
        writer.writerow(['Equipo', 'ID', 'Goles a Favor', 'Goles en Contra', 'Diferencia de Goles', 'Puntos'])
        for equipo in self.__Equipos:
            writer.writerow([equipo.get_nombre(), equipo.get_id(), equipo.get_goles_favor(), equipo.get_goles_contra(), equipo.get_diferencia_goles(), equipo.get_puntos()])
        archivo.close()   
