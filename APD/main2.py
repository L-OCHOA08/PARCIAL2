from salas.main import iniciar_juego
from salas.preparacion import ingreso_individual
from salas.sala1 import salaa1
from salas.sala2 import salaa2
from salas.sala3 import salaa3
from salas.sala4 import salaa4
from salas.resumen import resumen

def juego():
    lista_jugadores = {}
    cantidad_incial_jugadores = 1
    cantidad_incial_jugadores = iniciar_juego(cantidad_incial_jugadores)
    print(cantidad_incial_jugadores)
    for jugador in range(cantidad_incial_jugadores):
        info_jugador = []
        puntaje = 0
        nombre_jugador = ingreso_individual((120, 55, 12), jugador)
        info_jugador.append(nombre_jugador)
        puntaje += salaa1((161, 147, 250))
        puntaje += salaa2((37, 77, 112))
        puntaje += salaa3((45, 79, 43))
        puntaje += salaa4((82, 29, 68))
        info_jugador.append(puntaje)
        lista_jugadores[f'Jugador {jugador+1}: '] = info_jugador
    # resumen()
    print(lista_jugadores)


juego()