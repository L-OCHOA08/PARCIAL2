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
        sigue = False
        puntaje_sala1 = 0
        puntaje_sala2 = 0
        puntaje_sala3 = 0
        puntaje_sala4 = 0
        puntaje = 0

        nombre_jugador = ingreso_individual((120, 55, 12), jugador)

        puntaje_sala1, sigue = salaa1((161, 147, 250))

        if sigue == True:
            puntaje_sala2, sigue = salaa2((37, 77, 112))
            
        if sigue == True:
            puntaje_sala3, sigue = salaa3((45, 79, 43))

        if sigue == True:
            puntaje_sala4, sigue = salaa4((82, 29, 68))
            if sigue == True:
                info_jugador.append('Completo')
            else:
                info_jugador.append('No completo')


        puntaje = puntaje_sala1 + puntaje_sala2 + puntaje_sala3 + puntaje_sala4

        info_jugador.append(puntaje_sala1)
        info_jugador.append(puntaje_sala2)
        info_jugador.append(puntaje_sala3)
        info_jugador.append(puntaje_sala4)
        info_jugador.append(puntaje)

        lista_jugadores[f'{nombre_jugador}: '] = info_jugador
    # resumen((120, 55, 12),lista_jugadores)
    print(lista_jugadores)


juego()