from Usuario import *
from Empresa import *
from Persona import *

def ingresar_usuario():
    tipo_usuario = input("Eres una persona o una empresa? ")
    documento = input("Ingrese el documento: ")
    correo = input("Ingrese el correo: ")
    contraseña = input("Ingrese la contraseña: ")

    if tipo_usuario.lower() == "persona":
        pOcupacional = input("Ingrese la ocupación: ")
        estudios = input("Ingrese los estudios: ")
        exp = input("Ingrese la experiencia: ")
        usuario = Persona(pOcupacional, estudios, exp, documento, correo, contraseña)
    elif tipo_usuario.lower() == "empresa":
        rLegal = input("Ingrese el representante legal: ")
        nTrabajadores = input("Ingrese el número de trabajadores: ")
        aEconomica = input("Ingrese la actividad económica: ")
        usuario = Empresa(rLegal, nTrabajadores, aEconomica, documento, correo, contraseña)
    else:
        print("Opción inválida. Inténtalo nuevamente.")

    return usuario



nuevo_usuario = ingresar_usuario()

print("Este es el usuario creado")
print("Usuario creado:", type(nuevo_usuario).__name__)
print("Documento:", nuevo_usuario.getDocumento())
print("Correo:", nuevo_usuario.getCorreo())
print("Contraseña:", nuevo_usuario.getContraseña())


