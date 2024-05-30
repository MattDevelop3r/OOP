from menuOpciones import menu
from gestorEmpleados import GestorEmpleados
from gestorProgramas import GestorProgramasCapacitacion
from gestorMatriculas import GestorMatriculas
if __name__ == '__main__':

    GE = GestorEmpleados()
    GPC = GestorProgramasCapacitacion()
    GM = GestorMatriculas()
    GE.carga_empleados()
    GPC.carga_programas()
    GM.cargar_matriculas(GE, GPC)

    opcion = menu()

    while opcion != 0:
        if opcion == 1:
            try:
                id_em = int(input('Ingrese el id del empleado: '))
                GM.duracion_programas_empleado(id_em)
            except ValueError:
                print('Error en el tipo de dato ingresado, ingrese un numero de id')
            except AssertionError:
                print('Error! No se encontró empleado con ese id')
            except:
                print('Error! vuelva a ingresar una opcion')
        elif opcion == 2:
            try:
                nom = input('Ingrese el nombre del programa de capacitacion: ')
                GM.empleados_matriculados_programa(nom)
            except AssertionError:
                print('Error! No se encontró ese programa de capacitacion')
            except:
                print('Error! vuelva a ingresar una opcion')   
        elif opcion == 3:
            GM.empleados_sin_matricula(GE)
        else: 
            print('Opcion Invalida! ingrese nuevamente')
        opcion = menu()