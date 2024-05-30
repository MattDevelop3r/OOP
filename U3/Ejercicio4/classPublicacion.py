class Publicacion:
    __titulo: str
    __categoria: str
    __precio_base: float

    def __init__(self, titulo, categoria, precioBase):
        self.__titulo = titulo
        self.__categoria = categoria
        self.__precio_base = float(precioBase)
    
    def get_titulo(self):
        return self.__titulo
    def get_categoria(self):
        return self.__categoria
    def get_precio_base(self):
        return self.__precio_base