from ing_valid_datos.datos import *

def sala_de_escape():
    MAX_JUGADORES = 10
    lista_jugadores = []
    cant_jugadores = int(input("Cantidad de jugadores(1-10): "))
    while cant_jugadores <= 0 or cant_jugadores > MAX_JUGADORES:
        cant_jugadores = input("Cantidad inválida. Ingrese una cantidad de jugadores entre 1 y 10: ")

    # ingreso_individual(cant_jugadores, lista_jugadores)
    lista_jugadores, nombre_jugador = ingreso_individual(cant_jugadores, lista_jugadores)
    salas(lista_jugadores, nombre_jugador)


sala_de_escape()