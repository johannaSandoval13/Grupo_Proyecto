from Usuario import *

class Persona(Usuario):
    def __init__(self,pOcupacional,estudios,exp,documento,correo,contraseña):
        super().__init__(documento,correo,contraseña)
        self.__pOcupacional=pOcupacional
        self.__estudios=estudios
        self.__exp=exp
        
    def getpOcupacional(self):
        return self.__pOcupacional
    def setpOcupacional(self,pOcupacional):
        self.__pOcupacional=pOcupacional
    def getEstudios(self):
        return self.__estudios
    def setEstudios(self,estudios):
        self.__estudios=estudios
    def getExp(self):
        return self.__exp
    def setExp(self,exp):
        self.__exp=exp