from Ocupacion import *

class Oferta(Ocupacion):
    def __init__(self,codigoOc,nombreOc,funciones,habilidades,exp,nVacantes,contrato,jornada,salario,fCierre):
        super().__init__(codigoOc,nombreOc)
        self.funciones=funciones
        self.habilidades=habilidades
        self.exp=exp
        self.nVacantes=nVacantes
        self.contrato=contrato
        self.jornada=jornada
        self.salario=salario
        self.fCierre=fCierre