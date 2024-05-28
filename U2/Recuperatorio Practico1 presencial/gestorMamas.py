import numpy as np
import csv
from classMama import Mama
class GestorMamas:
    __listaMamas: np.ndarray
    __cantidad: int
    __dimension: int
    __incremento: int
    def __init__(self):
        self.__listaMamas = np.empty(0, dtype=Mama)
        self.__cantidad = 0
        self.__dimension = 0
        self.__incremento = 1
    def agregar_mama(self, unaMama):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__listaMamas.resize(self.__dimension)
        self.__listaMamas[self.__cantidad] = unaMama
        self.__cantidad += 1
    
    def lee_csv(self):
        archivo = open('Mamas.csv', newline='')
        reader = csv.reader(archivo, delimiter=';')
        bandera = True
        for fila in reader:
            if bandera:
                bandera = False
            else: 
                dni = int(fila[0])
                edad = int(fila[1])
                ayn = fila[2]
                unaMama = Mama(dni,edad,ayn)
                self.agregar_mama(unaMama)
        archivo.close()
        print('archivo Mamas.csv leido!')
    
    def mostrar_info(self, gestorNacimientos, dniMama):
        i = 0
        bandera = True
        while i < len(self.__listaMamas) and bandera:
            if self.__listaMamas[i].get_dni() == dniMama:
                print('\n   Apellido y Nombre: {}'.format(self.__listaMamas[i].get_ayn()))
                print('   Edad: {}'.format(self.__listaMamas[i].get_edad()))
                gestorNacimientos.imprime_tipo_parto(dniMama)
                gestorNacimientos.imprime_datos_bebe(dniMama)
            i += 1
    
    def mostrar_partos_multiples(self, gestorNacimientos):
        i=0
        for mama in self.__listaMamas:
            dni = mama.get_dni()
            if gestorNacimientos.tiene_mas_de_un_parto(dni, i):
                ayn = mama.get_ayn()
                edad = mama.get_edad()
                print('\nLa mama con apellido y nombre {}, DNI: {}, edad: {} tuvo mas de un parto'.format(ayn, dni, edad))
            i+=1    
