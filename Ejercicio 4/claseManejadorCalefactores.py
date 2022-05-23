import numpy as np

from claseCalefactor import Calefactor

class ManejadorCalefactores(object):
    __calefactores: np.array
    __dimension: int
    __incremento: int
    __cantidad: int

    def __init__(self, dim, inc=5):
        self._validar_entero(dim)
        self._validar_entero(inc)

        self.__calefactores = np.empty(dim, dtype=Calefactor)
        self.__dimension = dim
        self.__incremento = inc
        self.__cantidad = 0

    def _validar_entero(self, dato):
        if type(dato) != int:
            raise TypeError('Se espera un entero')

    def _validar_calefactor(self, dato):
        if not isinstance(dato, Calefactor):
            raise TypeError('Se espera un Calefactor')

    def agregarCalefactor(self, calefactor):
        self._validar_calefactor(calefactor)

        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__calefactores.resize(self.__dimension)
        self.__calefactores[self.__cantidad] = calefactor
        self.__cantidad += 1

    def mostrarCalefactores(self):
        for i in range(self.__cantidad):
            print(self.__calefactores[i])

    def obtener_calefactor_gas_de_menor_consumo():
        pass

    def obtener_calefactor_electrico_de_menor_consumo():
        pass