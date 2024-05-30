class MaterialRefractario:
    __material : int
    __caracteristicas: str
    __cant_utilizada: float
    __costo_adicional: float
    
    def __init__(self, mat, carac, cant, costo):
        self.__material = int(mat)
        self.__caracteristicas = carac
        self.__cant_utilizada = float(cant)
        self.__costo_adicional = float(costo)
    
    def get_mat(self):
        return self.__material
    def get_carac(self):
        return self.__caracteristicas
    def get_cant_util(self):
        return self.__cant_utilizada
    def get_costo_adicional(self):
        return self.__costo_adicional