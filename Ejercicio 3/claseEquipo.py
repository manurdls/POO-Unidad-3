

class Equipo(object):
    __nombre: str
    __ciudad: str
    __contratos: list

    def __init__(self, nom, ciu):
        self._validar_cadena(nom)
        self._validar_cadena(ciu)

        self.__nombre = nom
        self.__ciudad = ciu
        self.__contratos = []

    def __str__(self):
        return 'Nombre: {} Ciudad: {}'.format(self.__nombre.ljust(40), self.__ciudad)

    def _validar_cadena(self, dato):
        if type(dato) != str:
            raise TypeError('Se esperaba una Cadena')
    
    def _validar_contrato(self, dato):
        from claseContrato import Contrato
        if type(dato) != Contrato:
            raise TypeError('Se esperaba un Contrato')

    def agregarContrato(self, contrato):
        self._validar_contrato(contrato)
        self.__contratos.append(contrato)

    def getNombre(self):
        return self.__nombre

    def getContratos(self):
        retorno = None
        if len(self.__contratos) != 0:
            retorno = self.__contratos
        return retorno