from Vacante import *

class Oferta(Vacante):
    def __init__(self,id,numPostulados,fechaPub,fechaCierre,candidatosEntrevistar):
        self.__id=id
        self.__vacante=Vacante()
        self.__numPostulados=numPostulados
        self.__fechaPub=fechaPub
        self.__fechaCierre=fechaCierre
        self.__candidatosEntrevistar=candidatosEntrevistar