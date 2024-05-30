import csv
from classEdificio import Edificio
from classDepartamento import Departamento
class GestorEdificios:
    __edificios: list

    def __init__(self):
        self.__edificios = []

    def agregar_edificio(self, ed):
        self.__edificios.append(ed)

    def leeCSV(self):
        try: 
            archivo = open('Ejercicio1\\EdificioNorte.csv')
            reader = csv.reader(archivo, delimiter=';')
            aux = 0
            for fila in reader:
                if (int(fila[0]) != aux):  # Es un nuevo edificio
                    edificio = Edificio(int(fila[0]), fila[1], fila[2], fila[3], int(fila[4]), int(fila[5]))
                    self.agregar_edificio(edificio)
                    aux = int(fila[0])
                else:  # Es un departamento del edificio actual
                    edificio.agregar_departamento(int(fila[1]), fila[2], int(fila[3]), int(fila[4]), int(fila[5]), int(fila[6]), float(fila[7]))
            
        except FileNotFoundError:
            print('Archivo no encontrado')
        else: 
            print('Archivo EdificioNorte.csv leido')

    def mostrar_propietarios(self, nomE):
        try:
            i = 0
            bandera = True
            while i < len(self.__edificios) and bandera:
                if self.__edificios[i].get_nom() == nomE:
                    print('\n* Propietarios del edificio {}: '.format(nomE))
                    for dpto in self.__edificios[i].get_departamentos():
                        print('{}'.format(dpto.get_nombre_propietarios()))
                    bandera = False
                    print()
                i += 1
            assert bandera == False
        except AssertionError: 
            print('Edificio no encontrado!')
    
    def mostrar_superficie_edif(self, id):
        i = 0
        bandera = True
        sup_total = 0
        try: 
            while i < len(self.__edificios) and bandera:
                if self.__edificios[i].get_id() == id:
                    for dpto in self.__edificios[i].get_departamentos():
                        sup_total += dpto.get_sup()
                    bandera = False
                i += 1
            assert bandera == False
        except AssertionError:
            print('\nNo se encontro el id del edificio')
        else:
            print('\n* La superficie total cubierta por el edificio con id: {} fue: {}m\n'.format(id, sup_total))
    
    def mostrar_superficie_dept(self, propietario):
        encontrado = False
        try:
            for edificio in self.__edificios:
                sup_total_edificio = 0
                sup_total_propietario = 0
                for dpto in edificio.get_departamentos():
                    sup_total_edificio += dpto.get_sup()
                    if dpto.get_nombre_propietarios() == propietario:
                        sup_total_propietario += dpto.get_sup()
                        encontrado = True
                if sup_total_propietario > 0:
                    porcentaje = (sup_total_propietario / sup_total_edificio) * 100
                    nombre_edificio = edificio.get_nom()
                    print(f'El propietario {propietario} tiene una superficie total cubierta de {sup_total_propietario}m², lo que representa el {porcentaje:.2f}% del total de la superficie cubierta del {nombre_edificio}.')
            assert encontrado
        except AssertionError:
            print("No se encontró departamento para ese propietario.")
        

    def contar_dptos(self, num_piso):
        for edificio in self.__edificios:
            contador = 0
            piso_existe = False
            try:
                for dpto in edificio.get_departamentos():
                    if dpto.get_num_piso() == num_piso:
                        piso_existe = True
                        if dpto.get_cant_hab() == 3 and dpto.get_cant_bath() > 1:
                            contador += 1
                nom_ed = edificio.get_nom()
                assert not piso_existe
            except AssertionError:
                print(f'Para el {nom_ed} y el piso {num_piso} hay {contador} departamentos que tienen 3 dormitorios y más de un baño.')
            else: 
                print('El {} no tiene piso {}'.format(nom_ed, num_piso))

                    
