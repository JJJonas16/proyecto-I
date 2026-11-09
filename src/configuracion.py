import validaciones

# capacidad de la planta
CAPACIDAD = 150       # botellones por hora
LITROS = 19           # litros de un botellon
TANQUE = 35000        # litros que caben en el tanque
JORNADAS = 5
ESTADO_MIN = 20       # por debajo de esto la maquina no trabaja

# precios en dolares
PRECIO_AGUA = 0.03
PRECIO_BOTELLON = 6.00
COSTO_HORA = 40.00
COSTO_PERDIDA = 25.00
COSTO_DEFECTO = 1.50
COSTO_MANT = 200.00
HORAS_MANT = 1.5
BONO_MANT = 25
COSTO_REPARACION = 500.00

# cosas del proceso
DERRAME = 0.005
RETORNO = 0.85

# notas para evaluar
CALIDAD_OK = 95
CALIDAD_MEDIA = 90
CUMPLIMIENTO_OK = 95
CUMPLIMIENTO_MEDIO = 80
EFICIENCIA_OK = 70
EFICIENCIA_MEDIA = 55
DESPERDICIO_OK = 5
DESPERDICIO_ALTO = 10


def inicio():
    print("")
    print("planta de gestion de agua")
    print("--------------------------------------------")
    print("Botellones de agua 19L")
    print("--------------------------------------------")
    print("usted es el supervisor")
    print("se van a realizar 5 jornadas de produccion")
    print("--------------------------------------------")


def nombre_planta():
    return validaciones.pedir_texto("ingrese nombre de la planta: ")


def nombre_supervisor():
    return validaciones.pedir_texto("ingrese nombre del supervisor: ")


def pedir_escenario():
    print("")
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
    return validaciones.pedir_numero("Seleccione un escenario (1-3): ", 1, 3)
