from nodo import Nodo
from classCalefactorElectrico import CalefactorElectrico
from classCalefactorGas import CalefactorGas
import json

class Coleccion:
    __comienzo: Nodo
    __actual: Nodo
    __indice: int
    __tope: int

    def __init__(self):
        self.__comienzo = None
        self.__actual = None
        self.__indice = 0
        self.__tope = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice += 1
            calefactor = self.__actual.get_calefactor()
            self.__actual = self.__actual.get_siguiente()
            return calefactor
        
    def agregar_calefactor(self, calefactor):
        nodo = Nodo(calefactor)
        nodo.set_siguiente(self.__comienzo)
        self.__comienzo=nodo
        self.__actual=nodo
        self.__tope+=1

    def carga_calefactores(self):
        try:
            with open('calefactores.json', 'r', encoding='utf-8') as archivo:
                data = json.load(archivo)
            for calefactor_info in data["calefactores"]:
                calefactor = None 
                if calefactor_info["tipo"].lower() == "electrico":
                    calefactor = CalefactorElectrico(
                        calefactor_info["marca"],
                        calefactor_info["modelo"],
                        calefactor_info["pais_fabricacion"],
                        calefactor_info["precio_lista"],
                        calefactor_info["forma_pago"],
                        calefactor_info["cantidad_cuotas"],
                        calefactor_info["promocion"],
                        calefactor_info["potencia_maxima"]
                    )
                elif calefactor_info["tipo"].lower() == "gas natural":
                    calefactor = CalefactorGas(
                        calefactor_info["marca"],
                        calefactor_info["modelo"],
                        calefactor_info["pais_fabricacion"],
                        calefactor_info["precio_lista"],
                        calefactor_info["forma_pago"],
                        calefactor_info["cantidad_cuotas"],
                        calefactor_info["promocion"],
                        calefactor_info["matricula"],
                        calefactor_info["calorias"]
                    )
                self.agregar_calefactor(calefactor)
            print('calefactores.json leido!')
        except UnboundLocalError as e:
            print(e)

    def pide_datos(self):
        band = True
        while band:
            tipo = input('\nIngrese el tipo de calefactor (gas - electrico): ')
            if tipo.lower() == 'gas' or tipo.lower() == 'electrico':
                band = False
            else:
                print('Tipo de calefactor invalido.')
        marca = input('Ingrese la marca: ')
        modelo = input('Ingrese el modelo: ')
        pais = input('Ingrese el pais: ')
        band = True
        while band:
            try:
                precio = float(input("Ingresa el precio: "))
                band = False
            except ValueError:
                print("El valor ingresado no es un número flotante. Por favor, intenta de nuevo.")    
        band = True 
        while band:
            formaPago = input("Ingresa la forma de pago (contado - cuotas): ")
            if formaPago.lower() == 'contado' or formaPago.lower() == 'cuotas':
                band = False
            else:    
                print("Ingrese una forma de pago valida.")
        band = True
        while band:
            try:
                cantCuotas = int(input('Ingrese la cantidad de cuotas: '))
                band = False
            except: 
                print('El valor ingresado no es un entero. Por favor. intenta de nuevo')
        band = True
        while band:
            promocion = input('Ingrese si tiene promocion (si - no): ')
            if promocion.lower() == 'si' or promocion.lower() == 'no':
                band = False
            else:
                print('Ingrese una forma valida de promocion.')
            
        if tipo == 'gas':
            matricula = input('Ingrese una matricula: ')
            calorias = input('Ingrese la cantidad de calorias: ')
            un_calefactor_gas = CalefactorGas(marca, modelo, pais, precio, formaPago, cantCuotas, promocion, matricula, calorias)
            return un_calefactor_gas
        elif tipo == 'electrico':
            potencia = input('Ingrese la potencia maxima: ')
            un_calefactor_electrico = CalefactorElectrico(marca, modelo, pais, precio, formaPago, cantCuotas, promocion, potencia)
            return un_calefactor_electrico

    def insertar_calefactor(self):
        calefactor = self.pide_datos()
        nodo = Nodo(calefactor)
        band = True
        while band:
            try: 
                pos = int(input('Ingrese la posicion donde insertar: '))
                if pos <= 0 or pos > self.__tope + 1:
                    raise ValueError
                band = False
            except ValueError:
                print('Posicion invalida, ingrese nuevamente')
        if pos == 1:
            nodo.set_siguiente(self.__comienzo)
            self.__comienzo = nodo
        else:
            aux = self.__comienzo
            for i in range(1, pos - 1):
                aux = aux.get_siguiente()
            nodo.set_siguiente(aux.get_siguiente())
            aux.set_siguiente(nodo)
        self.__tope += 1

    def agregar_calefactor_ingresado(self):
        calefactor = self.pide_datos()
        self.agregar_calefactor(calefactor)
    
    def mostrar_tipo_por_posicion(self, pos):
        tipo = 'Tipo desconocido'  
        if pos < 1 or pos > self.__tope:
            print('Posición fuera de rango.')
            return
        aux = self.__comienzo
        for i in range(1, pos):
            aux = aux.get_siguiente()
        calefactor = aux.get_calefactor()
        if isinstance(calefactor, CalefactorGas):
            tipo = 'Calefactor a Gas'
        elif isinstance(calefactor, CalefactorElectrico):
            tipo = 'Calefactor Electrico'
        print('En la posición {} hay un {}'.format(pos, tipo))


    def calefactor_gas_menor_precio(self):
        menor = None
        for calefactor in self:
            if isinstance(calefactor, CalefactorGas):
                if menor is None or calefactor.get_precio() < menor.get_precio():
                    menor = calefactor
        if menor is not None:
            print('Marca: {}, Modelo: {}, Kilocalorías: {}'.format(menor.get_marca(), menor.get_modelo(), menor.get_calorias()))
        else:
            print('No hay calefactores a gas en la lista.')

    def mostrar_electricos_por_marca(self, marca_buscada):
        for calefactor in self:
            if isinstance(calefactor, CalefactorElectrico) and calefactor.get_marca().lower() == marca_buscada.lower():
                print('Modelo: {}, Potencia: {}, Precio: {}'.format(calefactor.get_modelo(), calefactor.get_potencia_maxima(), calefactor.get_precio()))

    def mostrar_en_promocion(self):
        for calefactor in self:
            if not isinstance(calefactor, list) and calefactor.get_promocion().lower() == 'si':
                print('Marca: {}, Modelo: {}, País: {}, Precio: {}'.format(
                    calefactor.get_marca(),
                    calefactor.get_modelo(),
                    calefactor.get_pais_fabricacion(),
                    calefactor.get_precio()
                ))
    
    def almacenar_en_archivo(self):
        calefactores = []
        aux = self.__comienzo
        while aux is not None:
            calefactor = aux.get_calefactor()
            if isinstance(calefactor, (CalefactorElectrico, CalefactorGas)):
                calefactores.append(calefactor.to_dict())
                print('calefactor agregado xd')
            else:
                print(f"Se encontró un objeto que no es un calefactor en la posición: {calefactores.index(calefactor)}")
            aux = aux.get_siguiente()
        with open('calefactores2.json', 'w+', encoding='utf-8') as archivo:
            json.dump(calefactores, archivo, indent=4)
        print('Calefactores almacenados en "calefactores2.json".')
