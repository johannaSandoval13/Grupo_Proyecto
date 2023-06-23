class Usuario:
    def __init__(self, documento, correo, contraseña):
        self.__documento=documento
        self.__correo=correo
        self.__contraseña=contraseña


    def getDocumento(self):
        return self.__documento
    def setpOcupacional(self,documento):
        self.__documento=documento
    def getCorreo(self):
        return self.__correo
    def setCorreo(self,correo):
        self.__correo=correo
    def getContraseña(self):
        return self.__contraseña
    def setContraseña(self,contraseña):
        self.__contraseña=contraseña