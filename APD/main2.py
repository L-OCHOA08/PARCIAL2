from salas.inicio import iniciar_juego
from salas.preparacion import ingreso_individual
from salas.sala1 import sala1
from salas.sala2 import sala2
from salas.sala3 import sala3
from salas.sala4 import sala4
from salas.resumen import resumen

def juego():
    lista_jugadores = {}
    lista_por_sala = {}
    no_pasaron_primera = list()
    cantidad_incial_jugadores = 1
    cantidad_incial_jugadores = iniciar_juego(cantidad_incial_jugadores)
    print(cantidad_incial_jugadores)
    for jugador in range(cantidad_incial_jugadores):
        info_jugador = []
        sala_finalizo = 1
        sigue = False
        puntaje_sala1 = 0
        puntaje_sala2 = 0
        puntaje_sala3 = 0
        puntaje_sala4 = 0
        puntaje = 0

        nombre_jugador = ingreso_individual((120, 55, 12), jugador)

        puntaje_sala1, sigue = sala1((161, 147, 250))

        if sigue == True:
            sala_finalizo += 1
            puntaje_sala2, sigue = sala2((37, 77, 112))
        else:
            no_pasaron_primera.append(nombre_jugador)
            
        if sigue == True:
            sala_finalizo += 1
            puntaje_sala3, sigue = sala3((45, 79, 43))

        if sigue == True:
            sala_finalizo += 1
            puntaje_sala4, sigue = sala4((82, 29, 68))

        if sigue == True:
            info_jugador.append('Completo')
        else:
            info_jugador.append('No completo')

        lista_por_sala[f'{nombre_jugador}: '] = f'Sala: {sala_finalizo}'


        puntaje = puntaje_sala1 + puntaje_sala2 + puntaje_sala3 + puntaje_sala4

        info_jugador.append(puntaje_sala1)
        info_jugador.append(puntaje_sala2)
        info_jugador.append(puntaje_sala3)
        info_jugador.append(puntaje_sala4)
        info_jugador.append(puntaje)

        lista_jugadores[f'{nombre_jugador}: '] = info_jugador
    resumen((120, 55, 12),lista_jugadores, lista_por_sala, no_pasaron_primera)
    print(lista_por_sala)


juego()