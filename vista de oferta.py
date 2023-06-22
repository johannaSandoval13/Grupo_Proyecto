class Persona:
    def __init__(self, nombre, apellido, correo, contraseña):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.contraseña = contraseña

class Menu:
    def __init__(self, opciones):
        self.opciones = opciones

class CarteleraVacantes:
    def __init__(self, vacantes):
        self.vacantes = vacantes

class Mapa:
    def __init__(self):
        pass

class Departamento:
    def __init__(self, nombre, vacantes):
        self.nombre = nombre
        self.vacantes = vacantes

class Municipio:
    def __init__(self, nombre):
        self.nombre = nombre

class AreaOcupacional:
    def __init__(self):
        pass

class Oferta:
    def __init__(self, nombreCargo, salario, lugar, habilidades, competencias, mesesExp, tipoSalario, tipoContrato, jornadaTrabajo, fechaCierre):
        self.nombreCargo = nombreCargo
        self.salario = salario
        self.lugar = lugar
        self.habilidades = habilidades
        self.competencias = competencias
        self.mesesExp = mesesExp
        self.tipoSalario = tipoSalario
        self.tipoContrato = tipoContrato
        self.jornadaTrabajo = jornadaTrabajo
        self.fechaCierre = fechaCierre

print(Persona)
print(Menu)
print(CarteleraVacantes)
print(Mapa)
print(Departamento)
print(Municipio)
print(AreaOcupacional)
print(Oferta)