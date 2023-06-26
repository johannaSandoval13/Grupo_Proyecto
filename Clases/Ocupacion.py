class Ocupacion :
    def __init__(self,codigo,nombre,descripcion) :
        self.__codigo=codigo
        self.__nombre=nombre
        self.__descripcion=descripcion
        self.__funciones=[]
    def getCodigo(self):
        return self.__codigo
    
    def getNombre(self):
        return self.__nombre
    
    def getFunciones(self):
        return self.__funciones
    
    def setCodigo(self, codigo):
        self.__codigo = codigo
        
    def setNombre(self, nombre):
        self.__nombre = nombre
        
    def agregarFunciones(self, funcion):
        self.__funciones.append(funcion)
