import numpy as np

from claseFlor import Flor

class ManejadorFlores(object):
    __flores: np
    __dimension: int
    __incremento: int
    __cantidad: int

    def __init__(self, dim=5, inc=5):
        self._validar_entero(dim)
        self._validar_entero(inc)
        
        self.__flores = np.empty(dim, dtype=Flor)
        self.__dimension = dim
        self.__incremento = inc
        self.__cantidad = 0

    def _validar_entero(self, dato):
        if type(dato) != int:
            raise TypeError('Se espera una cadena')

    def _validar_flor(self, dato):
        if type(dato) != Flor:
            raise TypeError('Se espera una Flor')

    def agregarFlor(self, flor):
        self._validar_flor(flor)

        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__flores.resize(self.__dimension)
        self.__flores[self.__cantidad] = flor
        self.__cantidad += 1
    
    def mostrarFlores(self):

        if self.__cantidad == 0:
            print('No hay flores registradas...')
        else:
            for i in range(self.__cantidad):
                print(self.__flores[i])

    def buscar_flores_nombre_y_color(self, nombre, color):
        indice = None
        band = False
        i = 0
        while not band and i < self.__cantidad:
            if self.__flores[i].getNombre() == nombre and self.__flores[i].getColor() == color:
                indice = i
                band = True
            i += 1
        return indice

    def getFlores(self, indice):
        retorno = None
        if indice >= 0 and indice <= self.__cantidad:
            retorno = self.__flores[indice]
        return retorno