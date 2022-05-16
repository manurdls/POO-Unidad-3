import numpy as np

from claseEquipo import Equipo

class ManejadorEquipos(object):
    __equipos: np.array
    __dimension: int
    __incremento: int
    __cantidad: int

    def __init__(self, dim=5, inc=5):
        self._validar_entero(dim)
        self._validar_entero(inc)

        self.__equipos = np.empty(dim, dtype=Equipo)
        self.__dimension = dim
        self.__incremento = inc
        self.__cantidad = 0

    def _validar_entero(self, dato):
        if type(dato) != int:
            raise TypeError('Se espera una cadena')

    def _validar_equipo(self, dato):
        if type(dato) != Equipo:
            raise TypeError('Se espera un Equipo')

    def _hay_equipos(self):
        return self.__cantidad != 0

    def agregarEquipo(self, equipo):
        self._validar_equipo(equipo)

        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__equipos.resize(self.__dimension)
        self.__equipos[self.__cantidad] = equipo
        self.__cantidad += 1

    def mostrarEquipos(self):
        for i in range(self.__cantidad):
            print(self.__equipos[i])

    def buscarEquipo(self, nombre) -> int:
        retorno = None
        if self._hay_equipos():
            band = False
            i = 0
            while not band and i < self.__cantidad:
                equipo = self.__equipos[i]
                if equipo.getNombre().lower() == nombre.lower():
                    retorno = i
                    band = True
                i += 1
        if not band:
            print("Equipo '{}' no encontrado...".format(nombre))
        return retorno

    def getEquipo(self, indice) -> Equipo:
        return self.__equipos[indice]