class Postulacion():
    def __init__(self,codigo,oferta,persona):
        self.__codigo=codigo
        self.__oferta=oferta
        self.__persona=persona
        
    def getCodigo(self):
        return self.__codigo
    def setCodigo(self,codigo):
        self.__codigo=codigo
        
    def getCargoOferta(self):
        return self.__oferta.get_cargoVacante()
    
    
    def setOferta(self,oferta):
        self.__oferta=oferta
    
    def getPersona(self):
        return self.__persona
    def setPersona(self,persona):
        self.__persona=persona
            