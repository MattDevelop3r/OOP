from menuOpciones import menu
from gestorProductos import GestorProductos

if __name__ == '__main__':
    GP = GestorProductos()
    GP.carga_productos_csv()
    op = -1
    try: 
        while op != 0:
            op = menu()
            if op==1:
                GP.agrega_producto_ingresado()
            elif op==2:
                try:
                    posicion = int(input('\n- ingrese la posicion de la que quiere saber el tipo de producto: '))
                    GP.mostrar_tipo_producto(posicion - 1)
                except ValueError:
                    print('Error: Ingrese un número válido para la posición!')
            elif op==3:
                GP.cantidad_cada_tipo()
            elif op==4:
                GP.muestra_datos_lista()
            else:
                print('Opcion Invalida! intente nuevamente')
    except TypeError as e:
        print(e)
    finally:
        print('Saliendo del programa:')
