from class_caja import *
class GestorCajas:
    __contenedor: list
    
    def __init__(self):
        self.__contenedor = []

    def addCaja(self):
        nroCuenta = int(input('Introduce el nro de cuenta: '))
        cuil = input('Introduce el cuil: ')
        apellido = input('introduce el apellido: ')
        nombre = input('introduce el nombre: ')
        saldo = float(input('introduce el saldo: '))

        cuenta = Caja_de_ahorro(nroCuenta, cuil, apellido, nombre, saldo)
        self.__contenedor.append(cuenta)
    
    def obtenerDatos(self, cuil):
        i = 0
        seEncontro = False
        resultado = 0
        while i < len(self.__contenedor) and seEncontro == False:
            if self.__contenedor[i].obtenerCuil() == cuil: 
                seEncontro = True
            else:
                i += 1
        if seEncontro:
            nombre = self.__contenedor[i].obtenerNombre()
            apellido = self.__contenedor[i].obtenerApellido()
            saldo = self.__contenedor[i].obtenerSaldo()
            datos = [nombre, apellido, saldo]
            resultado = datos

        return resultado
            
