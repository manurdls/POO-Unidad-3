import numpy as np

from datetime import datetime, timedelta

from claseContrato import Contrato

class ManejadorContratos(object):
    __contratos: np.array
    __dimension: int
    __incremento: int
    __cantidad: int

    def __init__(self, dim=5, inc=5):
        self._validar_entero(dim)
        self._validar_entero(inc)

        self.__contratos = np.empty(dim, dtype=Contrato)
        self.__dimension = dim
        self.__incremento = inc
        self.__cantidad = 0

    def _validar_entero(self, dato):
        if type(dato) != int:
            raise TypeError('Se espera una cadena')

    def _validar_contrato(self, dato):
        if type(dato) != Contrato:
            raise TypeError('Se espera un Contrato')

    def _es_vigente(self, contrato) -> bool:
        retorno = False
        fecha_actual = datetime.today()
        fecha_inicio = contrato.getFechaInicio()
        fecha_fin = contrato.getFechaFin()
        if fecha_inicio < fecha_actual and fecha_fin > fecha_actual:
            retorno = True
        return retorno

    def _buscar_contrato_vigente(self, jugador):
        retorno = None
        contratos = jugador.getContratos()
        if not contratos:
            print("'{}' aún no tiene registro de contratos...".format(jugador.getNombre()))
        else:
            band = False
            i = 0
            while not band and i < len(contratos):
                contrato = contratos[i]
                if self._es_vigente(contrato):
                    retorno = i
                    band = True
                i += 1
        return retorno

        """
        retorno = None
        band = False
        i = 0
        while not band and i < self.__cantidad:
            contrato = self.__contratos[i]
            if contrato.getJugador() == jugador:
                if self._es_vigente(contrato):
                    retorno = i
                    band = True
            i += 1
        return retorno
        """

    def agregarContrato(self, contrato):
        self._validar_contrato(contrato)

        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__contratos.resize(self.__dimension)
        self.__contratos[self.__cantidad] = contrato
        self.__cantidad += 1

    def mostrarContratos(self):
        for i in range(self.__cantidad):
            print(self.__contratos[i])

    def comprobar_si_hay_contrato(self, jugador, equipo) -> bool:
        retorno = False
        band = False
        i = 0
        while not band and i < self.__cantidad:
            if self.__contratos[i].getJugador() == jugador and self.__contratos[i].getEquipo() == equipo:
                band = True
            i += 1
        if band:
            retorno = band
        return retorno

    def consultar_jugador_contratado(self, jugador):
        indice_contrato = self._buscar_contrato_vigente(jugador)
        if indice_contrato == None:
            print("'{}' no posee contrato vigente..".format(jugador.getNombre()))
        else:
            contrato = self.__contratos[indice_contrato]
            equipo = contrato.getEquipo()
            fecha_fin = contrato.getFechaFin()
            fecha_fin = str(fecha_fin.day) + '/' + str(fecha_fin.month) + '/' + str(fecha_fin.year)
            print('Equipo: {} Fecha de finalizacion del contrato: {}'.format(equipo.getNombre().ljust(40), fecha_fin))

    def consultar_contratos_de_un_equipo(self, equipo):
        contratos = equipo.getContratos()
        if not contratos:
            print("'{}' aún no tiene registro de contratos...".format(equipo.getNombre()))
        else:
            hay_contratos_proximos_a_vencer = False
            for contrato in contratos:
                fecha_actual = datetime.today()
                dentro_de_seis_meses = fecha_actual + timedelta(days=365/2)
                fecha_fin = contrato.getFechaFin()
                if fecha_fin >= fecha_actual and fecha_fin <= dentro_de_seis_meses:
                    jugador = contrato.getJugador()
                    print("{} Nota: el contrato vence en '{}' mes/meses.".format(jugador, fecha_fin.month - fecha_actual.month))
                    hay_contratos_proximos_a_vencer = True
            if not hay_contratos_proximos_a_vencer: print("'{}' no posee contratos que venzan en los proximos 6 meses..".format(equipo.getNombre()))
        """
        hay_contratos = False
        for i in range(self.__cantidad):
            contrato = self.__contratos[i]
            if contrato.getEquipo() == equipo:
                fecha_actual = datetime.today()
                dentro_de_seis_meses = fecha_actual + timedelta(days=365/2)
                fecha_fin = contrato.getFechaFin()
                if fecha_fin >= fecha_actual and fecha_fin <= dentro_de_seis_meses:
                    jugador = contrato.getJugador()
                    print("{} Nota: el contrato vence en '{}' mes/meses.".format(jugador, fecha_fin.month - fecha_actual.month))
                    hay_contratos = True
        if not hay_contratos:
            print("'{}' no posee contratos que venzan en los proximos 6 meses..".format(equipo.getNombre()))
        """

    def obtener_importe_de_contratos(self, equipo):
        contratos = equipo.getContratos()
        if not contratos:
            print("'{}' aún no tiene registro de contratos...".format(equipo.getNombre()))
        else:
            importe_total = 0.0
            for contrato in contratos:
                if self._es_vigente(contrato):
                    importe_total += contrato.getPagoMensual()
            print("'{}' gasta por mes en contratos con sus jugadores {} pesos".format(equipo.getNombre(), importe_total))
