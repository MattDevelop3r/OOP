from menuOpciones import menu
from gestorMamas import GestorMamas
from gestorNacimientos import GestorNacimientos
if __name__ == '__main__':
    gestorM = GestorMamas()
    gestorN = GestorNacimientos()
    
    gestorM.lee_csv()
    gestorN.lee_csv()

    opcion = menu()

    while opcion != 0:
        if opcion == 1:
            dni_mama = int(input('Ingrese el DNI de una mama: '))
            gestorM.mostrar_info(gestorN, dni_mama)
        elif opcion == 2:
            gestorM.mostrar_partos_multiples(gestorN)
        else: 
            pass
        opcion = menu()
