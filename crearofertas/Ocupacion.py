class Ocupacion:
    def __init__(self,codigo,nombre,descripcion):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__descripcion = descripcion

    def getcodigo(self):
        return self.__codigo

    def getnombre(self):
        return self.__nombre

    def getdescripcion(self):
        return self.__descripcion

