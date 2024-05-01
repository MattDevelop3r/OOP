from gestorMotos import *
from gestorPedidos import *
if __name__ == '__main__':
    gestorM = GestorMotos()
    gestorP = GestorPedidos()
    def menu():
        print("1. Leer los Datos de las motos desde csv")
        print("2. Leer los Datos de los pedidos desde csv")
        print("3. Cargar Nuevos Pedidos")
        print("4. Modificar Tiempo Real entrega de un pedido")
        print("5. Tiempo Promedio dada una Moto")
        print("6. Generar un listado para cada moto")
        print("7. Salir")
        return int(input("Seleccione una opción: "))
    flag = True
    while flag:
        opcion = menu()
        if opcion == 1:
            gestorM.CSVMotoReader()
        elif opcion == 2:
            gestorP.CSVPedidoReader()
        elif opcion == 3:
            gestorP.cargaPedidos(gestorM)
        elif opcion == 4:
            gestorP.ordenaPedidos()
            gestorP.modTiempoReal()
        elif opcion == 5:
            gestorP.ordenaPedidos()
            pat = input("\nIngrese una patente: ")
            gestorM.muestraDatos(pat)
            gestorP.tiempoPromedioReal(pat)
        elif opcion == 6:
            gestorP.ordenaPedidos()
            gestorP.listar(gestorM)
        elif opcion == 7: 
            flag = False