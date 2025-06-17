import pygame

def resumen(color_fondo, lista_jugadores):
    pygame.init()

    ANCHO_VENTANA = 800
    ALTO_VENTANA = 900
    fuente = pygame.font.Font("Golden Age.ttf", 30)

    pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
    pygame.display.set_caption("Sala de Escape de Programación")
    tabla = ""
    for clave, valor in lista_jugadores.items():
        nombre_jugador, puntaje = valor
        tabla += f"{clave}{nombre_jugador} {puntaje} pts\n"

    lineas = tabla.strip().split('\n')

    flag_juego = True
    while flag_juego:
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                flag_juego = False

        pantalla.fill(color_fondo)

        for i, linea in enumerate(lineas):
            linea_render = fuente.render(linea, True, (255,255,255))
            pantalla.blit(linea_render, (50, 50 + i * 30))

        pygame.display.flip()



# resumen((68, 0, 255))