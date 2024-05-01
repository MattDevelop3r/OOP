from class_caja import Caja_de_ahorro
def test():
    cuentas = []
    for i in range (3):
        print('Creando la cuenta nro {}'.format(i+1))
        nroCuenta = int(input('Introduce el nro de cuenta: '))
        cuil = input('Introduce el cuil: ')
        apellido = input('introduce el apellido: ')
        nombre = input('introduce el nombre: ')
        saldo = float(input('introduce el saldo: '))

        cuenta = Caja_de_ahorro(nroCuenta, cuil, apellido, nombre, saldo)
        cuentas.append(cuenta)

        print('Metodos para cuenta nro {}'.format(i+1))
        cuenta.mostrar_datos()
        ext = float(input('Ingrese el importe a extraer: '))
        cuenta.extraer(ext)
        dep = float(input('Ingrese el importe a depositar: '))
        cuenta.depositar(dep)
        if cuenta.validar_CUIL() == True:
            print('El cuil de la cuenta nro {} es valido'.format(i+1))
        else:
            print('El cuil de la cuenta nro {} NO es valido'.format(i+1))




    
