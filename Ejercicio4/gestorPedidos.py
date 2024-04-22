from pedido import Pedido
class GestorPedidos: 
    __pedidos: list

    def __init__(self):
        self.__pedidos = Pedido
    
    def putPedido(self, Pedido):
        self.__pedidos.append(Pedido)
    
    def ordenaPedidos(self):
        n = len(self.__pedidos)
        for i in range(n-1):       # <-- bucle padre
            for j in range(n-1-i): # <-- bucle hijo
                if self.__pedidos[j].__patMoto > self.__pedidos[j].__patMoto:
                    self.__pedidos[j].__patMoto, self.__pedidos[j+1].__patMoto = self.__pedidos[j+1].__patMoto, self.__pedidos[j].__patMoto

    def modificaTiempo(self, id):
        pass