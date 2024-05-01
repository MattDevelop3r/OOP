import csv
from clasePedido import Pedido
class GestorPedidos: 
    __pedidos: list

    def __init__(self):
        self.__pedidos = []

    def ordenaPedidos(self):
        self.__pedidos.sort()

    def CSVPedidoReader(self):
        archivo = open("Ejercicio4\\datosPedidos.csv")
        reader = csv.reader(archivo, delimiter=',')
        for fila in reader:
            pat = fila[0]
            id = int(fila[1])
            com = fila[2]
            tMin = int(fila[3])
            prec = float(fila[4])
            unPedido = Pedido(pat, id, com, tMin, 0, prec)
            self.__pedidos.append(unPedido)
        archivo.close()
    def cargaPedidos(self, gestorM):
        print("--- NUEVO PEDIDO ---\n")
        pat = input('Ingrese la Patente: ')
        patenteValida = gestorM.validarPatente(pat)
        if patenteValida: 
            id = int(input('Ingrese ID del pedido: '))
            com = input('Ingrese comidas del pedido: ')
            tMin = input('Ingrese tiempo estimado de entrega del pedido: ')
            prec = float(input('Ingrese Precio del pedido: '))
            PedidoX = Pedido(pat,id,com,tMin,0,prec)
            self.__pedidos.append(PedidoX)
        else:
            print('La pantente no es valida, Intentelo nuevamente')

    def modTiempoReal(self):
        pat = input('\nIngrese la Patente: ')
        id = int(input('Ingrese ID del pedido: '))
        tR = int(input('Ingrese Tiempo Real de Entrega: '))
        i = 0
        while pat != self.__pedidos[i].getPatMoto() or id != self.__pedidos[i].getID() and i < len(self.__pedidos):
            if id == self.__pedidos[i].getID:
                self.__pedidos[i].modTR(tR)
                break
            else:
                i+=1
    
    def tiempoPromedioReal(self, pat):
        sumador = 0
        contador = 0
        for i in range(len(self.__pedidos)):
            if self.__pedidos[i].getPatMoto() == pat:
                contador += 1
                sumador += self.__pedidos[i].getTiempoReal()
        if contador != 0:
            prom = sumador / contador
            print('El tiempo real promedio del conductor es: {}'.format(prom))
        else:
            print("Esa moto no tuvo pedidos!")
    
    def listar(self, gestorM):
        patenteActual = self.__pedidos[0].getPatMoto()
        print('Patente: {}'.format(self.__pedidos[0].getPatMoto()))
        conductor = gestorM.buscaNyA(patenteActual)
        print("{}".format(conductor))
        print('ID PEDIDO --- TIEMPO ESTIMADO --- TIEMPO REAL --- PRECIO')
        total = 0
        for i in range(len(self.__pedidos)):
            if patenteActual == self.__pedidos[i].getPatMoto(): 
                print(f'{self.__pedidos[i].getID()} --- {self.__pedidos[i].getTiempoMin()} --- {self.__pedidos[i].getTiempoReal()} --- {self.__pedidos[i].getPrecio()}')
                total += self.__pedidos[i].getPrecio()
                print('comisiones = ${}'.format((total * 20 )/ 100))
            else:
                total = 0
                patenteActual = self.__pedidos[i].getPatMoto()
                print('Patente: {}'.format(self.__pedidos[i].getPatMoto()))
                conductor = gestorM.buscaNyA(patenteActual)
                print("{}".format(conductor))
                print('ID PEDIDO --- TIEMPO ESTIMADO --- TIEMPO REAL --- PRECIO')
                print(f'{self.__pedidos[i].getID()} --- {self.__pedidos[i].getTiempoMin()} --- {self.__pedidos[i].getTiempoReal()} --- {self.__pedidos[i].getPrecio()}')