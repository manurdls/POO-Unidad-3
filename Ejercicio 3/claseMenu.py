from datetime import datetime

import os

from claseManejadorEquipos import ManejadorEquipos

from claseManejadorJugadores import ManejadorJugadores

from claseManejadorContratos import ManejadorContratos

from claseContrato import Contrato

class Menu(object):
    __switcher: dict
    __equipos: ManejadorEquipos
    __jugadores: ManejadorJugadores
    __contratos: ManejadorContratos

    def __init__(self, equipos, jugadores, contratos):
        self.__switcher = {0:self.salir,
                           1:self.inciso1,
                           2:self.inciso2,
                           3:self.inciso3,
                           4:self.inciso4,
                           5:self.inciso5,
                           }
        self.__equipos = equipos
        self.__jugadores = jugadores
        self.__contratos = contratos

    def getSwitcher(self):
        return self.__switcher

    def option(self, op):
        func = self.__switcher.get(op, lambda: print("Opción no válida"))
        func()

    def salir(self):
        print('Fin Programa')

    def inciso1(self):
        dni_jugador = self._ingresar_dni()
        if dni_jugador:
            nombre_equipo = self._ingresar_cadena()
            if nombre_equipo:
                indice_jugador = self.__jugadores.buscarJugador(dni_jugador)
                indice_equipo = self.__equipos.buscarEquipo(nombre_equipo)
                if indice_jugador != None and indice_equipo != None:
                    jugador = self.__jugadores.getJugador(indice_jugador)
                    equipo = self.__equipos.getEquipo(indice_equipo)
                    if not self.__contratos.comprobar_si_hay_contrato(jugador, equipo):
                        fecha_inicio = self._ingresar_fecha('Ingrese la fecha de Inicio del contrato: ')
                        if fecha_inicio:
                            fecha_fin = self._ingresar_fecha('Ingrese la fecha de Finalizacion del contrato: ')
                            if fecha_fin:
                                pago_mensual = self._ingresar_monto()
                                if pago_mensual:
                                    contrato = Contrato(fecha_inicio, fecha_fin, pago_mensual, jugador, equipo)
                                    self.__contratos.agregarContrato(contrato)
                                    del contrato
                                    os.system('cls')
                                    print('El contrato se agregó correctamente...')
                    else: print('Al parecer está intentando agregar un contrato que incluye a un Jugador y un Equipo que ya \nestan vinculados por un contrato. Recuerde que este algoritmo implementa una Clase Asociacion \ny no un Clase que Modela una Asociacion.')

    def inciso2(self):
        dni_jugador = self._ingresar_dni()
        if dni_jugador:
            indice_jugador = self.__jugadores.buscarJugador(dni_jugador)
            if indice_jugador != None:
                jugador = self.__jugadores.getJugador(indice_jugador)
                self.__contratos.consultar_jugador_contratado(jugador)
                del jugador


    def inciso3(self):
        nombre_equipo = self._ingresar_cadena()
        if nombre_equipo:
            indice_equipo = self.__equipos.buscarEquipo(nombre_equipo)
            if indice_equipo != None:
                equipo = self.__equipos.getEquipo(indice_equipo)
                self.__contratos.consultar_contratos_de_un_equipo(equipo)
                del equipo

    def inciso4(self):
        nombre_equipo = self._ingresar_cadena()
        if nombre_equipo:
            indice_equipo = self.__equipos.buscarEquipo(nombre_equipo)
            if indice_equipo != None:
                equipo = self.__equipos.getEquipo(indice_equipo)
                self.__contratos.obtener_importe_de_contratos(equipo)
                del equipo

    def inciso5(self):
        pass

    def _ingresar_dni(self) -> int:
        dni = None
        band = False
        mensaje_error = 'Error: se esperaba un DNI Valido'
        while not band:
            entrada = input('Ingrese el dni del jugador: ')
            try:
                entrada = int(entrada)
                assert entrada > 0,mensaje_error
                entrada = str(entrada)
                assert len(entrada) == 8,mensaje_error
            except ValueError:
                if entrada.lower() == 'cancelar': band = True
                else: print(mensaje_error)
            except AssertionError as error:
                print(error)
            else:
                dni = entrada
                band = True
        return dni


    def _ingresar_cadena(self) -> str:
        cadena = None
        band = False
        while not band:
            entrada = input('Ingrese el nombre del club: ')
            try:
                entrada = int(entrada)
            except ValueError:
                if entrada.lower() != 'cancelar': cadena = entrada
                band = True
            else:
                print('Error: se esperaba una Cadena')
        return cadena

    def _ingresar_fecha(self, texto) -> datetime:
        fecha = None
        band = False
        while not band:
            entrada = input(texto)
            try:
                entrada = datetime.strptime(entrada, "%d/%m/%Y")
            except Exception:
                if entrada.lower() == 'cancelar': band = True
                else: print('Error: el formato valido para una Fecha es dd/mm/aaaa')
            else:
                fecha = entrada
                band = True
        return fecha

    def _ingresar_monto(self) -> float:
        monto = None
        band = False
        mensaje_error = 'Error: se esperaba un monto Valido. Esto es, un numero Real positivo'
        while not band:
            entrada = input('Ingrese el monto mensual que gana el jugador: ')
            try:
                entrada = float(entrada)
                assert entrada > 0,mensaje_error
            except ValueError:
                if entrada.lower() == 'cancelar': band = True
                else: print(mensaje_error)
            except AssertionError as error:
                print(error)
            else:
                monto = entrada
                band = True
        return monto
