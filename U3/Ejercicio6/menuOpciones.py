def menu():
    try:
        print('---------- MENU DE OPCIONES ----------')
        print('[1] Insertar un calefactor en una posicion determinada.')
        print('[2] Agregar calefactor a la coleccion.')
        print('[3] Mostrar tipo de calefactor para una posicion determinada.')
        print('[4] Mostrar marca, modelo y kilocalorías del calefactor a gas natural de menor precio.')
        print('[5] Dada una marca de calefactor eléctrico, mostrar modelo, potencia y precio de lista de todos los calefactores de esa marca. ')
        print('[6] Mostrar marca, modelo, país de fabricación e importe de venta de todos los calefactores que están en promoción.')
        print('[7] Almacenar los objetos de la colección Lista en el archivo “calefactores.json”. ')
        print('[0] Salir del programa.')
        opcion = int(input('- Seleccione una opcion: '))
    except ValueError:
        pass
    return opcion