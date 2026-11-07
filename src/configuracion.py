import validaciones

def Bienvenida():
    print()
    print("planta de gestion de agua")
    print("--------------------------------------------")
    print("Botellones de agua 19L")
    print("--------------------------------------------")
    print("usted es el supervisor")
    print("se van a realizar 5 jornadas de produccion")
    print("--------------------------------------------")

def PedirNombrePlanta():
    return validaciones.leer_texto("ingrese nombre de la planta: ")

def PedirNombreSupervisor():
    return validaciones.leer_texto("ingrese nombre del supervisor: ")

def  PedirEscenario():

    print()
    print("------------------------------------------------------")
    print("ESCENARIOS DE PRODUCCION")
    print("------------------------------------------------------")
    print("1) Produccion estable")
    print("   Demanda de 900 botellones por jornada.")
    print("2) Alta demanda")
    print("   Demanda de 1.100 botellones por jornada.")
    print("3) Produccion critica")
    print("   Solo 6 horas, maquina desgastada y pocos recursos.")
    print("------------------------------------------------------")
    return validaciones.leer_entero("Seleccione un escenario (1-3): ", 1, 3)


