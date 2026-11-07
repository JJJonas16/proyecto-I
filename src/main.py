import configuracion
import validaciones
import os


def main():
    while True:
        os.system('cls')

        configuracion.Bienvenida()

        NombrePlanta=configuracion.PedirNombrePlanta()

        NombreSupervisor=configuracion.PedirNombreSupervisor()

        Escenario=configuracion.PedirEscenario()

        if validaciones.confirmar("Desea iniciar la simulacion?"):
            Simulacion()
        else:
            print("fin simulacion")
            break

def Simulacion():
    print("iniciando simulacion")

           







if __name__ == "__main__":
    main()