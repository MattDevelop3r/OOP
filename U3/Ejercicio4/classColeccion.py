from classNodo import Nodo
from classAudioLibro import AudioLibro
from classLibroImpreso import LibroImpreso
import csv
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
        if self.__indice==self.__tope:
            self.__actual=self.__comienzo
            self.__indice=0
            raise StopIteration
        else:
            self.__indice+=1
            dato= self.__actual.getDato()
            self.__actual=self.__actual.getSiguiente()
            return dato
    
    def get_tope(self):
        return self.__tope
    
    def agregar_publicacion(self, publicacion):
        nodo = Nodo(publicacion)
        nodo.set_siguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__actual = nodo
        self.__tope += 1
        print('Publicacion Cargada!!!')
    
    def carga_libros_impresos(self):
        try: 
            with open('libroimpreso.csv', 'r') as archivo:
                reader = csv.reader(archivo, delimiter=',')
                bandera = True
                for fila in reader:
                    if bandera: 
                        bandera = False
                    else: 
                        titulo, categoria, precioBase, nomAutor, fecha, cantP = fila
                        self.agregar_publicacion(LibroImpreso(titulo, categoria, float(precioBase), nomAutor, fecha, int(cantP)))
            archivo.close()
        except FileNotFoundError:
            print('Archivo no encontrado')
        else: 
            print('archivo librosimpresos.csv leido')

    def carga_audiolibros(self):
        with open('audiolibro.csv', 'r') as archivo:
            reader = csv.reader(archivo, delimiter=',')
            bandera = True
            for fila in reader:
                if bandera: 
                    bandera = False
                else: 
                    titulo, categoria, precioBase, tiempoR, nombreN = fila
                    self.agregar_publicacion(AudioLibro(titulo, categoria, float(precioBase), int(tiempoR), nombreN))
        archivo.close()
        print('archivo audiolibros.csv leido')

    def lee_datos_carga(self):
        try:
            tipo = int(input('-Ingrese tipo de publicacion: \n  [1] Libro Impreso\n  [2] Audiolibro\n'))
        except UnboundLocalError:
            raise UnboundLocalError('No ingreso nada, intente nuevamente')
        except:
            print('Tipo de publicacion invalida!!!')
        if tipo > 2 or tipo < 1:
            return 
        titulo = input('-Ingrese titulo: ')
        categoria = input('-Ingrese categoria: ')
        prec_base = float(input('-Ingrese precio base: '))
        if tipo == 1:
            autor = input('-Ingrese nombre del autor: ')
            fecha = input('-Ingrese fecha de publicacion: ')
            cant_pag = int(input('-Ingrese la cantidad de paginas: '))
            self.agregar_publicacion(LibroImpreso(titulo, categoria, prec_base, autor, fecha, cant_pag))
        elif tipo == 2:
            t_reproduccion = int(input('-Ingrese el tiempo de reproduccion (minutos): '))
            nombre_nar = input('-Ingrese el nombre del narrador: ')
            self.agregar_publicacion(AudioLibro(titulo, categoria, prec_base, t_reproduccion, nombre_nar))
    
    def mostrar_tipo_publicacion(self, pos):
        try: 
            if pos < 0 or pos >= self.__tope:
                raise IndexError('Posicion fuera de rango')
            nodo = self.__comienzo
            indice = 0
            while nodo is not None and indice < pos:
                nodo = nodo.get_siguiente()
                indice += 1
            if nodo is not None:
                publicacion = nodo.get_publicacion()  
                if isinstance(publicacion, AudioLibro):
                    print(f'La publicación en la posición {pos+1} es un Audiolibro.')
                elif isinstance(publicacion, LibroImpreso):
                    print(f'La publicación en la posición {pos+1} es un Libro Impreso.')
                else:
                    print('Tipo de publicación desconocido.')  
        except IndexError as e:
            print(e) 

    def cantidad_cada_tipo(self):
        nodo = self.__comienzo
        cant_libro_impreso = 0
        cant_audiolibro = 0
        while nodo is not None:
            publicacion = nodo.get_publicacion()
            if isinstance(publicacion, LibroImpreso):
                cant_libro_impreso += 1
            elif isinstance(publicacion, AudioLibro):
                cant_audiolibro +=1
            nodo = nodo.get_siguiente()
        print('\nLa cantidad de libros impresos en la coleccion es: {}'.format(cant_libro_impreso))
        print('La cantidad de audiolibros en la coleccion es: {}'.format(cant_audiolibro))
    
    def mostrar_datos(self):
        nodo = self.__comienzo
        while nodo is not None:
            titulo = nodo.get_publicacion().get_titulo()
            categoria = nodo.get_publicacion().get_categoria()
            publicacion = nodo.get_publicacion()
            importe_venta = publicacion.get_importe_venta()
            if isinstance(publicacion, LibroImpreso):
                print(f'LIBRO IMPRESO - Titulo: {titulo} - Categoria: {categoria} - Importe Venta: {importe_venta}')
            if isinstance(publicacion, AudioLibro):
                print(f'AUDIOLIBRO - Titulo: {titulo} - Categoria: {categoria} - Importe Venta: {importe_venta}')
            nodo = nodo.get_siguiente()


                    
