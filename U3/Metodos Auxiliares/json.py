load() o loads()
dump() o dumps()

def toJSON(self):
    d = dict(
    __class__=self.__class__.__name__,
    puntos=[punto.toJSON() for punto in self.__puntos]
    )
    return d

class ObjectEncoder(object):
    def decodificarDiccionario(self, d):
        if '__class__' not in d:
            return d
        else:
            class_name=d['__class__']
            class_=eval(class_name)
            if class_name=='Manejador':
                puntos=d['puntos']
                dPunto = puntos[0]
                manejador=class_()
                for i in range(len(puntos)):
                    dPunto=puntos[i]
                    class_name=dPunto.pop('__class__')
                    class_=eval(class_name)
                    atributos=dPunto['__atributos__']
                    unPunto=class_(**atributos)
                    manejador.agregarPunto(unPunto)
        return manejador

if __name__=='__main__':
    jsonF=ObjectEncoder()
    puntos = Manejador()
    bandera=True
    while bandera:
        menu=Menu()
        opcion=menu.mostrarMenu()
        if opcion==1:
            print('Creando un nuevo Punto')
            x=int(input('Coordenada x: '))
            y=int(input('Coordenada y: '))
            punto=Punto(x,y)
            puntos.agregarPunto(punto)
        else:
            if opcion==2:
                d=puntos.toJSON()
                jsonF.guardarJSONArchivo(d,'datosPuntos.json')
            else:
                if opcion==3:
                    diccionario=jsonF.leerJSONArchivo('datosPuntos.json')
                    puntos=jsonF.decodificarDiccionario(diccionario)
                else:
                    if opcion==4:
                        puntos.mostrarDatos()
                    else:
                        bandera=False
                        print('Ha seleccionado salir, hasta la vuelta')