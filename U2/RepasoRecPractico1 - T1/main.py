from gestorCabanas import GestorCabanas
from gestorReservas import GestorReservas
from menuOpciones import menu

if __name__ == '__main__':
    gestorC = GestorCabanas()
    gestorR = GestorReservas()

    gestorC.lee_csv()
    gestorR.lee_csv()
    
    opcion = 10

    while opcion != 0: # Si la opcion es 0 finaliza el programa
        opcion = menu()
        if opcion == 1: # item a)
            cant_huespedes = int(input('\nIngrese la cantidad de huespedes: '))
            gestorC.mostrar_numeros_cabanas(gestorR, cant_huespedes)
        elif opcion == 2: # item b)
            fecha_ingresada = input('\nIngrese una fecha: ')
            gestorR.emitir_listado(gestorC, fecha_ingresada)
        elif opcion == 3:
            gestorC.escribe_csv()
        else: 
            pass
