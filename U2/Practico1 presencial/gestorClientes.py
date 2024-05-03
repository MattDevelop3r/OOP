import csv
from claseCliente import *
class GestorClientes:
    __Clientes : list

    def __init__(self):
        self.__Clientes = []
    
    def agregarCliente(self, cl):
        self.__Clientes.append(cl)

    def leeCSV(self):
        archivo = open('ClientesFarmaCiudad.csv')
        reader = csv.reader(archivo, delimiter=';')
        bandera = True
        for fila in reader:
            if bandera:
                bandera = False
            else: 
                nom = fila[0]
                ap = fila[1]
                dni = int(fila[2])
                num = int(fila[3])
                saldo = float(fila[4])
                unCliente = Cliente(nom,ap,dni,num,saldo)
                self.agregarCliente(unCliente)
        print('ClientesFarmaCiudad.csv leido')
        archivo.close()

    def obtieneDatos(self, dni):
        seEncontro = False
        i = 0
        apellido = ''
        nombre = ''
        numeroCuenta = 0
        saldoAnterior = 0
        datos = []
        while i < len(self.__Clientes) and seEncontro == False:
            if dni == self.__Clientes[i].getDNI():
                seEncontro = True
                apellido = self.__Clientes[i].getApellido()
                nombre = self.__Clientes[i].getNombre()
                numeroCuenta = self.__Clientes[i].getNumeroCuenta()
                saldoAnterior = self.__Clientes[i].getSaldoAnterior()
                datos = [apellido, nombre, numeroCuenta, saldoAnterior]
            else: i += 1
        return datos
    def actualizaSaldo(self, dni, saldo):
        seEncontro = False
        i = 0
        while i < len(self.__Clientes) and seEncontro == False:
            if dni == self.__Clientes[i]:
                seEncontro = True
                self.__Clientes[i].actualizarSaldo(saldo)
            else: i += 1

