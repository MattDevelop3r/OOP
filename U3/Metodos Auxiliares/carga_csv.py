def carga_csv(self):
        try: 
            archivo = open('Ejercicio1\\EdificioNorte.csv')
            reader = csv.reader(archivo, delimiter=';')
            aux = 0
            for fila in reader:
                if (int(fila[0]) != aux):  # Es un nuevo edificio
                    edificio = Edificio(int(fila[0]), fila[1], fila[2], fila[3], int(fila[4]), int(fila[5]))
                    self.agregar_edificio(edificio)
                    aux = int(fila[0])
                else:  # Es un departamento del edificio actual
                    edificio.agregar_departamento(int(fila[1]), fila[2], int(fila[3]), int(fila[4]), int(fila[5]), int(fila[6]), float(fila[7]))
            
        except FileNotFoundError:
            print('Archivo no encontrado')
        else: 
            print('Archivo EdificioNorte.csv leido')

def carga_csv_JSON(self):
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
        
    except FileNotFoundError:
        print('Archivo no encontrado')
    else: 
        print('calefactores.json leido!')

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