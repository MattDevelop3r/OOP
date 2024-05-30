from classPrograma import ProgramaCapacitacion
import csv
class GestorProgramasCapacitacion:
    __lista_programas: list

    def __init__(self):
        self.__lista_programas = []
    
    def agregar_programa(self, programa):
        self.__lista_programas.append(programa)
    
    def carga_programas(self):
        with open('programas_capacitacion.csv', 'r') as archivo:
            reader = csv.reader(archivo, delimiter=',')
            flag = True
            for row in reader:
                if flag:
                    flag = False
                else: 
                    nom, cod, dur = row
                    un_programa = ProgramaCapacitacion(nom, cod, int(dur))
                    self.agregar_programa(un_programa)
        archivo.close()
        print('leido programas_capacitacion.csv')
    
    def obtener_programa(self, id_em):
        i = 0
        flag = False
        programa: ProgramaCapacitacion
        while i < len(self.__lista_programas) and not flag:
            if self.__lista_programas[i].get_codigo() == id_em:
                programa = self.__lista_programas[i]
                flag = True
            i+=1
        assert flag is True
        return programa