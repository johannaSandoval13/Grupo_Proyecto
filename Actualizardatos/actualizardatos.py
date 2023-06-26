from Empresa import *
from Persona import *
from Usuario import *

def ingresar_informacion():
    tipo_usuario = input("Eres una empresa o una persona? (empresa/persona): ")
    if tipo_usuario.lower() == "empresa":
        rLegal = input("Ingrese el nombre del representante legal: ")
        nTrabajadores = input("Ingrese el número de trabajadores: ")
        aEconomica = input("Ingrese la actividad económica: ")
        documento = input("Ingrese el número de documento: ")
        correo = input("Ingrese el correo electrónico: ")
        contraseña = input("Ingrese la contraseña: ")
        empresa = Empresa(rLegal, nTrabajadores, aEconomica, documento, correo, contraseña)
        mostrar_informacion(empresa)
        while True:
            actualizar = input("¿Desea actualizar la información? (si/no): ")
            if actualizar.lower() == "si":
                opcion = input("¿Qué información desea actualizar? (rLegal/nTrabajadores/documento/correo/contraseña): ")
                if opcion.lower() == "rlegal":
                    nuevo_rlegal = input("Ingrese el nuevo nombre del representante legal: ")
                    empresa.setrLegal(nuevo_rlegal)
                elif opcion.lower() == "ntrabajadores":
                    nuevo_ntrabajadores = input("Ingrese el nuevo número de trabajadores: ")
                    empresa.setnTrabajadores(nuevo_ntrabajadores)
                elif opcion.lower() == "documento":
                    print("No se puede actualizar el documento de una empresa.")
                elif opcion.lower() == "correo":
                    nuevo_correo = input("Ingrese el nuevo correo electrónico: ")
                    empresa.setCorreo(nuevo_correo)
                elif opcion.lower() == "contraseña":
                    nueva_contraseña = input("Ingrese la nueva contraseña: ")
                    empresa.setContraseña(nueva_contraseña)
                else:
                    print("Opción inválida.")
                
                mostrar_informacion(empresa)
            else:
                break
    
    elif tipo_usuario.lower() == "persona":
        documento = input("Ingrese el número de documento: ")
        correo = input("Ingrese el correo electrónico: ")
        contraseña = input("Ingrese la contraseña: ")
        persona = Usuario(documento, correo, contraseña)
        mostrar_informacion(persona)
        while True:
            actualizar = input("¿Desea actualizar la información? (si/no): ")
            if actualizar.lower() == "si":
                opcion = input("¿Qué información desea actualizar? (documento/correo/contraseña): ")
                if opcion.lower() == "documento":
                    print("No se puede actualizar el documento de una persona.")
                elif opcion.lower() == "correo":
                    nuevo_correo = input("Ingrese el nuevo correo electrónico: ")
                    persona.setCorreo(nuevo_correo)
                elif opcion.lower() == "contraseña":
                    nueva_contraseña = input("Ingrese la nueva contraseña: ")
                    persona.setContraseña(nueva_contraseña)
                else:
                    print("Opción inválida.")
                
                mostrar_informacion(persona)
            else:
                break
    else:
        print("Por favor, seleccione 'empresa' o 'persona'.")
        ingresar_informacion()

def mostrar_informacion(usuario):
    if isinstance(usuario, Empresa):
        print("->Información de la empresa:")
        print("Representante Legal:", usuario.getrLegal())
        print("Número de Trabajadores:", usuario.getnTrabajadores())
        print("Actividad Económica:", usuario.getaEconomica())
        print("Documento:", usuario.getDocumento())
        print("Correo:", usuario.getCorreo())
        print("Contraseña:", usuario.getContraseña())
        print()
    elif isinstance(usuario, Usuario):
        print("->Información de la persona:")
        print("Documento:", usuario.getDocumento())
        print("Correo:", usuario.getCorreo())
        print("Contraseña:", usuario.getContraseña())
        print()
        
ingresar_informacion()
input("Presiona Enter para salir...")