from gestorMotos import GestorMotos
from gestorPedidos import GestorPedidos
from moto import Moto
from pedido import Pedido
import csv
def CSVMotoReader():
    archivo = open('datosMotos.csv')
    reader = csv.reader(archivo, delimiter=';')
    for fila in reader:
        pat = fila[0]
        marca = fila[1]
        nya = fila[2]
        km = int(fila[3])
        unaMoto = Moto(pat,marca,nya,km)
        GestorMotos.putMoto(unaMoto)
    archivo.close()
def CSVPedidoReader():
    archivo = open('datosPedidos.csv')
    reader = csv.reader(archivo, delimiter=';')
    for fila in reader:
        patMoto = fila[0]
        id = fila[1]
        comidas = fila[2]
        tiempoEst = fila[3]
        tiempoReal = fila[4]
        precio = fila[5]
        unPedido = Pedido(patMoto, id, comidas, tiempoEst, tiempoReal, precio)
        GestorPedidos.putPedido(unPedido)
    archivo.close()
def cargaPedido():
        patMoto = input('Ingrese el num patente: ')
        motoExiste = False
        for moto in GestorMotos.__motos:
            if moto == patMoto:
                motoExiste == True
        if motoExiste:
            id = input(int('Ingrese el id: '))
            comidas = input('Ingrese las comidas: ')
            tiempoEst = input(int('Ingrese el tiempo estimado: '))
            precio = input(float('Ingrese el precio: '))
            unPedido = Pedido(patMoto, id, comidas, tiempoEst, 0, precio)
            GestorPedidos.putPedido(unPedido)   
        else: print('Error')
def menu():
        print("1. Leer los Datos de las motos desde csv")
        print("2. Leer los Datos de los pedidos desde csv")
        print("3. Cargar Nuevos Pedidos")
        print("4. Modificar Tiempo Real entrega de un pedido")
        print("5. Tiempo Promedio dada una Moto")
        print("6. Generar un listado para cada moto")
        print("7. Salir")
        return int(input("Seleccione una opción: "))
if __name__ == '__main__':
    flag = True
    while flag:
        opcion = menu()
        if opcion == 1:
            CSVMotoReader()
        elif opcion == 2:
            CSVPedidoReader()
        elif opcion == 3:
            cargaPedido()
        elif opcion == 4:
            pat = input('Ingrese Num Patente: ')
            id = input(int('Ingrese el ID del pedido: '))
            temp = input(int('Ingrese el tiempo Real de entrega: '))
            GestorPedidos.modificaTiempo(pat,id,temp)
        elif opcion == 7: 
            flag = False