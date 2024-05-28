from classBebe import Bebe
import csv

class GestorNacimientos:
    __listaNacimientos = list

    def __init__(self):
        self.__listaNacimientos = []
    
    def agregar_nacimiento(self, unNacimiento):
        self.__listaNacimientos.append(unNacimiento)
    
    def lee_csv(self):
        archivo = open('Nacimientos.csv', newline='')
        reader = csv.reader(archivo, delimiter=';')
        bandera = True
        for fila in reader:
            if bandera:
                bandera = False
            else: 
                dniMama = int(fila[0])
                tipoParto = fila[1]
                fecha= fila[2] 
                hora= fila[3] 
                peso= fila[4]
                xpeso = float(peso.replace(',', '.'))
                altura= int(fila[5])
                unNacimiento = Bebe(dniMama, tipoParto, fecha, hora, xpeso, altura)
                self.agregar_nacimiento(unNacimiento)
        archivo.close()
        print('archivo Nacimientos.csv leido!')

    def imprime_tipo_parto(self, dniMama):
        i=0
        bandera = True
        while i < len(self.__listaNacimientos) and bandera:
            if self.__listaNacimientos[i].get_dni_mama() == dniMama:
                bandera = False
                print('   Tipo de Parto: {}'.format(self.__listaNacimientos[i].get_tipo_parto()))
            i += 1
        
    def imprime_datos_bebe(self, dniMama):
        i=0
        print('   Peso --- Altura')
        while i < len(self.__listaNacimientos):
            if self.__listaNacimientos[i].get_dni_mama() == dniMama:
                pesobb = self.__listaNacimientos[i].get_peso()
                alturabb = self.__listaNacimientos[i].get_altura()
                print('   {}  ---   {}'.format(pesobb, alturabb))
            i+=1

    def busca_fecha(self, dniMama):
        i = 0
        bandera = True
        fecha = ''
        while i < len(self.__listaNacimientos) and bandera:
            if self.__listaNacimientos[i].get_dni_mama() == dniMama:
                bandera = False
                fecha = self.__listaNacimientos[i].get_fecha_nacimiento()
            i+=1
        return fecha


    def tiene_mas_de_un_parto(self, dniMama, indice):
        i = 0
        bandera = False
        fecha_parto = self.busca_fecha(dniMama)
        while i < len(self.__listaNacimientos):
            if self.__listaNacimientos[indice] == self.__listaNacimientos[i]:
                bandera = True
            i+=1
        return bandera




                

