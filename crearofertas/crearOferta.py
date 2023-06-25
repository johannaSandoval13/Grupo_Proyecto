from Empresa import *
from Vacante import *
from Ocupacion import *
from Oferta import *

def mostrar_menu_ubicacion():
    print("->Ubicación")
    print("1. Soacha")
    print("2. Cali")
    print("3. Pereira")
def seleccionar_ubicacion():
    mostrar_menu_ubicacion()
    opcion = input("Seleccione una ubicación (1-3): ")
    if opcion == "1":
        ubicacion = Ubicacion("25", "25754", "Cundinamarca", "Soacha")
    elif opcion == "2":
        ubicacion = Ubicacion("76", "76001", "Valle del cauca", "Cali")
    elif opcion == "3":
        ubicacion = Ubicacion("66", "66001", "Risaralda", "Pereira")
    else:
        print("Seleccione nuevamente.")
        return seleccionar_ubicacion()
    return ubicacion

def mostrar_menu_ocupacion():
    print("->Ocupación")
    print("1. Ingenieros de tecnologías de la información")
    print("2. Secretarios")
    print("3. Maquilladores")
def seleccionar_ocupacion():
    mostrar_menu_ocupacion()
    opcion = input("Seleccione una ocupación (1-3): ")
    if opcion == "1":
        ocupacion = Ocupacion("2145", "Ingenieros de tecnologías de la información",
                            "Investigan, planifican, diseñan, evalúan, integran e implementan soluciones informáticas, sistemas operativos, almacenes de datos y software de tecnologías de la información y las comunicaciones.")
    elif opcion == "2":
        ocupacion = Ocupacion("1311", "Secretarios", 
                            "Realizan funciones de secretariado a empleados, profesionales y directivos. Son empleados por el sector público y privado.")
        
    elif opcion == "3":
        ocupacion = Ocupacion("6379", "Maquilladores",
                            "Prestan servicios de maquillaje mediante técnicas")
    else:
        print("seleccione nuevamente.")
        return seleccionar_ocupacion()
    return ocupacion

def crear_empresa():
    print("---> Crear Empresa")
    r_legal = input("Ingrese el representante legal legal de la empresa: ")
    n_trabajadores = input("Ingrese el número de trabajadores de la empresa: ")
    a_economica = input("Ingrese la actividad económica de la empresa: ")
    documento = input("Ingrese el documento del usuario: ")
    correo = input("Ingrese el correo del usuario: ")
    contraseña = input("Ingrese la contraseña del usuario: ")
    empresa = Empresa(r_legal, n_trabajadores, a_economica, documento, correo, contraseña)
    print("---> Empresa")
    print("Representante legal:", empresa.getrLegal())
    print("Número de trabajadores:", empresa.getnTrabajadores())
    print("Actividad económica:", empresa.getaEconomica())
    print("Documento del usuario:", empresa.getDocumento())
    print("Correo del usuario:", empresa.getCorreo())
    print("Contraseña del usuario:", empresa.getContraseña())
    return empresa
def crear_vacante(empresa):
    print("---> Crear Vacantes")
    num_vacantes = input("Ingrese el número de vacantes: ")
    salario = input("Ingrese el salario de la vacante: ")
    exp_necesaria = input("Ingrese la experiencia necesaria para la vacante: ")
    tipo_contrato = input("Ingrese el tipo de contrato: ")
    
    ubicacion = seleccionar_ubicacion()
    ocupacion = seleccionar_ocupacion()
    vacante = Vacante(num_vacantes, salario, exp_necesaria, tipo_contrato)
    vacante.ubicacion = ubicacion
    vacante.ocupacion = ocupacion
    print("--->Vacante:")
    print("Número de vacantes:", vacante.getnumVacantes())
    print("Salario:", vacante.getsalario())
    print("Experiencia necesaria:", vacante.getexpNecesaria())
    print("Tipo de contrato:", vacante.gettipoContrato())
    print("Ubicación:")
    print("  Código de departamento:", vacante.ubicacion.getcodDepartmento())
    print("  Código de municipio:", vacante.ubicacion.getcodMunicipio())
    print("  Nombre de departamento:", vacante.ubicacion.getnombreDepartamento())
    print("  Nombre de municipio:", vacante.ubicacion.getnombreMunicipio())
    print("Ocupación:")
    print("  Código:", vacante.ocupacion.getcodigo())
    print("  Nombre:", vacante.ocupacion.getnombre())
    print("  Descripción:", vacante.ocupacion.getdescripcion())

empresa_creada = crear_empresa()
crear_vacante(empresa_creada)

input("Presiona Enter para salir...")
