import csv
import random
from classLadrillo import Ladrillo
class GestorLadrillo:
    __listaLadrillos: list

    def __init__(self):
        self.__listaLadrillos = []

    def agregarLadrillo(self,ladrillo):
        self.__listaLadrillos.append(ladrillo)

    def cargarladrillos(self):
        band=False
        archivo=open("ladrillos.csv")
        reader=csv.reader(archivo,delimiter=";")
        for fila in reader:
            if band is False:
                band=True
            else:
                self.agregarLadrillo(Ladrillo(int(fila[0]),int(fila[1]),float(fila[2]),float(fila[3])))
        archivo.close()
    
    def asignarMateriales(self,GM):
        indicesLadrillos=list(range(len(self.__listaLadrillos))) 
        indicesMateriales=list(range(GM.getTotalMateriales())) 
        for i in range(4): 
            indiceRandomL=random.choice(indicesLadrillos)  
            indiceRandomM=random.choice(indicesMateriales)
            self.__listaLadrillos[indiceRandomL].agregarMaterial(GM.getMaterialPorPosicion(indiceRandomM))
    
    def detallar_datos(self, id_ladrillo):
        i = 0
        band = True
        while i < len(self.__listaLadrillos) and band:
            if self.__listaLadrillos[i].get_id() == id_ladrillo:
                print(f'-costo: {self.__listaLadrillos[i].get_costo()}')
                print('-caracteristicas del material solicitado: ')
                for material in self.__listaLadrillos[i].get_materiales():
                    print(f'   {material.get_carac()}')
                band = False
            i+=1
        assert band is False
    
    def mostrar_costo_ladrillos(self):
        for pos, ladrillo in enumerate(self.__listaLadrillos):
            xcosto_asociado = 0
            for material in ladrillo.get_materiales():
                xcosto_asociado += material.get_costo_adicional()
            costo_total = ladrillo.get_costo() + xcosto_asociado
            print(f'Ladrillo {pos+1}, COSTO TOTAL: {costo_total} ')
    
    def mostrar_detalle_ladrillos(self):
        band = True
        for ladrillo in self.__listaLadrillos:
            xcosto_asociado = 0
            xmateriales = ''
            xid = ladrillo.get_id()
            for material in ladrillo.get_materiales():
                xmateriales += (' ' + material.get_carac())
                xcosto_asociado += material.get_costo_adicional()
            if band: 
                print('N° identificador       Material        Costo asociado') 
                band = False
            if xmateriales != '':
                print(f'      {xid}            {xmateriales}            {xcosto_asociado}')
            else:
                print(f'      {xid}                     ---                           ---')