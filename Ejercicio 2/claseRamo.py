

class Ramo(object):
    __tamanio: str
    __flores: list

    def __init__(self, tamanio, flores):
        self._validar_cadena(tamanio)

        self.__tamanio = tamanio
        self.__flores = flores

    def __str__(self):
        retorno = 'Tamanio: {}, Flores: '.format(self.__tamanio)
        for flor in self.__flores():
            retorno += flor.getNombre() + ' '
    
    def _validar_cadena(self, dato):
        if type(dato) != str:
            raise TypeError('Se espera una cadena')

    def getTamanio(self):
        return self.__tamanio
    
    def getFlores(self):
        return self.__flores
