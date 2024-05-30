from classEmpleado import Empleado
import csv
class GestorEmpleados:
    __lista_empleados: list

    def __init__(self):
        self.__lista_empleados = []
    
    def agregar_empleado(self, empleado):
        self.__lista_empleados.append(empleado)
    
    def carga_empleados(self):
        with open('empleados.csv', 'r') as archivo:
            reader = csv.reader(archivo, delimiter=',')
            flag = True
            for row in reader:
                if flag:
                    flag = False
                else: 
                    nya, id_empleado, puesto = row
                    un_empleado = Empleado(nya,int(id_empleado),puesto)
                    self.agregar_empleado(un_empleado)
        archivo.close()
        print('leido empleados.csv')
    
    def obtener_empleado(self, id_em):
        i = 0
        flag = False
        empleado: Empleado
        while i < len(self.__lista_empleados) and not flag:
            if self.__lista_empleados[i].get_id() == id_em:
                empleado = self.__lista_empleados[i]
                flag = True
            i+=1
        assert flag is True
        return empleado
    
    def get_empleados(self):
        return self.__lista_empleados

