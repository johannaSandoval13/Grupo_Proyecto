from Usuario import *

class Empresa(Usuario):
    def __init__(self,rLegal,nTrabajadores,aEconomica,documento,correo,contraseña):
        super().__init__(documento,correo,contraseña)
        self.__rLegal=rLegal
        self.__nTrabajadores=nTrabajadores
        self.__aEconomica=aEconomica

    def getrLegal(self):
        return self.__rLegal
    def setrLegal(self,rLegal):
        self.__rLegal=rLegal
    def getnTrabajadores(self):
        return self.__nTrabajadores
    def setnTrabajadores(self,nTrabajadores):
        self.__nTrabajadores=nTrabajadores
    def getaEconomica(self):
        return self.__aEconomica
    def setContraseña(self,aEconomica):
        self.__aEconomica=aEconomica
