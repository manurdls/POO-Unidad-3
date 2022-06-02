from abc import ABC, abstractclassmethod

class AparatoElectronico(ABC):
    __marca: str
    __modelo: str
    __color: str
    __pais_fabricacion: str
    __precio_base: float

    def __init__(self, marca, modelo, color, pais_fabricacion, precio_base):
        self._validar_cadena(marca)
        self._validar_cadena(modelo)
        self._validar_cadena(color)
        self._validar_cadena(pais_fabricacion)
        self._validar_flotante(precio_base)

        self.__marca = marca
        self.__modelo = modelo
        self.__color = color
        self.__pais_fabricacion = pais_fabricacion
        self.__precio_base = precio_base

    def _validar_cadena(self, dato):
        if type(dato) != str:
            raise TypeError('Se esperaba una Cadena')

    def _validar_flotante(self, dato):
        if type(dato) != float:
            raise TypeError('Se esperaba un numero en Punto Flotante (numero real)')

    def __str__(self):
        return 'Marca: {}\nModelo: {}\nColor: {}\nPais de fabricacion: {}\nPrecio base: {}\n'.format(self.__marca,
                                                                                                   self.__modelo,
                                                                                                   self.__color,
                                                                                                   self.__pais_fabricacion,
                                                                                                   self.__precio_base)

    def get_precio_base(self):
        return self.__precio_base

    def get_importe_venta(self):
        return self.__precio_base + (self._calcular_porcentaje_adicional() /100) * self.__precio_base

    @abstractclassmethod
    def _calcular_porcentaje_adicional(self):
        pass