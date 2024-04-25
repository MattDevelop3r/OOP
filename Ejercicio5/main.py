from gestorEquipos import GestorEquipos
from gestorFechas import GestorFechas
from claseEquipo import Equipo
from claseFecha import Fecha
if __name__ == '__main__':
    chacarita = Equipo(1, 'Chacarita', 2, 3, 1)
    listaEquipos = GestorEquipos()
    listaEquipos.addEquipo(chacarita)
    listaEquipos.cargaCSV()
    listaEquipos.leeCSV()