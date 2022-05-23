import os


class Menu(object):
    __switcher: dict
    __calefactores = None

    def __init__(self, calefactores):
        self.__switcher = {0:self.salir,
                           1:self.inciso1,
                           }
        self.__calefactores = calefactores

    def getSwitcher(self):
        return self.__switcher

    def option(self, op):
        func = self.__switcher.get(op, lambda: print("Opción no válida"))
        func()

    def salir(self):
        print('Fin Programa')

    def inciso1(self):
        costo_kcaloriasm3 = int(input("Ingrese el costo de 1 kcaloria/m3: "))
        cantidad_estimada_enm3 = int(input("Ingrese la cantidad estimada en m3 que se va a consumir: "))
        costo_a_pagar_en_gas = costo_kcaloriasm3 * cantidad_estimada_enm3
        calefactor_gas_menor_consumo = self.__calefactores.obtener_calefactor_gas_de_menor_consumo()
        print("Marca y modelo del calefactor a gas natural de menor consumo: ")
        print(calefactor_gas_menor_consumo)

        costo_kwatth = int(input("Ingrese el costo del kwat/hora: "))
        cantidad_estimada_en1h = int(input("Ingrese la cantidad estimada que se va a consumir en 1 hora: "))
        costo_a_pagar_en_energia = costo_kwatth * cantidad_estimada_en1h
        calefactor_electrico_menor_consumo = self.__calefactores.obtener_calefactor_electrico_de_menor_consumo()
        print("Marca y modelo del calefactor eléctrico de menor consumo: ")
        print(calefactor_electrico_menor_consumo)

        if costo_a_pagar_en_gas < costo_a_pagar_en_energia:
            print("El tipo de calefactor de menor consumo en este caso es el Calefactor a Gas: ")
            print(calefactor_gas_menor_consumo)
        elif costo_a_pagar_en_energia < costo_a_pagar_en_gas:
            print("El tipo de calefactor de menor consumo en este caso es el Calefactor Electrico: ")
            print(calefactor_electrico_menor_consumo)
        else:
            print("Ambos calefactores tienen el mismo consumo: ")
            print(calefactor_gas_menor_consumo)
            print(calefactor_electrico_menor_consumo)