from Ubicacion import *
from Ocupacion import *

class Vacante:
    def __init__(self, numVacantes, salario, expNecesaria, tipoContrato):
        self.__numVacantes = numVacantes
        self.__salario = salario
        self.__expNecesaria = expNecesaria
        self.__tipoContrato = tipoContrato
        self.ubicacion=Ubicacion()
        self.ocupacion=Ocupacion()