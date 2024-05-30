def menu():
    try:
        print('---MENU DE OPCIONES---')
        print('1_ Para un ID ladrillo detallar costo y caracteristica del material')
        print('2_ Mostrar para cada ladrillo el costo total de fabricacion del pedido')
        print('3_ Listar Detalles de ladrillos')
        opcion = int(input('* Seleccione una Opcion 1-2-3 (0 para terminar): '))
    except ValueError:
        pass
    return opcion