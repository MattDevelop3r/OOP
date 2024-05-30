from classMatricula import Matricula
import csv
class GestorMatriculas:
    __lista_matriculas: list

    def __init__(self):
        self.__lista_matriculas = []
    
    def agregar_matricula(self, matricula):
        self.__lista_matriculas.append(matricula)

    def cargar_matriculas(self, GE, GPC):
        with open('matriculas.csv', 'r') as archivo:
            reader = csv.reader(archivo, delimiter=',')
            flag = True
            for row in reader:
                if flag:
                    flag = False
                else: 
                    fecha = row[0]
                    id_empleado = int(row[1])
                    codigo_programa = row[2]
                    try:
                        empleado = GE.obtener_empleado(id_empleado)
                    except AssertionError:
                        print('No se encontro el empleado asociado a la matricula')
                    try:
                        programa = GPC.obtener_programa(codigo_programa)
                    except AssertionError:
                        print('No se encontro el programa asociado a la matricula')
                    try: 
                        una_matricula = Matricula(fecha, empleado, programa)
                        self.agregar_matricula(una_matricula)
                    except ValueError:
                        print('error en la carga de empleado y/o programa')
                    except: 
                        print('error en la carga de matriculas')
        archivo.close()
        print('leido matriculas.csv')

    def duracion_programas_empleado(self, id_empleado):
        duracion_total = 0
        for matricula in self.__lista_matriculas:
            if matricula.get_empleado().get_id() == id_empleado:
                duracion_total += matricula.get_programa().get_duracion()
        assert duracion_total > 0
        print("Duración total de los programas para el empleado con ID {}: {}".format(id_empleado, duracion_total))

    def empleados_matriculados_programa(self, nombre_programa):
        empleado_encontrado = False
        for matricula in self.__lista_matriculas:
            if matricula.get_programa().get_nombre() == nombre_programa:
                empleado = matricula.get_empleado()
                print("Empleado matriculado en el programa {}: Nombre - {}, ID - {}".format(nombre_programa, empleado.get_nya(), empleado.get_id()))
                empleado_encontrado = True
        assert empleado_encontrado


    def empleados_sin_matricula(self, GE):
        for empleado in GE.get_empleados():
            matriculado = False
            i = 0
            while not matriculado and i < len(self.__lista_matriculas):
                matricula = self.__lista_matriculas[i]
                if matricula.get_empleado().get_id() == empleado.get_id():
                    matriculado = True
                i += 1
            if not matriculado:
                print("Empleado sin matricularse: Nombre - {}, ID - {}".format(empleado.get_nya(), empleado.get_id()))

