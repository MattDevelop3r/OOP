import numpy as np
import csv
from claseMovimiento import *
class GestorMovimientos:
    __Movimientos : np.ndarray
    __cantidad: int
    __dimension: int
    __incremento : int
    def __init__(self):
        self.__Movimientos = np.empty([0], dtype=Movimiento)
        self.__cantidad = 0
        self.__dimension = 0
        self.__incremento = 1
    def agregarMovimiento(self, mov):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__Movimientos.resize(self.__dimension)
        self.__Movimientos[self.__cantidad]=mov
        self.__cantidad += 1
    
    def leeCSV(self):
        archivo = open('MovimientosAbril2024.csv')
        reader = csv.reader(archivo, delimiter=';')
        bandera = True
        for fila in reader:
            if bandera:
                bandera = False
            else: 
                num = int(fila[0])
                fecha = fila[1]
                desc = fila[2]
                tipo = fila[3]
                importe = float(fila[4])
                unMovimiento = Movimiento(num,fecha,desc,tipo,importe)
                self.agregarMovimiento(unMovimiento)
        print('MovimientosAbril2024.csv leido')
        archivo.close()

    def listarMovimientos(self, numCuenta): 
        i = 0
        print('Movimientos')
        print('FECHA --- DESCRIPCION --- IMPORTE --- TIPO MOVIMIENTO')
        sumaImportes = 0
        while i < len(self.__Movimientos):
            if numCuenta == self.__Movimientos[i].getNumeroCuenta():
                fecha = self.__Movimientos[i].getFecha()
                desc = self.__Movimientos[i].getDescripcion()
                imp = self.__Movimientos[i].getImporte()
                if self.__Movimientos[i].getTipoMovimiento() == 'C':
                    sumaImportes += imp
                else: sumaImportes -= imp
                tipo = self.__Movimientos[i].getTipoMovimiento()
                print('{} --- {} --- ${} --- {}'.format(fecha,desc,imp,tipo))
            i+=1
        return sumaImportes
    
    def verificaMovimientos(self, numCuenta):
        i = 0
        tuvoMovimientos = False
        while i < len(self.__Movimientos) and tuvoMovimientos == False:
            if numCuenta == self.__Movimientos[i].getNumeroCuenta():
                tuvoMovimientos = True
            else: i+=1
        return tuvoMovimientos
    
    def ordenaMovimientos(self):
        self.__Movimientos.sort()
        print('Movimientos Ordenados')