from Ubicacion import *
from Ocupacion import *

class Vacante:
    def __init__(self, numVacantes, salario, expNecesaria, tipoContrato):
        self.__numVacantes = numVacantes
        self.__salario = salario
        self.__expNecesaria = expNecesaria
        self.__tipoContrato = tipoContrato
        self.ubicacion=Ubicacion(codDepartmento="",codMunicipio="",nombreDepartamento="",nombreMunicipio="")
        self.ocupacion=Ocupacion(codigo="",nombre="",descripcion="")
    def getnumVacantes(self):
        return self.__numVacantes

    def getsalario(self):
        return self.__salario

    def getexpNecesaria(self):
        return self.__expNecesaria

    def gettipoContrato(self):
        return self.__tipoContrato        