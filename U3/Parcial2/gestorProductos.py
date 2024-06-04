from classProducto import Producto
from classProductoCongelado import ProductoCongelado
from classProductoRefrigerado import ProductoRefrigerado
import csv
class GestorProductos:
    __lista_productos = license

    def __init__(self):
        self.__lista_productos = []

    def agregar_producto(self, producto):
        if isinstance(producto, Producto):
            self.__lista_productos.append(producto)
        
    def carga_productos_csv(self):
        try:
            with open('productos.csv') as archivo:
                reader = csv.reader(archivo, delimiter=';')
                band = True
                for fila in reader: 
                    if band:
                        band = False
                    else: 
                        if fila[0].lower() == 'c':
                            tipo, nombre, fechaE, fechaV, temp, pais, num_lote, costo, porcNitrogeno, porcOxigeno, porcDioxido, porcVapor, metodo = fila
                            unCongelado = ProductoCongelado(nombre, fechaE, fechaV, temp, pais, num_lote, costo, porcNitrogeno, porcOxigeno, porcDioxido, porcVapor, metodo)
                            self.agregar_producto(unCongelado)
                        elif fila[0].lower() == 'r':
                            tipo, nombre, fechaE, fechaV, temp, pais, num_lote, costo, organismo, a, b, c, d = fila
                            unRefrigerado = ProductoRefrigerado(nombre, fechaE, fechaV, temp, pais, num_lote, costo, organismo)
                            self.agregar_producto(unRefrigerado)
                        else:
                            raise AssertionError
        except FileNotFoundError as e:
            print(e)
        except AssertionError:
            print('Se leyo un producto de tipo desconocido')
        else: print('se leyo productos.csv')
    
    def pide_producto(self):
        try:
            tipo = input("Ingrese el tipo de producto (R: para refrigerado - C: para congelado):")
            nombre = input("Nombre del producto: ")
            fechaE = input("Fecha de elaboración: ")
            fechaV = input("Fecha de vencimiento: ")
            temp = float(input("Temperatura de almacenamiento: "))
            pais = input("País de origen: ")
            num_lote = input("Número de lote: ")
            costo = float(input("Costo del producto: "))
            if tipo.lower() == 'c':
                porcNitrogeno = float(input("Porcentaje de nitrogeno: "))
                porcOxigeno = float(input("Porcentaje de oxigeno: "))
                porcDioxido = float(input("Porcentaje de dioxido: "))
                porcVapor = float(input("Porcentaje de vapor: "))
                metodo = input("Metodo de congelación: ")
                producto =  ProductoCongelado(nombre, fechaE, fechaV, temp, pais, num_lote, costo, porcNitrogeno, porcOxigeno, porcDioxido, porcVapor, metodo)
            elif tipo.lower() == 'r':
                organismo = input("Codigo del organismo de supervision: ")
                producto = ProductoRefrigerado(nombre, fechaE, fechaV, temp, pais, num_lote, costo, organismo)
        except ValueError:
            print("Error: Por favor, ingrese un valor válido.")
        else: 
            print('Producto Agregado! ')
            return producto

    def agrega_producto_ingresado(self):
        try: 
            op = input('Quiere agregar un producto? (si - no): ')
            while op.lower() == 'si':
                producto = self.pide_producto()
                self.agregar_producto(producto)
                op = input('Quiere agregar otro producto? (si - no): ')
            raise AssertionError
        except AssertionError:
            print('Finalizada la carga de productos')
    
    def mostrar_tipo_producto(self, pos):
        try: 
            if pos < 0 or pos >= len(self.__lista_productos):
                raise IndexError('Posicion fuera de rango')
            producto = self.__lista_productos[pos]
            if isinstance(producto, ProductoCongelado):
                print(f'\n-El producto en la posicion {pos+1} es un Congelado.')
            elif isinstance(producto, ProductoRefrigerado):
                print(f'\n-El producto en la posicion {pos+1} es un Refrigerado.')
            else:
                print('Tipo de producto desconocido.')            
        except IndexError as e:
            print(e) 

    def cantidad_cada_tipo(self):
        cant_refrigerados = 0
        cant_congelados = 0
        for producto in self.__lista_productos:
            if isinstance(producto, ProductoCongelado):
                cant_congelados += 1
            elif isinstance(producto, ProductoRefrigerado):
                cant_refrigerados +=1
        print('\nLa cantidad de productos congelados es: {}'.format(cant_congelados))
        print('La cantidad de productos refrigerados es: {}\n'.format(cant_refrigerados))
    
    def muestra_datos_lista(self):
        for producto in self.__lista_productos:
            producto.mostrar_informacion()
