from claseRamo import Ramo

class ManejadorRamos(object):
    __ramos: list

    def __init__(self):
        self.__ramos = []

    def _validar_ramo(self, dato):
        if type(dato) != Ramo:
            raise TypeError('Se espera un Ramo')

    def agregarRamo(self, ramo):
        self._validar_ramo(ramo)

        self.__ramos.append(ramo)
        print('El ramo fue agregado exitosamente...')

    def mostrarRamos(self):
        for ramo in self.__ramos:
            print(ramo)
    
    def mostrar_nombre_5_flores_mas_pedidas(self):
        datos = {}
        for ramo in self.__ramos:
            flores = ramo.getFlores()
            for flor in flores:
                if flor.getNombre() not in datos:
                    datos[flor.getNombre()] = 1
                else:
                    datos[flor.getNombre()] += 1

        datos = sorted(datos.items(), key=lambda x: x[1], reverse=True)
        
        try:
            print("Flores más vendidas: ")
            for i in range(5):
                print('Top {}: {}. Ramos en los que aparece: {}'.format(i+1, datos[i][0], datos[i][1]))
        except Exception:
                print('Al parecer no hay suficientes ventas para hacer un top 5...')

    def mostrar_flores_venidas_para_un_tamanio(self, tamanio):
        flores_vendidas_por_tamanio_de_ramo = []
        print('Flores vendidas para el tamaño: ',tamanio)
        for ramo in self.__ramos:
            if ramo.getTamanio() == tamanio:
                flores = ramo.getFlores()
                for flor in flores:
                    if flor not in flores_vendidas_por_tamanio_de_ramo:
                        flores_vendidas_por_tamanio_de_ramo.append(flor)
                        print('Nombre: {}, Color: {}'.format(flor.getNombre(), flor.getColor()))
        if len(flores_vendidas_por_tamanio_de_ramo) == 0:
            print('No se han registrado ventas para el tamanio: ', tamanio)

        
