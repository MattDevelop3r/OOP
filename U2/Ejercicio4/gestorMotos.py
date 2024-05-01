import csv
from claseMoto import Moto
class GestorMotos: 
    __motos: list

    def __init__(self):
        self.__motos = []
    
    def CSVMotoReader(self):
        archivo = open('Ejercicio4\\datosMotos.csv')
        reader = csv.reader(archivo, delimiter=',')
        for fila in reader:
            pat = fila[0]
            marca = fila[1]
            nombre = fila[2]
            apellido = fila[3]
            km = int(fila[4])
            unaMoto = Moto(pat, marca, nombre, apellido, km)
            self.__motos.append(unaMoto)
        archivo.close()
    
    def validarPatente(self, pat):
        seEncontro = False
        i = 0
        while i < len(self.__motos) and seEncontro == False:
            if pat == self.__motos[i].getPatente():
                seEncontro = True
            i+=1
        return seEncontro
    
    def muestraDatos(self, pat):
        i = 0
        seEncontro = False
        while i < len(self.__motos) and seEncontro == False:
            if self.__motos[i].getPatente() == pat:
                seEncontro = True
                print(f"{self.__motos[i].getPatente()}   {self.__motos[i].getMarca()}   {self.__motos[i].getNombre()}   {self.__motos[i].getApellido()}   {self.__motos[i].getKm()}")
            i += 1

    def buscaNyA(self, pat):
        seEncontro = False
        i = 0
        while i< len(self.__motos) and seEncontro == False:
            if self.__motos[i].getPatente() == pat:
                seEncontro = True
                nya = str(self.__motos[i].getNombre()) + " " + str(self.__motos[i].getApellido())
            i += 1
        return nya

