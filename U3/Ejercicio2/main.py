from menuOpciones import menu
from gestorLadrillo import GestorLadrillo
from gestorMaterial import GestorMaterial
if __name__ == '__main__':
    GL = GestorLadrillo()
    GM = GestorMaterial()
    GL.cargarladrillos()
    GM.cargarMateriales()
    GL.asignarMateriales(GM)
    opcion = menu()
    while opcion != 0:
        if opcion == 1:
            try:
                id = int(input('Ingrese el id del ladrillo: '))
                GL.detallar_datos(id)
            except ValueError:
                print("Entrada invalida. Se esperaba un entero")
            except AssertionError:
                print("Error. El ID ingresado no pertenece a un ladrillo")
        elif opcion == 2:
            GL.mostrar_costo_ladrillos()
        elif opcion == 3:
            GL.mostrar_detalle_ladrillos()
        else:
            print("Opcion Invalida!")
        opcion = menu()

    