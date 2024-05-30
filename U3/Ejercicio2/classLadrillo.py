class Ladrillo:
    __alto : 7
    __largo: 25
    __ancho : 15
    __cantidad : int
    __id : int
    __kgMatprimUti: float
    __costo : float
    __materiales : list

    def __init__(self, cant, id, kgMP, costo):
        self.__cantidad = int(cant)
        self.__id = int(id)
        self.__kgMatprimUti = float(kgMP)
        self.__costo = float(costo)
        self.__materiales = []    
    
    def agregarMaterial(self,material):
        if (material in self.__materiales)is False:
            self.__materiales.append(material)
            print(f"Al ladrillo {self.__id} se le agrega el material {material.get_mat()}")
        else:
            print(f"No se agrega el material {material.get_mat()} al ladrillo {self.__id} porque ya lo tiene")

    def get_cant(self):
        return self.__cantidad
    def get_id(self):
        return self.__id
    def get_kgMP(self):
        return self.__kgMatprimUti
    def get_costo(self):
        return self.__costo
    def get_materiales(self):
        return self.__materiales
    @classmethod 
    def get_alto(cls):
        return cls.__alto
    @classmethod
    def get_largo(cls):
        return cls.__largo
    @classmethod
    def get_ancho(cls):
        return cls.__ancho