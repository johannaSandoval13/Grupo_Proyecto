class Oferta:
    def __init__(self, ocupacion, departamento):
        self.ocupacion = ocupacion
        self.departamento = departamento

    def getOcupacion(self):
        return self.ocupacion

    def getDepartamento(self):
        return self.departamento


class Usuario:
    def __init__(self, documento, correo, contraseña):
        self.documento = documento
        self.correo = correo
        self.contraseña = contraseña

    def getDocumento(self):
        return self.documento

    def setpOcupacional(self, documento):
        self.documento = documento

    def getCorreo(self):
        return self.correo

    def setCorreo(self, correo):
        self.correo = correo

    def getContraseña(self):
        return self.contraseña

    def setContraseña(self, contraseña):
        self.contraseña = contraseña


class Empresa(Usuario):
    def __init__(self, rLegal, nTrabajadores, aEconomica, documento, correo, contraseña):
        super().__init__(documento, correo, contraseña)
        self.rLegal = rLegal
        self.nTrabajadores = nTrabajadores
        self.aEconomica = aEconomica

    def getrLegal(self):
        return self.rLegal

    def setrLegal(self, rLegal):
        self.rLegal = rLegal

    def getnTrabajadores(self):
        return self.nTrabajadores

    def setnTrabajadores(self, nTrabajadores):
        self.nTrabajadores = nTrabajadores

    def getaEconomica(self):
        return self.aEconomica

    def setContraseña(self, aEconomica):
        self.aEconomica = aEconomica


class Persona(Usuario):
    def __init__(self, pOcupacional, estudios, exp, documento, correo, contraseña):
        super().__init__(documento, correo, contraseña)
        self.pOcupacional = pOcupacional
        self.estudios = estudios
        self.exp = exp

    def getpOcupacional(self):
        return self.pOcupacional

    def setpOcupacional(self, pOcupacional):
        self.pOcupacional = pOcupacional

    def getEstudios(self):
        return self.estudios

    def setEstudios(self, estudios):
        self.estudios = estudios

    def getExp(self):
        return self.exp

    def setExp(self, exp):
        self.exp = exp


# Ejemplo de uso
ofertas = [
    Oferta("Desarrollador", "Tecnología"),
    Oferta("Diseñador", "Creativo"),
    Oferta("Contador", "Finanzas"),
    Oferta("Ingeniero", "Ingeniería")
]

def mostrar_ofertas(ofertas, filtro_ocupacion=None, filtro_departamento=None):
    for oferta in ofertas:
        if filtro_ocupacion and oferta.getOcupacion() != filtro_ocupacion:
            continue
        if filtro_departamento and oferta.getDepartamento() != filtro_departamento:
            continue
        print("Ocupación:", oferta.getOcupacion())
        print("Departamento:", oferta.getDepartamento())