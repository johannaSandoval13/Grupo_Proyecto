class Pais():
    def __init__(self,codigo,nombre):
        self.__codigo=codigo
        self.__nombre=nombre
        
    def getCodigo(self):
        return self.__codigo
    def setCodigo(self,codigo):
        self.__codigo=codigo
    
    def getNombre(self):
        return self.__nombre
    def setNombre(self,nombre):
        self.__nombre=nombre