from claseTelevisor import Televisor
from claseHeladera import Heladera
from claseLavarropa import Lavarropa

def test():
    unTelevisor = Televisor(marca='Toshiba', modelo='ACD', color='rojo', pais_fabricacion='Alemania', precio_base=40000.0,
                            tipo_pantalla='lcd', pulgadas=40.0, definicion='FULL HD', conexion_internet=True)
    
    unaHeladera = Heladera(marca='Toshiba', modelo='ACD', color='rojo', pais_fabricacion='Alemania', precio_base=40000.0,
                            capacidad_litros=2000.0, freezer=False, ciclica=True)

    unLavarropa = Lavarropa(marca='Toshiba', modelo='ACD', color='rojo', pais_fabricacion='Alemania', precio_base=40000.0,
                            capacidad_lavado=6.0, velocidad_centrifugado=600, cantidad_programas=5, tipo_carga='Superior')


    print(unTelevisor)
    print('')
    print(unaHeladera)
    print('')
    print(unLavarropa)

if __name__ == '__main__':
    test()