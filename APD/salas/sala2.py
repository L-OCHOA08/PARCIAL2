import pygame
import random

def sala2(color_fondo):
    pygame.init()

    # COLORES
    ANCHO_VENTANA = 800
    ALTO_VENTANA = 900
    COLOR_BLANCO = (255, 255, 255)
    COLOR_CORRECTO = (255, 255, 255)
    COLOR_INCORRECTO = (255, 255, 255)
    COLOR_TIMER = (255,255,255)

    # VENTANA
    pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
    pygame.display.set_caption("Sala de Escape de Programación")

    # RELOJ
    reloj = pygame.time.Clock()
    TIEMPO = 15000
    respondio = False
    inicio_tiempo = pygame.time.get_ticks()

    # FONDOS
    fondo1 = pygame.image.load("puerta_cerrada.png")
    fondo2 = pygame.image.load("puerta_abierta.png")
    usar_fondo1 = True

    avanzar = pygame.image.load("flecha_avanzar.svg")
    avanzar = pygame.transform.scale(avanzar, (200,200))
    avanzar_rect = avanzar.get_rect(topleft=(370,600))

    # TEXTOS
    fuente_sala = pygame.font.Font("Golden Age.ttf", 30)
    texto_sala = fuente_sala.render("Sala 2", True, COLOR_BLANCO)
    fuente_pregunta = pygame.font.Font("Golden Age Shad.ttf", 30)
    texto_pregunta = fuente_pregunta.render('Que imprime print("Hola"[1])?', True, color_fondo)

    rect_respuesta = pygame.Rect(100, 270, 600, 80)
    pos_respuesta = 400


    intentos = 2

    respuesta_font = pygame.font.Font("Golden Age.ttf", 30)
    respuesta_correcta = "o"
    ingreso = ""

    rect_boton = pygame.Rect(250, 400, 300, 80)
    texto_boton = respuesta_font.render("Responder", True, color_fondo)

    flag_juego = True
    while flag_juego:
        sigue = False
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                flag_juego = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_BACKSPACE:
                    ingreso = ingreso[:-1]
                    pos_respuesta += 8
                else:
                    ingreso += evento.unicode
                    pos_respuesta -= 8
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if rect_boton.collidepoint(evento.pos) and ingreso.lower() != respuesta_correcta:
                    texto_intentos = fuente_sala.render(f"Intentos restantes: {intentos}", True, COLOR_BLANCO)
                    intentos -= 1
                    COLOR_INCORRECTO = (176, 23, 31)
                    if intentos == 0:
                        sigue = False
                        puntaje_sala2= 0
                        return puntaje_sala2, sigue
                if rect_boton.collidepoint(evento.pos) and ingreso.lower() == respuesta_correcta:
                    puntaje_sala2 = random.randint(10, 35)
                    rect_boton = pygame.Rect(100, 270, 0, 0)
                    rect_respuesta = pygame.Rect(100, 270, 0, 0)
                    ingreso = ""
                    usar_fondo1 = False
                    respondio = True
                    COLOR_TIMER = (86, 252, 25)
                    
                if avanzar_rect.collidepoint(evento.pos):
                    sigue = True
                    return puntaje_sala2, sigue

        if not respondio:
            tiempo_actual = pygame.time.get_ticks()
            tiempo_restante = max(0, TIEMPO - (tiempo_actual - inicio_tiempo))
            segundos_restantes = tiempo_restante // 1000

        if segundos_restantes == 0:
            pygame.quit()

        if usar_fondo1:
            pantalla.blit(fondo1, (-100,0))
        else:
            pantalla.blit(fondo2, (-100,0))
            pantalla.blit(avanzar, (370,600))

        texto_tiempo = fuente_sala.render(f"Tiempo: {segundos_restantes}", True, COLOR_TIMER)
        pantalla.blit(texto_tiempo, (330, 500))

        # MUESTRO LA PREGUNTA
        pantalla.blit(texto_sala, (355, 25))
        texto_intentos = fuente_sala.render(f"Intentos restantes: {intentos}", True, COLOR_INCORRECTO)
        pantalla.blit(texto_intentos, (250, 50))
        marco_pregunta = pygame.draw.rect(pantalla, COLOR_BLANCO, pygame.Rect(60, 75, 690, 150), 0, 50, 50, 25, 25)
        pantalla.blit(texto_pregunta, (135, 135))
        marco_respuesta = pygame.draw.rect(pantalla, COLOR_CORRECTO, rect_respuesta, 10, 20, 20, 20, 20)
        input_respuesta = respuesta_font.render(f"{ingreso}", True, COLOR_BLANCO)
        pantalla.blit(input_respuesta, (pos_respuesta, 295))


        if len(ingreso) > 0:
            marco_boton = pygame.draw.rect(pantalla, COLOR_BLANCO, rect_boton, 0, 50, 50, 25, 25)
            pantalla.blit(texto_boton, (330, 425))


        pygame.display.flip()
        reloj.tick(60)

    pygame.quit()