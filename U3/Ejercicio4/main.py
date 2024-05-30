from classColeccion import Coleccion
from menuOpciones import menu

if __name__ == '__main__':
    C = Coleccion()
    C.carga_libros_impresos()
    C.carga_audiolibros()
    opcion = menu()
    while opcion != 0:
        if opcion == 1:
            C.lee_datos_carga()
        elif opcion == 2:
            try:
                pos = int(input('Ingrese la posicion de la lista: '))
                C.mostrar_tipo_publicacion(pos-1)
            except ValueError:
                print('Error: Debe ingresar un numero entero.')
            except IndexError as e:
                print(e)
            except Exception as e:
                print(f'Error inesperado: {e}')
        elif opcion == 3:
            C.cantidad_cada_tipo()
        elif opcion == 4:
            C.mostrar_datos()
        else:
            print('Ingrese una opcion valida!')
        opcion = menu()