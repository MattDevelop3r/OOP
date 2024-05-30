from coleccion import Coleccion
from menuOpciones import menu

if __name__ == '__main__':
    C = Coleccion()
    C.carga_calefactores()

    opcion = menu()

    while opcion != 0:
        try:
            if opcion == 1:
                C.insertar_calefactor()
            elif opcion == 2:
                C.agregar_calefactor_ingresado()
            elif opcion == 3:
                pos = int(input('Ingrese la posición para mostrar el tipo de calefactor: '))
                C.mostrar_tipo_por_posicion(pos)
            elif opcion == 4:
                C.calefactor_gas_menor_precio()
            elif opcion == 5:
                marca = input('Ingrese la marca del calefactor eléctrico: ')
                C.mostrar_electricos_por_marca(marca)
            elif opcion == 6:
                C.mostrar_en_promocion()
            elif opcion == 7:
                C.almacenar_en_archivo()
            else:      
                print('Opcion invalida! ingrese nuevamente una opcion')           
        except ValueError as e:
            print(e)
        except UnboundLocalError as e:
            print(e)
        opcion = menu()
