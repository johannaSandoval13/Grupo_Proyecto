from actualizar_datos.actualizarDatos import actualizarDatos
from crearofertas.crearOferta import crearOferta
from actualizar_datos.Empresa import *

def mostrar_menu():
    print("Bienvenido al programa")
    print("Seleccione una opción:")
    print("1. Actualizar datos")
    print("2. Crear ofertas")
    print("3. Salir")

def ejecutar_opcion(opcion):
    if opcion == "1":
        actualizarDatos()
    elif opcion == "2":
        crearOferta()
    elif opcion == "3":
        print("¡Hasta luego!")
        exit()
    else:
        print("Opción invalida")
while True:
    mostrar_menu()
    opcion = input("Ingrese el número de la opción: ")
    ejecutar_opcion(opcion)