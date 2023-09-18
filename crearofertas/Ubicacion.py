class Ubicacion:
    def __init__(self,codDepartmento,codMunicipio,nombreDepartamento,nombreMunicipio):
        self.__codDepartmento = codDepartmento
        self.__codMunicipio = codMunicipio
        self.__nombreDepartamento = nombreDepartamento
        self.__nombreMunicipio = nombreMunicipio
        
    def getcodDepartmento(self):
        return self.__codDepartmento

    def getcodMunicipio(self):
        return self.__codMunicipio

    def getnombreDepartamento(self):
        return self.__nombreDepartamento

    def getnombreMunicipio(self):
        return self.__nombreMunicipio