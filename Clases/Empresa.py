from Usuario import *

class Empresa(Usuario):
    def __init__(self,rLegal,nTrabajadores,aEconomica,documento,correo,contraseña):
        super().__init__(documento,correo,contraseña)
        self.__rLegal=rLegal
        self.__nTrabajadores=nTrabajadores
        self.__aEconomica=aEconomica
        self.__vacantes=[]
        self.__cargos=[]

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
    def verOcupaciones(self):
        cont=0
        for l in self.__cargos:
            cont+=1
            print(f"{cont}. {l.getCodigo()} {l.getNombre()}")
            print("Funciones: ")
            print(f"{l.verFuncionesCargo()}")
    def Ocupaciones(self):
        return self.__cargos