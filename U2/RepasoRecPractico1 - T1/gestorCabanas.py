import numpy as np
import csv
from classCabana import Cabana
class GestorCabanas:
    __cabanas: np.ndarray
    __cantidad: int
    __dimension: int

    def __init__(self):
        self.__cabanas = np.empty(10, dtype=Cabana)
        self.__cantidad = 0
        self.__dimension = 10

    def agregar_cabana(self, una_cabana):

        if self.__cantidad < self.__dimension:
            self.__cabanas[self.__cantidad] = una_cabana
            self.__cantidad += 1

    def lee_csv(self):
        with open('Cabañas.csv', newline='') as archivo:
            reader = csv.reader(archivo, delimiter=';')
            bandera = True
            for fila in reader:
                if bandera:
                    bandera = False
                else: 
                    num = int(fila[0])
                    cantH = int(fila[1])
                    cantCGrande = int(fila[2])
                    cantCChica = int(fila[3])
                    imp = float(fila[4])
                    una_cabana = Cabana(num, cantH, cantCGrande, cantCChica, imp)
                    self.agregar_cabana(una_cabana)
        archivo.close()    

    def escribe_csv(self):
        archivo = open('Pinga.csv', mode='w', newline='')
        writer = csv.writer(archivo, delimiter=';')
        for cabana in self.__cabanas:
            writer.writerow(cabana.convierte_a_tupla())
        archivo.close()

    def mostrar_numeros_cabanas(self, gestorReservas, cantH):
        i = 0
        bandera = True
        while i < len(self.__cabanas):
            if self.__cabanas[i] >= cantH and not gestorReservas.esta_reservada(self.__cabanas[i].get_num()):
                if bandera:
                    print('\n+ Cabañas con capacidad suficiente y sin reservas: ')
                    bandera = False  
                print('++' + 'Cabaña numero: {}'.format(self.__cabanas[i].get_num()))
            i+=1  
        if bandera:
            print('\n- No se encontraron cabañas :(')        

    def buscar_importe_cabaña(self, numC):
        i = 0
        bandera = True
        while i < len(self.__cabanas) and bandera:
            if self.__cabanas[i].get_num() == numC:
                bandera = False
                importe_diario = self.__cabanas[i].get_importe_dia()
            i += 1
        return importe_diario
    
    def get_cabanas(self):
        return self.__cabanas
