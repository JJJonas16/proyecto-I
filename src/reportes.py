import configuracion


def panel(planta, supervisor, esc, dia, agua, botellones, maquina, horas, costo, total):
    print("")
    print("======================================================")
    print("PLANTA:", planta)
    print("SUPERVISOR:", supervisor)
    print("ESCENARIO:", esc)
    print("JORNADA", dia, "DE", configuracion.JORNADAS)
    print("------------------------------------------------------")
    print("Agua cruda:", round(agua), "L")
    print("Botellones vacios:", botellones)
    print("Estado de la maquina:", maquina, "%")
    print("Horas disponibles:", round(horas, 1))
    print("Costo de la jornada: $" + str(round(costo, 2)))
    print("Costo acumulado: $" + str(round(total, 2)))
    print("======================================================")


def reporte(dia, plan, producidos, defectuosos, agua_usada,
            calidad, cumplimiento, eficiencia, desperdicio,
            desperdicio_pct, horas_usadas, horas_perdidas,
            costo, estado):
    print("")
    print("------------------------------------------------------")
    print("RESULTADOS DE LA JORNADA", dia)
    print("------------------------------------------------------")
    print("Produccion planificada:", plan, "botellones")
    print("Produccion realizada:", producidos, "botellones")
    print("Botellones defectuosos:", defectuosos)
    print("Agua cruda consumida:", round(agua_usada), "L")
    print("Calidad:", round(calidad, 1), "%")
    print("Cumplimiento:", round(cumplimiento, 1), "%")
    print("Eficiencia:", round(eficiencia, 1), "%")
    print("Desperdicio:", round(desperdicio), "L (" + str(round(desperdicio_pct, 1)) + " %)")
    print("Horas utilizadas:", round(horas_usadas, 1))
    print("Horas perdidas:", round(horas_perdidas, 1))
    print("Costo de la jornada: $" + str(round(costo, 2)))
    print("------------------------------------------------------")
    print("ESTADO:", estado)
    print("------------------------------------------------------")


def informe(planta, supervisor, esc, tot_plan, tot_real, pendiente,
            tot_def, tot_desperdicio, desperdicio_pct,
            tot_agua, tot_horas, tot_perdidas,
            calidad, eficiencia, cumplimiento, tot_costo, final):
    print("")
    print("======================================================")
    print("INFORME FINAL DE LA SIMULACION")
    print("======================================================")
    print("Planta:", planta)
    print("Supervisor:", supervisor)
    print("Escenario:", esc)
    print("------------------------------------------------------")
    print("Produccion total planificada:", tot_plan, "botellones")
    print("Produccion total realizada:", tot_real, "botellones")
    print("Produccion pendiente:", pendiente, "botellones")
    print("Total de defectuosos:", tot_def, "botellones")
    print("Desperdicio acumulado:", round(tot_desperdicio), "L ("
          + str(round(desperdicio_pct, 1)) + " %)")
    print("Agua cruda consumida:", round(tot_agua), "L")
    print("Horas utilizadas:", round(tot_horas, 1))
    print("Horas perdidas:", round(tot_perdidas, 1))
    print("Cumplimiento global:", round(cumplimiento, 1), "%")
    print("Calidad final:", round(calidad, 1), "%")
    print("Eficiencia final:", round(eficiencia, 1), "%")
    print("Costo acumulado: $" + str(round(tot_costo, 2)))
    print("------------------------------------------------------")
    print("RESULTADO:", final)
    print("======================================================")


def resultado(cumplimiento, calidad, dias_sin_recursos, tot_real):
    if tot_real <= 0:
        return "PLAN DE PRODUCCION NO CUMPLIDO"
    if calidad < configuracion.CALIDAD_MEDIA:
        return "RESULTADO CRITICO POR CALIDAD"
    if dias_sin_recursos >= 2:
        return "RESULTADO CRITICO POR FALTA DE RECURSOS"
    if cumplimiento >= configuracion.CUMPLIMIENTO_OK:
        if calidad >= configuracion.CALIDAD_OK:
            return "PLAN DE PRODUCCION CUMPLIDO"
    if cumplimiento >= configuracion.CUMPLIMIENTO_MEDIO:
        return "CUMPLIMIENTO PARCIAL DEL PLAN"
    return "PLAN DE PRODUCCION NO CUMPLIDO"
