import numpy as np

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