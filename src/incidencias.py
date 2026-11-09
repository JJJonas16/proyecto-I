import random


def sale_incidencia(prob):
    numero = random.randint(1, 100)
    return numero <= prob


def escoger_incidencia():
    return random.randint(1, 4)


def mostrar_evento(codigo):
    print("")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    if codigo == 1:
        print("  INCIDENCIA: FALLA DE LA LLENADORA")
        print("  La llenadora se detuvo por una averia.")
        print("  1) Reparar de inmediato: -2 horas, -$500, +40 estado.")
        print("  2) Continuar produciendo: -10 estado, +5 % defectos.")
        print("  3) Correctivo programado: -3 horas, -$350, +25 estado.")
    elif codigo == 2:
        print("  INCIDENCIA: CONTAMINACION MICROBIOLOGICA")
        print("  El laboratorio detecto un resultado fuera de norma.")
        print("  1) Reprocesar el lote: -1 hora, -$150, +1 % defectos.")
        print("  2) Descartar el lote: -$200, +6 % defectos.")
        print("  3) Revisar y continuar: -0,5 horas, -$80, +3 % defectos.")
    elif codigo == 3:
        print("  INCIDENCIA: SENSOR DE LLENADO DESCALIBRADO")
        print("  Los botellones no se llenan con la cantidad exacta.")
        print("  1) Recalibrar el sensor: -1 hora, -$100.")
        print("  2) Continuar: +6 % defectos.")
        print("  3) Cambiar el sensor: -2 horas, -$250, +10 estado.")
    else:
        print("  INCIDENCIA: CORTE ELECTRICO")
        print("  Un corte de energia detuvo la linea de llenado.")
        print("  1) Usar el generador: -0,5 horas, -$180, -3 estado.")
        print("  2) Esperar la reparacion: -3 horas.")
        print("  3) Adelantar el preventivo: -2 horas, -$200, +15 estado.")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
