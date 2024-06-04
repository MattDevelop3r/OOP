def menu():
    try: 
        print('\n----- Menu de Opciones -----')
        print('[1]_ Agregar productos al gestor de productos.')
        print('[2]_ Mostrar tipo de producto dada una posicion.')
        print('[3]_ Mostrar la cantidad de productos de cada tipo.')
        print('[4]_ Mostrar datos para todos los productos.')
        print('[0]_ Salir del programa')
        opcion = int(input('Seleccione una opcion: '))
    except ValueError:
        pass
    else:
        return opcion