from menu_opciones import menu
from gestorEdificios import GestorEdificios
if __name__ == '__main__':
    gestorE = GestorEdificios()
    gestorE.leeCSV()
    op = -1
    while op != 5:
        try: 
            op = menu()
        except ValueError:
            print('tipo de dato ingresado invalido! seleccione una opcion')  
        if op == 1: 
            nombre_edificio = input('\n- Ingrese el nombre del edificio: ')
            gestorE.mostrar_propietarios(nombre_edificio)
    
        if op == 2: 
            try: 
                id_edificio = int(input('\n- Ingrese el id del edificio: '))
                gestorE.mostrar_superficie_edif(id_edificio)
            except ValueError:
                print('tipo de dato ingresado invalido! debe ser un id de edificio')
        if op == 3: 
            nom_prop = input('\n- Ingrese el nombre del propietario del dpto: ')
            gestorE.mostrar_superficie_dept(nom_prop)
        if op == 4: 
            try: 
                num_piso = int(input('\n- Ingrese el numero de piso: '))
                gestorE.contar_dptos(num_piso)
            except ValueError:
                print('tipo de dato ingresado invalido! debe ser un numero de piso')
    