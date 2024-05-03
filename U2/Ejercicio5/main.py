from gestorEquipos import GestorEquipos
from gestorFechas import GestorFechas
from menu import menu
if __name__ == '__main__':
    gestorE = GestorEquipos()
    gestorF = GestorFechas()
    bandera = True
    while bandera:
        op = int(input('Ingrese una Opcion: '))
        if op == 1:
            gestorE.leeEquiposCSV()
        elif op == 2:
            gestorF.leeFechasCSV()
        elif op == 3:
            nom = input("Ingrese el nombre del equipo: ")
            gestorE.listarEquipo(nom)
        elif op == 4:
            pass
        elif op == 5:
            gestorE.ordenaLista()
        elif op == 6:
            gestorE.cargaCSV()
        elif op == 7:
            bandera = False