from re import A
from claseAparatoElectronico import AparatoElectronico

class Heladera(AparatoElectronico):
    __capacidad_litros: float
    __freezer: bool
    __ciclica: bool

    def __init__(self, **datos):
        self._validar_flotante(datos['capacidad_litros'])
        self._validar_booleano(datos['freezer'])
        self._validar_booleano(datos['ciclica'])
        
        super().__init__(datos['marca'], datos['modelo'], datos['color'], datos['pais_fabricacion'], datos['precio_base'])
        self.__capacidad_litros = datos['capacidad_litros']
        self.__freezer = datos['freezer']
        self.__ciclica = datos['ciclica']

    def _validar_flotante(self, dato):
        if type(dato) != float:
            raise TypeError('Se esperaba un numero en Punto Flotante (numero real)')

    def _validar_booleano(self, dato):
        if type(dato) != bool:
            raise TypeError('Se esperaba un Booleano')

    def __str__(self):
        return super().__str__() + 'Capacidad (litros): {}\nFreezer: {}\nCiclica: {}\nImporte de venta: {}'.format(self.__capacidad_litros,
                                                                                                                   self.__freezer,
                                                                                                                   self.__ciclica,
                                                                                                                   super().get_importe_venta())

    def _calcular_porcentaje_adicional(self):
        porcentaje = 0

        if not self.__freezer: porcentaje += 1
        else: porcentaje += 5

        if self.__ciclica: porcentaje += 10

        return porcentaje