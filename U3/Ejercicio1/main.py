from menu_opciones import menu
from gestorEdificios import GestorEdificios
if __name__ == '__main__':
    gestorE = GestorEdificios()
    gestorE.leeCSV()
    op = 0
    while op != 5:
        op = menu()
        if op == 1: 
            nombre_edificio = input('\n- Ingrese el nombre del edificio: ')
            gestorE.mostrar_propietarios(nombre_edificio)
        if op == 2: 
            id_edificio = int(input('\n- Ingrese el id del edificio: '))
            gestorE.mostrar_superficie_edif(id_edificio)
        if op == 3: 
            nom_prop = input('\n- Ingrese el nombre del propietario del dpto: ')
            gestorE.mostrar_superficie_dept(nom_prop)
        if op == 4: 
            num_piso = int(input('\n- Ingrese el numero de piso: '))
            gestorE.contar_dptos(num_piso)
        else: 
            pass