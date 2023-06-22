from Oferta import *
from Ocupacion import *

oferta1 = Oferta("2281","Técnicos en tecnologías de la información","Monitorear sistema de seguridad de la información y las comunicaciones según modelo y estándares técnicos.",
                "Comunicacion asertiva","12Meses","2","Indefinido","Completa","1.496.000","31/02/2030")
oferta2 = Oferta("8374","Mecanicos de aviacion","Reparar y revisar los sistemas estructurales: mecánico e hidráulico",
                "Mantenimiento de Equipos","38Meses","1","Fijo","Completa","2.300.000","31/02/2030")
oferta3 = Oferta("5131","Productores, directores artísticos y ocupaciones relacionadas","Diseñar ambientes de grabación de acuerdo con las especificaciones del libreto",
                "Gestión del Tiempo","6Meses","8","Teletrabajo","Completa","1.200.000","31/02/2030")


print("Escriba un numero:")
print("1.Técnicos en tecnologías de la información")
print("2.Mecanicos de aviacion")
print("3.Productores, directores artísticos y ocupaciones relacionadas")

opcion = input("Ingrese el número de a ver: ")

if opcion == "1":
    print("Información de Técnicos en tecnologías de la información:")
    print("Código:", oferta1.codigo)
    print("Nombre:", oferta1.nombre)
    print("Funciones:", oferta1.funciones)
    print("Habilidades:", oferta1.habilidades)
    print("Experiencia requerida:", oferta1.exp)
    print("Número de vacantes:", oferta1.nVacantes)
    print("Tipo de contrato:", oferta1.contrato)
    print("Jornada laboral:", oferta1.jornada)
    print("Salario:", oferta1.salario)
    print("Fecha de cierre:", oferta1.fCierre)
elif opcion == "2":
    print("Información de Mecanicos de aviacion:")
    print("Código:", oferta2.codigo)
    print("Nombre:", oferta2.nombre)
    print("Funciones:", oferta2.funciones)
    print("Habilidades:", oferta2.habilidades)
    print("Experiencia requerida:", oferta2.exp)
    print("Número de vacantes:", oferta2.nVacantes)
    print("Tipo de contrato:", oferta2.contrato)
    print("Jornada laboral:", oferta2.jornada)
    print("Salario:", oferta2.salario)
    print("Fecha de cierre:", oferta2.fCierre)
elif opcion == "3":
    print("Información de Productores, directores artísticos y ocupaciones relacionadas:")
    print("Código:", oferta3.codigo)
    print("Nombre:", oferta3.nombre)
    print("Funciones:", oferta3.funciones)
    print("Habilidades:", oferta3.habilidades)
    print("Experiencia requerida:", oferta3.exp)
    print("Número de vacantes:", oferta3.nVacantes)
    print("Tipo de contrato:", oferta3.contrato)
    print("Jornada laboral:", oferta3.jornada)
    print("Salario:", oferta3.salario)
    print("Fecha de cierre:", oferta3.fCierre)
else:
    print("Opción no valida.")
