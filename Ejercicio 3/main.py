import csv, os

from datetime import datetime

from claseContrato import Contrato, Jugador, Equipo

from claseManejadorEquipos import ManejadorEquipos

from claseManejadorJugadores import ManejadorJugadores

from claseManejadorContratos import ManejadorContratos

from claseMenu import Menu

def test():
    unJugador = Jugador('38409657', 'Manuel Cruz Rossi de los Santos', 'Cordoba', 'Argentina', '11/08/1994')
    #print(unJugador)

    unEquipo = Equipo('El Lobito', 'Jachal')
    #print(unEquipo)

    unContrato = Contrato('15/05/2022', '15/05/2025', 2000000, unJugador, unEquipo)
    print(unContrato)

def cargar_datos_equipos() -> ManejadorEquipos:
    archivo = open('Equipos.csv')
    reader = csv.reader(archivo, delimiter=';')
    linea = next(reader)
    cant_equipos = int(linea[0])
    equipos = ManejadorEquipos(cant_equipos)
    for i in range(cant_equipos):
        linea = next(reader)
        equipos.agregarEquipo(Equipo(linea[0], linea[1]))
    archivo.close()
    return equipos

def cargar_datos_jugadores() -> ManejadorJugadores:
    jugadores = ManejadorJugadores()
    archivo = open('Jugadores.csv')
    reader = csv.reader(archivo, delimiter=';')
    for linea in reader:
        jugadores.agregarJugador(Jugador(linea[0], linea[1], linea[2], linea[3], datetime.strptime(linea[4], "%d/%m/%Y")))
    archivo.close()
    return jugadores

def menu(equipos, jugadores, contratos):
    os.system('cls')
    menu = Menu(equipos, jugadores, contratos)
    exit = False
    while not exit:
        print("----------------------MENU----------------------\n"
              "1.Crear un contrato para un jugador en un equipo\n"
              "2.Consultar jugadores Contratados\n"
              "3.Consultar Contratos\n"
              "4.Obtener importe de contratos\n"
              "5.Guardar Contratos\n"
              "0.Salir")
        opt = input('Ingrese una opcion: ')
        os.system('cls')
        print('---------------------------------------------------------------------------------------------')
        print("***IMPORTANTE*** USTED PUEDE CANCELAR LA OPERACION EN CUALQUIER MOMENTO SI INGRESA 'cancelar'")
        print('---------------------------------------------------------------------------------------------')
        if opt.lower() == 'cancelar':
            opt = 0
        else:
            opt = int(opt)
        menu.option(opt)
        exit = opt==0

if __name__ == '__main__':
    #test()
    equipos = cargar_datos_equipos()
    #equipos.mostrarEquipos()
    jugadores = cargar_datos_jugadores()
    #jugadores.mostrarJugadores()
    contratos = ManejadorContratos()
    menu(equipos, jugadores, contratos)