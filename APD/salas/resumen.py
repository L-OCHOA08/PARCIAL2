import pygame

def resumen(color_fondo, lista_jugadores):
    pygame.init()

    ANCHO_VENTANA = 800
    ALTO_VENTANA = 900
    fuente = pygame.font.Font("Golden Age.ttf", 30)

    pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
    pygame.display.set_caption("Sala de Escape de Programación")

    flag_juego = True
    while flag_juego:
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                flag_juego = False

        pantalla.fill(color_fondo)

        ordenados = sorted(lista_jugadores.items(), key=lambda x: x[1][-1], reverse=True)

        y = 50
        for jugador, valores in ordenados:
            texto = f"{jugador}{' - '.join(str(v) for v in valores)}"
            render = fuente.render(texto, True, (255,255,255))
            pantalla.blit(render, (40, y))
            y += 50

        mejor_puntaje_fuente = pygame.font.Font("Golden Age.ttf", 40)
        mejor_puntaje_texto = mejor_puntaje_fuente.render("Mejor Puntaje Total", True, (255,255,255))
        pantalla.blit(mejor_puntaje_texto, (200, 560))

        pygame.display.flip()



# resumen((68, 0, 255))