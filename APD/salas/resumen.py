import pygame

def resumen(color_fondo):
    pygame.init()

    ANCHO_VENTANA = 800
    ALTO_VENTANA = 900

    pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
    pygame.display.set_caption("Sala de Escape de Programación")

    flag_juego = True
    while flag_juego:
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                flag_juego = False

        pantalla.fill(color_fondo)

        pygame.display.flip()



# resumen((68, 0, 255))