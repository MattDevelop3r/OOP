from gestorCajas import *

if __name__ == '__main__':
    op = input('Quiere Ingresar una caja? SI / NO: ')
    gestor = GestorCajas()
    while op.lower() == 'si':
        gestor.addCaja()
        op = input('Quiere Ingresar una caja? SI / NO: ')
        
    cuil = input('Ingrese el Cuil: ')
    res = gestor.obtenerDatos(cuil)

    if res == 0:
        print('CUIL NO ENCONTRADO')
    else:
        for i in res:
            print(i)