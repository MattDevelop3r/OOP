from menuOpciones import *
from gestorClientes import *
from gestorMovimientos import *
if __name__ == '__main__':
    gestorC = GestorClientes()
    gestorM = GestorMovimientos()
    gestorC.leeCSV()
    gestorM.leeCSV()
    bandera = True
    while bandera:
        op = opciones()
        if op == 1:
            datos = []
            dni = int(input('Ingrese el DNI: '))
            datos = gestorC.obtieneDatos(dni)
            print(f'{len(datos)}')
            if len(datos) > 3:
                print('Cliente: {}, {}   Numero de cuenta: {}'.format(datos[0], datos[1], datos[2]))
                print('Saldo Anterior: ${}'.format(datos[3]))
                numCuenta = datos[2]
                saldoAnterior = datos[3]
                saldoPendiente = gestorM.listarMovimientos(numCuenta)
                saldo = saldoAnterior + saldoPendiente
                gestorC.actualizaSaldo(dni, saldo)
                print('Saldo Actualizado: ${}'.format(saldo))
            else:
                print('No se encontro el dni')
        elif op == 2:
            datos = []
            dni = int(input('Ingrese un DNI: '))
            datos = gestorC.obtieneDatos(dni)
            if len(datos) > 3:
                numCuenta = datos[2]
                tuvoMovimientos = gestorM.verificaMovimientos(numCuenta)
                if tuvoMovimientos == False:
                    print('{} {} NO tuvo movimientos: '.format(datos[0], datos[1]))
                else: 
                    print('{} {} si tuvo movimientos'.format(datos[0], datos[1]))
            else: 
                print('No se encontro el dni')
        elif op == 3: 
            gestorM.ordenaMovimientos()
        elif op == 0: 
            bandera = False
        else:
            pass