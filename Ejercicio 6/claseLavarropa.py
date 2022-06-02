from re import A
from claseAparatoElectronico import AparatoElectronico

class Lavarropa(AparatoElectronico):
    __capacidad_lavado: int
    __velocidad_centrifugado: int
    __cantidad_programas: int
    __tipo_carga: str

    def __init__(self, **datos):
        self._validar_flotante(datos['capacidad_lavado'])
        self._validar_entero(datos['velocidad_centrifugado'])
        self._validar_entero(datos['cantidad_programas'])
        self._validar_cadena(datos['tipo_carga'])

        super().__init__(datos['marca'], datos['modelo'], datos['color'], datos['pais_fabricacion'], datos['precio_base'])
        self.__capacidad_lavado = datos['capacidad_lavado']
        self.__velocidad_centrifugado = datos['velocidad_centrifugado']
        self.__cantidad_programas = datos['cantidad_programas']
        self.__tipo_carga = datos['tipo_carga']

    def _validar_flotante(self, dato):
        if type(dato) != float:
            raise TypeError('Se esperaba un numero en Punto Flotante (numero real)')

    def _validar_entero(self, dato):
        if type(dato) != int:
            raise TypeError('Se esperaba un numero Entero')

    def _validar_cadena(self, dato):
        if type(dato) != str:
            raise TypeError('Se esperaba una Cadena')

    def __str__(self):
        return super().__str__() + 'Capcidad de lavado: {} kg\nVelocidad de centrifugado: {} rpm\nCantidad de programas: {}\nTipo de carga: {}\nImporte de venta: {}'.format(self.__capacidad_lavado,
                                                                                                                                                                             self.__velocidad_centrifugado,
                                                                                                                                                                             self.__cantidad_programas,
                                                                                                                                                                             self.__tipo_carga,
                                                                                                                                                                             super().get_importe_venta())

    def _calcular_porcentaje_adicional(self):
        porcentaje = 0

        if self.__capacidad_lavado <= 5: porcentaje += 1
        else: porcentaje += 3

        return porcentaje