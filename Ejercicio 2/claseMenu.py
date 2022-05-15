from claseManejadorFlores import ManejadorFlores

from claseManejadorRamos import ManejadorRamos

from claseRamo import Ramo

class Menu(object):
    __switcher: dict
    __flores: ManejadorFlores
    __ramos: ManejadorRamos

    def __init__(self, flores, ramos):
        self.__switcher = {0:self.salir,
                           1:self.inciso1,
                           2:self.inciso2,
                           3:self.inciso3,
                           }
        self.__flores = flores
        self.__ramos = ramos

    def getSwitcher(self):
        return self.__switcher

    def option(self, op):
        func = self.__switcher.get(op, lambda: print("Opción no válida"))
        func()

    def salir(self):
        print('Fin Programa')

    def inciso1(self):
        tamanio = self._ingresarTamanio()
        if tamanio:
            flores = self._ingresarFlores()
            if flores:
                self.__ramos.agregarRamo(Ramo(tamanio, flores))
            else:
                print("Operación cancelada...")    
        else:
            print("Operación cancelada...")

    def inciso2(self):
        self.__ramos.mostrar_nombre_5_flores_mas_pedidas()

    def inciso3(self):
        tamanio = self._ingresarTamanio()
        if tamanio:
            self.__ramos.mostrar_flores_venidas_para_un_tamanio(tamanio)

    def _ingresarTamanio(self) -> str:
        tamanios = ('chico', 'mediano', 'grande')
        tamanio_ramo = None
        band = False
        print("Nota: si desea cancelar la operación ingrese 'cancelar'.")
        while not band:
            entrada = input('Ingrese el tamanio del ramo: ').lower()
            if entrada in tamanios:
                tamanio_ramo = entrada
                band = True
            elif entrada == 'cancelar':
                band = True
            else:
                print("Error: ingrese un tamanio válido. ('chico', 'mediano', 'grande')")
        return tamanio_ramo
    
    def _ingresarFlores(self) -> list:
        flores = []
        band = False
        cant_flores = 0
        
        print('A continuación se hará el ingreso de las flores para el ramo.')
        print('Nota: se pueden ingresar como máximo 4 tipos distintos de flores para un ramo.')
        print('Nota: Las rosas de color rojo y las rosas de color rosa son flores de distinto tipo, tenga en cuenta eso.')

        while not band:
            respuesta = input('¿Desea agregar un tipo de flores al ramo?. si/no: ').lower()
            if respuesta == 'si':
                nombre_flores = input('Ingrese el nombre de las flores: ').lower()
                color_flores = input('Ingrese el color de las flores: ').lower()
                indice = self.__flores.buscar_flores_nombre_y_color(nombre_flores, color_flores)
                if indice:
                    flor = self.__flores.getFlores(indice)
                    if flor not in flores:
                        flores.append(flor)
                        print('Las flores han sido agregadas al ramo...')
                    else:
                        print('Las flores ya han sido agregadas al ramo...')
                else:
                    print('No contamos con flores con las características que busca... disculpe')

            elif respuesta == 'no':
                if len(flores) > 0:
                    print('Ingreso de flores terminado..')
                band = True
            else:
                print('Error: Respuesta inválida. Ingrese si o no.')
            
            if len(flores) == 4 :
                print('Ingreso de flores terminado..')
                band = True

            if len(flores) == 0:
                flores = None

        return flores
