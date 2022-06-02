from zope.interface import implementer

from claseInterface import Interface

from claseAparatoElectronico import AparatoElectronico

class Nodo(object):
    __aparato_electronico = None
    __siguiente = None

    def __init__(self, aparato):
        self._validar_aparato_electronico(aparato)

        self.__aparato_electronico = aparato
        self.__siguiente = None

    def _validar_aparato_electronico(dato):
        if not isinstance(dato, AparatoElectronico):
            raise TypeError('Se esperaba un objeto derivado de AparatoElectronico')

    def _validar_nodo(dato):
        if type(dato) != Nodo:
            raise TypeError('Se esperaba un objeto de tipo Nodo')

    def set_siguiente(self, siguiente):
        self._validar_nodo(siguiente)

        self.__siguiente = siguiente

    def get_siguiente(self):
        return self.__siguiente

    def get_dato(self):
        return self.__aparato_electronico

@implementer(Interface)
class Lista(object):
    __comienzo = None
    __final = None
    __actual = None
    __indice = 0
    __tope = 0

    def __init__(self):
        self.__comienzo = None
        self.__final = None
        self.__actual = None
        self.__indice = 0
        self.__tope = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice += 1
            dato = self.__actual.get_dato()
            self.__actual = self.__actual.getSiguiente()
            return dato
    
    def agregarElemento(self, aparato_electronico):
        nodo = Nodo(aparato_electronico)
        if self.__comienzo == None:
            self.__comienzo = nodo
            self.__actual = nodo
            self.__final = nodo
        else:
            self.__final.get_siguiente(nodo)
        self.__tope += 1

    def insertarElemento(self, aparato_electronico, posicion):
        print('Falta')

    def mostrarElemento(self, posicion):
        print('Falta')
