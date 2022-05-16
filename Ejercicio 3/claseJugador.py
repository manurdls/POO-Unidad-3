from datetime import datetime

class Jugador(object):
    

    __dni: str
    __nombre: str
    __ciudad_natal: str
    __pais_origen: str
    __fecha_nacimiento: str
    __contratos: list

    def __init__(self, dni, nom, ciu, pais, fecha):
        self._validar_cadena(dni)
        self._validar_cadena(nom)
        self._validar_cadena(ciu)
        self._validar_cadena(pais)
        self._validar_fecha(fecha)

        self.__dni = dni
        self.__nombre = nom
        self.__ciudad_natal = ciu
        self.__pais_origen = pais
        self.__fecha_nacimiento = fecha
        self.__contratos = []

    def __str__(self):
        fecha_nacimiento = str(self.__fecha_nacimiento.day) + '/' + str(self.__fecha_nacimiento.month) + '/' + str(self.__fecha_nacimiento.year)
        return 'DNI: {} Nombre: {} Fecha de Nacimiento: {}'.format(self.__dni.ljust(10), self.__nombre.ljust(20), fecha_nacimiento)

    def _validar_cadena(self, dato):
        if type(dato) != str:
            raise TypeError('Se esperaba una Cadena')

    def _validar_fecha(self, dato):
        if type(dato) != datetime:
            raise TypeError('Se esperaba una Fecha')

    def _validar_contrato(self, dato):
        from claseContrato import Contrato
        if type(dato) != Contrato:
            raise TypeError('Se esperaba un Contrato')

    def agregarContrato(self, contrato):
        self._validar_contrato(contrato)
        self.__contratos.append(contrato)

    def getDni(self):
        return self.__dni
