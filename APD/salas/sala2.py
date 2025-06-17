import pygame
import random
from salas.sala3 import salaa3

def salaa2(color_fondo):
    pygame.init()

    # COLORES
    ANCHO_VENTANA = 800
    ALTO_VENTANA = 900
    COLOR_BLANCO = (255, 255, 255)
    COLOR_INCORRECTO1 = (255, 255, 255)
    COLOR_INCORRECTO2 = (255, 255, 255)
    COLOR_CORRECTO = (255, 255, 255)
    COLOR_INCORRECTO4 = (255, 255, 255)

    # VENTANA
    pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
    pygame.display.set_caption("Sala de Escape de Programación")

    # TEXTOS
    fuente_sala = pygame.font.Font("Golden Age.ttf", 30)
    texto_sala = fuente_sala.render("Sala 2", True, COLOR_BLANCO)
    fuente_pregunta = pygame.font.Font("Golden Age Shad.ttf", 30)
    texto_pregunta = fuente_pregunta.render("Como se estructura un IF en Python?", True, color_fondo)


    intentos = 2

    fuente_opciones = pygame.font.Font("Golden Age.ttf", 30)
    texto_opcion1 = fuente_opciones.render("if (x > 5) then { print('Mayor'') }", True, color_fondo)
    rect_opcion1 = pygame.Rect(100, 270, 600, 80)
    texto_opcion2 = fuente_opciones.render("if x > 5: print 'Mayor'", True, color_fondo)
    rect_opcion2 = pygame.Rect(100, 370, 600, 80)
    texto_opcion3 = fuente_opciones.render("if x > 5: print('Mayor')", True, color_fondo)
    rect_opcion3 = pygame.Rect(100, 470, 600, 80)
    texto_opcion4 = fuente_opciones.render("if x > 5 do print('Mayor'')", True, color_fondo)
    rect_opcion4 = pygame.Rect(100, 570, 600, 80)

    rect_boton = pygame.Rect(250, 750, 0, 0)
    texto_boton = fuente_opciones.render("Siguiente", True, color_fondo)

    texto_ganaste = fuente_sala.render("Ganaste!", True, (86, 252, 25))
    pos_texto_ganaste = (-100, -100)

    flag_juego = True
    while flag_juego:
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                flag_juego = False
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if marco_opcion1.collidepoint(evento.pos):
                    COLOR_INCORRECTO1 = (176, 23, 31)
                    intentos -= 1
                    if intentos == 0:
                        puntaje_sala2 = 0
                        sigue = False
                        return puntaje_sala2, sigue

                if marco_opcion2.collidepoint(evento.pos):
                    COLOR_INCORRECTO2 = (176, 23, 31)
                    intentos -= 1
                    if intentos == 0:
                        puntaje_sala2 = 0
                        sigue = False
                        return puntaje_sala2, sigue

                if marco_opcion3.collidepoint(evento.pos):
                    pos_texto_ganaste = (330, 700)
                    rect_boton = (250, 750, 300, 80)
                    rect_opcion1 = pygame.Rect(100, 370, 0, 0)
                    rect_opcion2 = pygame.Rect(100, 370, 0, 0)
                    rect_opcion4 = pygame.Rect(100, 370, 0, 0)
                    texto_opcion3 = fuente_opciones.render("if x > 5: print('Mayor')", True, (255, 255, 255))
                    COLOR_CORRECTO = (86, 252, 25)
                    puntaje_sala2 = random.randint(10, 35)
                    sigue = True

                if marco_opcion4.collidepoint(evento.pos):
                    COLOR_INCORRECTO4 = (176, 23, 31)
                    intentos -= 1
                    if intentos == 0:
                        puntaje_sala2 = 0
                        sigue = False
                        return puntaje_sala2, sigue

                if marco_boton.collidepoint(evento.pos):
                    return puntaje_sala2, sigue

        pantalla.fill(color_fondo)

        # MUESTRO LA PREGUNTA
        pantalla.blit(texto_sala, (350, 25))
        texto_intentos = fuente_sala.render(f"Intentos restantes: {intentos}", True, COLOR_BLANCO)
        pantalla.blit(texto_intentos, (235, 50))
        marco_pregunta = pygame.draw.rect(pantalla, COLOR_BLANCO, pygame.Rect(60, 75, 690, 150), 0, 50, 50, 25, 25)
        pantalla.blit(texto_pregunta, (70, 135))

        # MUESTRO LAS OPCIONES
        marco_opcion1 = pygame.draw.rect(pantalla, COLOR_INCORRECTO1, rect_opcion1, 0, 50, 50, 25, 25)
        marco_opcion2 = pygame.draw.rect(pantalla, COLOR_INCORRECTO2, rect_opcion2, 0, 50, 50, 25, 25)
        marco_opcion3 = pygame.draw.rect(pantalla, COLOR_CORRECTO, rect_opcion3, 0, 50, 50, 25, 25)
        marco_opcion4 = pygame.draw.rect(pantalla, COLOR_INCORRECTO4, rect_opcion4, 0, 50, 50, 25, 25)

        marco_boton = pygame.draw.rect(pantalla, COLOR_BLANCO, rect_boton, 0, 50, 50, 25, 25)
        pantalla.blit(texto_opcion1, (180, 300))
        pantalla.blit(texto_opcion2, (180, 400))
        pantalla.blit(texto_opcion3, (180, 500))
        pantalla.blit(texto_opcion4, (180, 600))


        pantalla.blit(texto_ganaste,pos_texto_ganaste)
        pantalla.blit(texto_boton, (330, 775))


        pygame.display.flip()

