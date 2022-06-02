from claseAparatoElectronico import AparatoElectronico


class Televisor(AparatoElectronico):
    __tipo_pantalla: str
    __pulgadas: float
    __definicion: str
    __conexion_internet: bool

    def __init__(self, **datos):
        self._validar_cadena(datos['tipo_pantalla'])
        self._validar_flotante(datos['pulgadas'])
        self._validar_cadena(datos['definicion'])
        self._validar_booleano(datos['conexion_internet'])


        super().__init__(datos['marca'], datos['modelo'], datos['color'], datos['pais_fabricacion'], datos['precio_base'])
        self.__tipo_pantalla = datos['tipo_pantalla']
        self.__pulgadas = datos['pulgadas']
        self.__definicion = datos['definicion']
        self.__conexion_internet = datos['conexion_internet']

    def _validar_cadena(self, dato):
        if type(dato) != str:
            raise TypeError('Se esperaba una Cadena')
    
    def _validar_flotante(self, dato):
        if type(dato) != float:
            raise TypeError('Se esperaba un numero en Punto Flotante (numero real)')

    def _validar_booleano(self, dato):
        if type(dato) != bool:
            raise TypeError('Se esperaba un Booleano')

    def __str__(self):
        return super().__str__() + 'Tipo de pantalla: {}\nPulgadas: {}\nDefinicion: {}\nConexion a internet: {}\nImporte de venta: {}'.format(self.__tipo_pantalla,
                                                                                                                                              self.__pulgadas,
                                                                                                                                              self.__definicion,
                                                                                                                                              self.__conexion_internet,
                                                                                                                                              super().get_importe_venta())

    def _calcular_porcentaje_adicional(self):
        porcentaje = 0

        if self.__definicion == 'SD': porcentaje += 1
        elif self.__definicion == 'HD': porcentaje += 2
        elif self.__definicion == 'FULL HD': porcentaje +=3

        if self.__conexion_internet == True: porcentaje += 10

        return porcentaje
