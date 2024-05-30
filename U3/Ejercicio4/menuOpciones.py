def menu():
    try:
        print('---------- MENU DE OPCIONES ----------')
        print('[1] Agregar Publicacion.')
        print('[2] Dada una posicion de la coleccion, mostrar tipo de publicacion.')
        print('[3] Mostrar cantidad de publicaciones de cada tipo.')
        print('[4] Mostrar Titulo-Categoria-Importe de Venta para toda la coleccion.')
        print('[0] Salir del Programa')
        op = int(input('Seleccione una opcion: '))
    except ValueError:
        pass
    return op