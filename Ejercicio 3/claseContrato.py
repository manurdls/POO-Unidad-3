from datetime import datetime

from claseJugador import Jugador

from claseEquipo import Equipo

class Contrato(object):
    __fecha_inicio: str
    __fecha_fin: str
    __pago_mensual: int
    __jugador: Jugador
    __equipo: Equipo

    def __init__(self, fecha_i, fecha_f, pago, jugador, equipo):
        self._validar_fecha(fecha_i)
        self._validar_fecha(fecha_f)
        self._validar_flotante(pago)
        self._validar_jugador(jugador)
        self._validar_equipo(equipo)

        self.__fecha_inicio = fecha_i
        self.__fecha_fin = fecha_f
        self.__pago_mensual = pago
        self.__jugador = jugador
        self.__jugador.agregarContrato(self)
        self.__equipo = equipo
        self.__equipo.agregarContrato(self)


    def __str__(self):
        fecha_inicio = str(self.__fecha_inicio.day) + '/' + str(self.__fecha_inicio.month) + '/' + str(self.__fecha_inicio.year)
        fecha_fin = str(self.__fecha_fin.day) + '/' + str(self.__fecha_fin.month) + '/' + str(self.__fecha_fin.year)
        return 'Jugador: [{}]\nEquipo: [{}]\nContrato: {} ~ {}\nSueldo: {}'.format(self.__jugador,
                                                                                self.__equipo,
                                                                                fecha_inicio,
                                                                                fecha_fin,
                                                                                self.__pago_mensual
                                                                                )

    def _validar_fecha(self, dato):
        if type(dato) != datetime:
            raise TypeError('Se esperaba una Fecha')
    
    def _validar_flotante(self, dato):
        if type(dato) != float:
            raise TypeError('Se esperaba un numero en Punto Flotante (numero real)')

    def _validar_jugador(self, dato):
        if type(dato) != Jugador:
            raise TypeError('Se esperaba un Jugador')

    def _validar_equipo(self, dato):
        if type(dato) != Equipo:
            raise TypeError('Se esperaba un Equipo')
    
    def getFechaInicio(self):
        return self.__fecha_inicio

    def getFechaFin(self):
        return self.__fecha_fin

    def getPagoMensual(self):
        return self.__pago_mensual

    def getJugador(self):
        return self.__jugador

    def getEquipo(self):
        return self.__equipo