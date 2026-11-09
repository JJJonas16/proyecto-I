import configuracion
import validaciones


def pedir_agua(agua_actual, recomendado):
    # cuanto espacio queda en el tanque
    espacio = int(configuracion.TANQUE - agua_actual)
    print("")
    if espacio <= 0:
        print("  el tanque esta lleno")
        return 0.0
    print("  precio del agua: $" + str(configuracion.PRECIO_AGUA) + " el litro")
    print("  espacio en el tanque:", espacio, "L")
    print("  recomendado comprar:", recomendado, "L")
    return float(validaciones.pedir_numero("  Litros a comprar: ", 0, espacio))


def pedir_botellones(recomendado):
    print("")
    print("  precio del botellon vacio: $" + str(configuracion.PRECIO_BOTELLON))
    print("  recomendado comprar:", recomendado, "botellones")
    return validaciones.pedir_numero("  Botellones a comprar: ", 0, 500)


def mantenimiento(maquina):
    print("")
    print("------------------------------------------------------")
    print("MANTENIMIENTO PREVENTIVO")
    print("  estado de la maquina:", maquina, "%")
    if maquina < 60:
        print("  ojo: la maquina esta muy desgastada")
    print("  costo: $" + str(configuracion.COSTO_MANT))
    print("  tiempo:", configuracion.HORAS_MANT, "horas")
    print("  recupera:", configuracion.BONO_MANT, "puntos de estado")
    print("------------------------------------------------------")
    return validaciones.preguntar("  ¿Desea realizar el mantenimiento?")
