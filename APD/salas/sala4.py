import pygame
from salas.resumen import resumen

def salaa4(color_fondo):
    pygame.init()

    # COLORES
    ANCHO_VENTANA = 800
    ALTO_VENTANA = 900
    COLOR_BLANCO = (255, 255, 255)
    COLOR_INCORRECTO1 = (255, 255, 255)
    COLOR_CORRECTO = (255, 255, 255)
    COLOR_INCORRECTO3 = (255, 255, 255)
    COLOR_INCORRECTO4 = (255, 255, 255)

    # VENTANA
    pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
    pygame.display.set_caption("Sala de Escape de Programación")

    # TEXTOS
    fuente_sala = pygame.font.Font("Golden Age.ttf", 30)
    texto_sala = fuente_sala.render("Sala 4", True, COLOR_BLANCO)
    fuente_pregunta = pygame.font.Font("Golden Age Shad.ttf", 30)
    texto_pregunta = fuente_pregunta.render("Que diferencia hay entre", True, color_fondo)
    texto2_pregunta = fuente_pregunta.render("deepcopy() y copy()?", True, color_fondo)


    intentos = 2

    fuente_opciones = pygame.font.Font("Golden Age.ttf", 20)
    fuente_boton = pygame.font.Font("Golden Age.ttf", 30)
    texto_opcion1 = fuente_opciones.render("copy() copia en otra carpeta", True, color_fondo)
    texto2_opcion1 = fuente_opciones.render("y deepcopy() lo hace comprimido", True, color_fondo)
    rect_opcion1 = pygame.Rect(100, 270, 600, 80)
    texto_opcion2 = fuente_opciones.render("copy() realiza una copia referencial al", True, color_fondo)
    texto2_opcion2 = fuente_opciones.render("original y deepcopy() realiza una copia independiente", True, color_fondo)
    rect_opcion2 = pygame.Rect(100, 370, 600, 80)
    texto_opcion3 = fuente_opciones.render("Indicar que un directorio debe tratarse como un", True, color_fondo)
    texto2_opcion3 = fuente_opciones.render("paquete de Python", True, color_fondo)
    rect_opcion3 = pygame.Rect(100, 470, 600, 80)
    texto_opcion4 = fuente_opciones.render("Ninguna de las anteriores", True, color_fondo)
    rect_opcion4 = pygame.Rect(100, 570, 600, 80)

    rect_boton = pygame.Rect(250, 750, 0, 0)
    texto_boton = fuente_boton.render("Siguiente", True, color_fondo)

    texto_ganaste = fuente_sala.render("Ganaste!", True, (86, 252, 25))
    pos_texto_ganaste = (-100, -100)

    flag_juego = True
    while flag_juego and intentos > 0:
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                flag_juego = False
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if marco_opcion1.collidepoint(evento.pos):
                    COLOR_INCORRECTO1 = (176, 23, 31)
                    intentos -= 1
                if marco_opcion2.collidepoint(evento.pos):
                    pos_texto_ganaste = (330, 700)
                    rect_boton = (250, 750, 300, 80)
                    rect_opcion1 = pygame.Rect(100, 370, 0, 0)
                    texto_opcion2 = fuente_opciones.render("copy() realiza una copia referencial al", True, (255,255,255))
                    texto2_opcion2 = fuente_opciones.render("original y deepcopy() realiza una copia independiente", True, (255,255,255))
                    rect_opcion3 = pygame.Rect(100, 370, 0, 0)
                    rect_opcion4 = pygame.Rect(100, 370, 0, 0)
                    COLOR_CORRECTO = (86, 252, 25)
                if marco_opcion3.collidepoint(evento.pos):
                    COLOR_INCORRECTO3 = (176, 23, 31)
                    intentos -=1
                if marco_opcion4.collidepoint(evento.pos):
                    COLOR_INCORRECTO4 = (176, 23, 31)
                    intentos -= 1
                    print(intentos)
                if marco_boton.collidepoint(evento.pos):
                    resumen((120, 55, 12))

        pantalla.fill(color_fondo)

        # MUESTRO LA PREGUNTA
        pantalla.blit(texto_sala, (350, 25))
        texto_intentos = fuente_sala.render(f"Intentos restantes: {intentos}", True, COLOR_BLANCO)
        pantalla.blit(texto_intentos, (235, 50))
        marco_pregunta = pygame.draw.rect(pantalla, COLOR_BLANCO, pygame.Rect(60, 75, 690, 150), 0, 50, 50, 25, 25)
        pantalla.blit(texto_pregunta, (175, 125))
        pantalla.blit(texto2_pregunta, (210, 155))

        # MUESTRO LAS OPCIONES
        marco_opcion1 = pygame.draw.rect(pantalla, COLOR_INCORRECTO1, rect_opcion1, 0, 50, 50, 25, 25)
        marco_opcion2 = pygame.draw.rect(pantalla, COLOR_CORRECTO, rect_opcion2, 0, 50, 50, 25, 25)
        marco_opcion3 = pygame.draw.rect(pantalla, COLOR_INCORRECTO3, rect_opcion3, 0, 50, 50, 25, 25)
        marco_opcion4 = pygame.draw.rect(pantalla, COLOR_INCORRECTO4, rect_opcion4, 0, 50, 50, 25, 25)

        marco_boton = pygame.draw.rect(pantalla, COLOR_BLANCO, rect_boton, 0, 50, 50, 25, 25)
        pantalla.blit(texto_opcion1, (130, 295))
        pantalla.blit(texto2_opcion1, (130, 315))
        pantalla.blit(texto_opcion2, (130, 395))
        pantalla.blit(texto2_opcion2, (130, 415))
        pantalla.blit(texto_opcion3, (130, 495))
        pantalla.blit(texto2_opcion3, (130, 515))
        pantalla.blit(texto_opcion4, (130, 600))


        pantalla.blit(texto_ganaste,pos_texto_ganaste)
        pantalla.blit(texto_boton, (330, 775))


        pygame.display.flip()

    pygame.quit()