

class Carrera(object):
    __codigo: int
    __nombre: str
    __titulo: str
    __cant_semestres: str
    __tipo_titulo: str

    def __init__(self, cod, nom, tit, cant_sem, tipo_tit):
        
        # Una forma de validar los datos
        self._validar_entero(cod)
        self._validar_cadena(nom)
        self._validar_cadena(tit)
        self._validar_cadena(cant_sem)
        self._validar_cadena(tipo_tit)
    
        self.__codigo = cod
        self.__nombre = nom
        self.__titulo = tit
        self.__cant_semestres = cant_sem
        self.__tipo_titulo = tipo_tit

    def _validar_entero(self, dato):
        if type(dato) != int:
            raise TypeError('Se espera una cadena')

    def _validar_cadena(self, dato):
        if type(dato) != str:
            raise TypeError('Se espera una cadena')

    def getCodigo(self):
        return self.__codigo
    
    def getNombre(self):
        return self.__nombre

    def getCantSemestres(self):
        return self.__cant_semestres

    def validarNombre(self, nombre):
        self._validar_cadena(nombre)
        return self.__nombre.lower() == nombre.lower()