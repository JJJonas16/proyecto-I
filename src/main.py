# Proyecto I - Programacion I
# Simulador de la planta de botellones

import configuracion
import validaciones
import planificacion
import incidencias
import reportes


def main():
    :

        configuracion.inicio()

        planta = configuracion.nombre_planta()
        supervisor = configuracion.nombre_supervisor()
        esc = configuracion.pedir_escenario()

        if validaciones.preguntar("Desea iniciar la simulacion?"):
            simular(planta, supervisor, esc)
        else:
            print("fin simulacion")
            break


def simular(planta, supervisor, esc):
    # datos de cada escenario
    if esc == 1:
        nombre_esc = "Produccion estable"
        demanda = 900
        horas_base = 8.0
        maquina = 90
        agua = 28000.0
        botellones = 1200
        tasa_base = 0.02
        rend = 0.72
        prob = 50
    elif esc == 2:
        nombre_esc = "Alta demanda"
        demanda = 1100
        horas_base = 8.0
        maquina = 85
        agua = 24000.0
        botellones = 1000
        tasa_base = 0.03
        rend = 0.70
        prob = 75
    else:
        nombre_esc = "Produccion critica"
        demanda = 750
        horas_base = 6.0
        maquina = 70
        agua = 14000.0
        botellones = 600
        tasa_base = 0.05
        rend = 0.65
        prob = 95

    # aqui voy sumando los totales
    tot_plan = 0
    tot_real = 0
    tot_def = 0
    tot_desperdicio = 0.0
    tot_agua = 0.0
    tot_horas = 0.0
    tot_perdidas = 0.0
    tot_programadas = 0.0
    tot_costo = 0.0
    dias_sin_recursos = 0
    ayer = 0

    print("")
    print("======================================================")
    print("INICIO DE LA SIMULACION")
    print("Planta:", planta)
    print("Supervisor:", supervisor)
    print("Escenario:", nombre_esc)
    print("Demanda por jornada:", demanda, "botellones")
    print("======================================================")

    for dia in range(1, configuracion.JORNADAS + 1):
        horas = horas_base
        costo = 0.0
        producidos = 0
        defectuosos = 0
        agua_usada = 0.0
        desperdicio = 0.0
        horas_usadas = 0.0
        horas_perdidas = 0.0

        # vuelven los botellones
        if dia > 1:
            retorno = int(ayer * configuracion.RETORNO)
            botellones += retorno
            print("")
            print("Retornaron", retorno, "botellones vacios.")

        reportes.panel(planta, supervisor, nombre_esc, dia,
                       agua, botellones, maquina, horas,
                       costo, tot_costo)

        # mantenimiento
        if planificacion.mantenimiento(maquina):
            horas -= configuracion.HORAS_MANT
            costo += configuracion.COSTO_MANT
            maquina += configuracion.BONO_MANT
            if maquina > 100:
                maquina = 100
            print("Mantenimiento preventivo aplicado.")

        # mientras mas gastada la maquina, mas defectos salen
        tasa = tasa_base + ((100 - maquina) / 100) * 0.05
        if tasa > 0.25:
            tasa = 0.25

        # plan de la jornada
        print("")
        print("Demanda de la jornada:", demanda, "botellones")
        plan = validaciones.pedir_numero("Cantidad a producir: ", 0, 2000)

        # lo que hace falta para el plan
        agua_neces = plan * configuracion.LITROS / rend
        agua_comprar = agua_neces - agua
        if agua_comprar <= 0:
            agua_comprar = 0
        else:
            agua_comprar = int(agua_comprar) + 1

        bot_comprar = plan - botellones
        if bot_comprar < 0:
            bot_comprar = 0

        horas_neces = plan / (configuracion.CAPACIDAD * maquina / 100)

        print("")
        print("PLANIFICACION DE LA JORNADA")
        print("Cantidad a producir:", plan, "botellones")
        print("Agua: tiene", round(agua), "L | necesita", round(agua_neces),
              "L | recomendado comprar", agua_comprar, "L")
        print("Botellones: tiene", botellones, "| necesita", plan,
              "| recomendado comprar", bot_comprar)
        print("Horas: tiene", round(horas, 1), "h | necesita",
              round(horas_neces, 1), "h")

        if horas_neces > horas:
            print("ADVERTENCIA: faltan", round(horas_neces - horas, 1),
                  "horas. El plan se vera limitado.")

        # si no cabe en el tanque aviso
        espacio = configuracion.TANQUE - agua
        if agua_comprar > espacio:
            agua_comprar = int(espacio)
            print("ADVERTENCIA: el tanque no alcanza para todo el plan.")
            print("Plan maximo con el tanque lleno:",
                  int(configuracion.TANQUE * rend // configuracion.LITROS))

        if bot_comprar > 500:
            bot_comprar = 500
            print("ADVERTENCIA: solo puede comprar 500 botellones por jornada.")

        # compras
        litros = planificacion.pedir_agua(agua, agua_comprar)
        agua += litros
        costo += litros * configuracion.PRECIO_AGUA

        comprados = planificacion.pedir_botellones(bot_comprar)
        botellones += comprados
        costo += comprados * configuracion.PRECIO_BOTELLON

        # hasta donde se puede producir
        max_agua = int(agua * rend // configuracion.LITROS)
        max_maquina = int(configuracion.CAPACIDAD * maquina / 100 * horas)
        limite = plan
        if limite > max_agua:
            limite = max_agua
        if limite > max_maquina:
            limite = max_maquina
        if limite > botellones:
            limite = botellones
        if limite < 0:
            limite = 0
        print("Produccion maxima con los recursos actuales:", limite, "botellones.")
        if plan > limite:
            print("ADVERTENCIA: el plan de", plan, "supera el limite.")

        # sale una incidencia
        if incidencias.sale_incidencia(prob):
            codigo = incidencias.escoger_incidencia()
            incidencias.mostrar_evento(codigo)
            opcion = validaciones.pedir_numero("  Seleccione una opcion (1-3): ", 1, 3)

            # efectos de la decision
            if codigo == 1:
                if opcion == 1:
                    horas -= 2
                    costo += configuracion.COSTO_REPARACION
                    maquina += 40
                    print("Reparacion inmediata: -2 horas, -$500 y +40 estado.")
                elif opcion == 2:
                    maquina -= 10
                    tasa += 0.05
                    print("Sigue produciendo: -10 estado y +5 % defectos.")
                else:
                    horas -= 3
                    costo += 350
                    maquina += 25
                    print("Correctivo programado: -3 horas, -$350 y +25 estado.")
            elif codigo == 2:
                if opcion == 1:
                    horas -= 1
                    costo += 150
                    tasa += 0.01
                    print("Lote reprocesado: -1 hora, -$150 y +1 % defectos.")
                elif opcion == 2:
                    costo += 200
                    tasa += 0.06
                    print("Lote descartado: -$200 y +6 % defectos.")
                else:
                    horas -= 0.5
                    costo += 80
                    tasa += 0.03
                    print("Revision del proceso: -0,5 horas, -$80 y +3 % defectos.")
            elif codigo == 3:
                if opcion == 1:
                    horas -= 1
                    costo += 100
                    print("Sensor recalibrado: -1 hora y -$100.")
                elif opcion == 2:
                    tasa += 0.06
                    print("Se continua con el sensor: +6 % defectos.")
                else:
                    horas -= 2
                    costo += 250
                    maquina += 10
                    print("Sensor cambiado: -2 horas, -$250 y +10 estado.")
            else:
                if opcion == 1:
                    horas -= 0.5
                    costo += 180
                    maquina -= 3
                    print("Generador: -0,5 horas, -$180 y -3 estado.")
                elif opcion == 2:
                    horas -= 3
                    print("Espera: -3 horas.")
                else:
                    horas -= 2
                    costo += 200
                    maquina += 15
                    print("Preventivo adelantado: -2 horas, -$200 y +15 estado.")

            # que no queden valores raros
            if horas < 0:
                horas = 0
            if maquina < 1:
                maquina = 1
            if maquina > 100:
                maquina = 100
            if tasa > 0.25:
                tasa = 0.25

            reportes.panel(planta, supervisor, nombre_esc, dia,
                           agua, botellones, maquina, horas,
                           costo, tot_costo + costo)
        else:
            print("")
            print("No se presentaron incidencias en esta jornada.")

        # produccion
        max_agua = int(agua * rend // configuracion.LITROS)
        max_maquina = int(configuracion.CAPACIDAD * maquina / 100 * horas)
        max_bot = botellones

        if maquina < configuracion.ESTADO_MIN:
            print("La maquina esta fuera de servicio: no hay produccion.")
            producidos = 0
        else:
            producidos = plan
            if producidos > max_agua:
                producidos = max_agua
            if producidos > max_maquina:
                producidos = max_maquina
            if producidos > max_bot:
                producidos = max_bot
            if producidos < 0:
                producidos = 0

        # cuentas del dia
        agua_usada = producidos * configuracion.LITROS / rend
        defectuosos = round(producidos * tasa)
        desperdicio = defectuosos * configuracion.LITROS
        desperdicio += producidos * configuracion.LITROS * configuracion.DERRAME
        horas_usadas = producidos / (configuracion.CAPACIDAD * maquina / 100)
        if horas_usadas > horas:
            horas_usadas = horas
        horas_perdidas = horas_base - horas_usadas
        if horas_perdidas < 0:
            horas_perdidas = 0.0

        agua -= agua_usada
        if agua < 0:
            agua = 0.0
        botellones -= producidos
        if botellones < 0:
            botellones = 0
        maquina -= int(producidos / 300)
        if maquina < 1:
            maquina = 1

        costo += horas_usadas * configuracion.COSTO_HORA
        costo += horas_perdidas * configuracion.COSTO_PERDIDA
        costo += defectuosos * configuracion.COSTO_DEFECTO

        calidad = 0.0
        if producidos > 0:
            calidad = (producidos - defectuosos) / producidos * 100

        cumplimiento = 0.0
        if plan > 0:
            cumplimiento = producidos / plan * 100

        eficiencia = producidos / (configuracion.CAPACIDAD * horas_base) * 100

        desperdicio_pct = 0.0
        if producidos > 0:
            desperdicio_pct = desperdicio / (producidos * configuracion.LITROS) * 100

        # como quedo la jornada
        if cumplimiento < configuracion.CUMPLIMIENTO_MEDIO:
            estado = "JORNADA NO CUMPLIDA (produccion insuficiente)"
        elif calidad < configuracion.CALIDAD_MEDIA:
            estado = "JORNADA NO CUMPLIDA (calidad critica)"
        elif desperdicio_pct > configuracion.DESPERDICIO_ALTO:
            estado = "JORNADA NO CUMPLIDA (desperdicio excesivo)"
        elif eficiencia < configuracion.EFICIENCIA_MEDIA:
            estado = "JORNADA NO CUMPLIDA (eficiencia baja)"
        elif cumplimiento < configuracion.CUMPLIMIENTO_OK:
            estado = "JORNADA EN RIESGO (cumplimiento parcial)"
        elif calidad < configuracion.CALIDAD_OK:
            estado = "JORNADA EN RIESGO (calidad en atencion)"
        elif desperdicio_pct > configuracion.DESPERDICIO_OK:
            estado = "JORNADA EN RIESGO (desperdicio elevado)"
        elif eficiencia < configuracion.EFICIENCIA_OK:
            estado = "JORNADA EN RIESGO (eficiencia media)"
        else:
            estado = "JORNADA SUPERADA"

        # sumo para el informe
        tot_plan += plan
        tot_real += producidos
        tot_def += defectuosos
        tot_desperdicio += desperdicio
        tot_agua += agua_usada
        tot_horas += horas_usadas
        tot_perdidas += horas_perdidas
        tot_programadas += horas_base
        tot_costo += costo
        if producidos < plan:
            if max_agua < plan or max_bot < plan:
                dias_sin_recursos += 1
        ayer = producidos

        reportes.reporte(dia, plan, producidos, defectuosos, agua_usada,
                         calidad, cumplimiento, eficiencia, desperdicio,
                         desperdicio_pct, horas_usadas, horas_perdidas,
                         costo, estado)

        validaciones.pausa()

    # informe final
    pendiente = tot_plan - tot_real
    if pendiente < 0:
        pendiente = 0

    cumpl_global = 0.0
    if tot_plan > 0:
        cumpl_global = tot_real / tot_plan * 100

    calidad_global = 0.0
    if tot_real > 0:
        calidad_global = (tot_real - tot_def) / tot_real * 100

    eficiencia_global = tot_real / (configuracion.CAPACIDAD * tot_programadas) * 100

    desperdicio_global = 0.0
    if tot_real > 0:
        desperdicio_global = tot_desperdicio / (tot_real * configuracion.LITROS) * 100

    final = reportes.resultado(cumpl_global, calidad_global, dias_sin_recursos, tot_real)

    reportes.informe(planta, supervisor, nombre_esc,
                     tot_plan, tot_real, pendiente,
                     tot_def, tot_desperdicio, desperdicio_global,
                     tot_agua, tot_horas, tot_perdidas,
                     calidad_global, eficiencia_global, cumpl_global,
                     tot_costo, final)

    validaciones.pausa()


if __name__ == "__main__":
    main()
