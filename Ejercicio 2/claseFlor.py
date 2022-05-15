

class Flor(object):
    __numero: int
    __nombre: str
    __color: str
    __descripcion: str

    def __init__(self, num, nom, col, desc):
        self._validar_entero(num)
        self._validar_cadena(nom)
        self._validar_cadena(col)
        self._validar_cadena(desc)

        self.__numero = num
        self.__nombre = nom
        self.__color = col
        self.__descripcion = desc

    def _validar_entero(self, dato):
        if type(dato) != int:
            raise TypeError('Se espera una cadena')

    def _validar_cadena(self, dato):
        if type(dato) != str:
            raise TypeError('Se espera una cadena')

    def __str__(self):
        return 'Numero: {}, Nombre: {}, Color: {}, Descripción: {}'.format(self.__numero,
                                                                           self.__nombre,
                                                                           self.__color,
                                                                           self.__descripcion)

    def getNumero(self):
        return self.__numero

    def getNombre(self):
        return self.__nombre

    def getColor(self):
        return self.__color

    def getDescripcion(self):
        return self.__descripcion
