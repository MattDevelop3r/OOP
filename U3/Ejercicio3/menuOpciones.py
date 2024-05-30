def menu():
    try:
        print('-------      Menu de Opciones     -------')
        print('[1] Mostrar duracion de los programas a los que esta matriculado un empleado')
        print('[2] Mostrar empleados matriculados en un programa de capacitacion')
        print('[3] Informar Empleados no matriculados en ningun programa')
        print('[0] Salir del programa')
        op = int(input('Seleccione una opcion: '))
    except ValueError:
        pass
    return op