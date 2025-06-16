import random
import csv

def ingreso_individual(cant_jugadores, lista_jugadores):
    for i in range(cant_jugadores):
        nombre_jugador = input(f"Ingrese su nombre jugador {i+1}: ").strip()
        while len(nombre_jugador) < 1:
            nombre_jugador = input(f"Ingrese un nombre válido: ")
        lista_jugadores.append(nombre_jugador)
    return lista_jugadores, nombre_jugador

def salas(lista_jugadores, nombre_jugador):
    for i in lista_jugadores:
        print(f'Bienvenido {i} a "Sala de Escape de Programación".\nEsto consta de 4 niveles. Tenés que responder la pregunta correctamente para avanzar, tenés solo 2 intentos por sala y un tiempo de 1 minuto.')
        preparado = False
        while preparado == False:
            pregunta_preparado = input("Estas listo(S/N)?").upper()
            if pregunta_preparado == 'N':
                print("Preparate bien y cuando quieras comenzamos!")
                pregunta_preparado = input("Estas listo(S/N)?").upper()
            else:
                print("Comencemos!")
                preparado = True
        escape(nombre_jugador)

def cargar_respuestas(csv_path, nivel):
    respuestas = list()
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for _ in range(nivel):
            linea = next(reader)
            opciones = linea[1:]
            respuestas.clear()
            respuestas.extend(opciones)
        random.shuffle(respuestas)

    for res in enumerate(respuestas, 1):
        print(res)
    return respuestas

def buscar_respuesta_correcta(respuestas, respuesta_correcta):
    encontrado = False
    i = 0
    while not encontrado and i < len(respuestas):
        if respuesta_correcta == respuestas[i]:
            respuesta_correcta = i+1
            encontrado = True
            return respuesta_correcta
        else:
            i += 1

def validar_respuesta(pregunta, opcion_correcta):
    respuesta = int(input(pregunta))
    intentos = 1
    respuesta_correcta = False
    while intentos != 0 and not respuesta_correcta:
        if respuesta == opcion_correcta:
            print("Opcion Correcta!\nAvanzando a la siguiente sala...")
            respuesta_correcta = True
            return respuesta_correcta
        else:
            intentos -= 1
            print("INCORRECTO!")
            print(f"Te queda {intentos+1} intento")
            respuesta = int(input(pregunta))
        if intentos == 0:
            print("PERDISTE! VUELVE A INTENTARLO")
            respuesta_correcta = False
            return respuesta_correcta


def escape(nombre_jugador):
    puntaje_general = 0
    puntaje_sala1 = 0
    puntaje_sala2 = 0
    puntaje_sala3 = 0
    puntaje_sala4 = 0
    completo = 'No Completó'
    print(f"Tu puntaje actual es: {puntaje_general}")
    print("-----Primera Sala-----")
    print("Pregunta: '¿Qué tipos de datos primitivos existen en Python?'")
    respuestas = cargar_respuestas('APND/ing_valid_datos/respuestas.csv', 1)
    respuesta_correcta = buscar_respuesta_correcta(respuestas, "int / float / str / boolean")
    sigue = validar_respuesta('¿Qué tipos de datos primitivos existen en Python? Elige una opción: ', respuesta_correcta)
    if sigue == True:
        puntaje_sala1 = random.randint(10, 35)
        puntaje_general += puntaje_sala1
        print(f"Tu puntaje actual es: {puntaje_general}")
        print("-----Segunda Sala-----")
        print("Pregunta: '¿Como se estructura un IF en Python?'")
        respuestas = cargar_respuestas('APND/ing_valid_datos/respuestas.csv', 2)
        respuesta_correcta = buscar_respuesta_correcta(respuestas, "if x > 5: print('Mayor')")
        sigue = validar_respuesta('¿Como se estructura un IF en Python? Elige una opción: ', respuesta_correcta)
    if sigue == True:
        puntaje_sala2 = random.randint(10, 60)
        puntaje_general += puntaje_sala2
        print(f"Tu puntaje actual es: {puntaje_general}")
        print("-----Tercera Sala-----")
        print("Pregunta: '¿Qué funcion tiene un archivo __init__?'")
        respuestas = cargar_respuestas('APND/ing_valid_datos/respuestas.csv', 3)
        respuesta_correcta = buscar_respuesta_correcta(respuestas, "Indicar que un directorio debe tratarse como un paquete de Python.")
        sigue = validar_respuesta('¿Qué funcion tiene un archivo "__init__"?', respuesta_correcta)
    if sigue == True:
        puntaje_sala3 = random.randint(10,35)
        puntaje_general += puntaje_sala3
        print(f"Tu puntaje actual es: {puntaje_general}")
        print("-----Cuarta Sala-----")
        print("Pregunta: '¿Qué diferencia hay entre deepcopy() y copy()?'")
        respuestas = cargar_respuestas('APND/ing_valid_datos/respuestas.csv', 4)
        respuesta_correcta = buscar_respuesta_correcta(respuestas, "copy() realiza una copia referencial al original y deepcopy() realiza una copia independiente")
        sigue = validar_respuesta('Qué diferencia hay entre deepcopy() y copy()?', respuesta_correcta)
        puntaje_sala4 = random.randint(10,35)
        puntaje_general += puntaje_sala4
        print(f"Tu puntaje final es: {puntaje_general}")
        completo = 'Completó'

    print("----- TABLA -----")
    print(f"{'Jugador':10} {'Sala 1':10} {'Sala 2':10} {'Sala 3':10} {'Sala 4':10} {'Total':10} {'Completo/No Completo':40}")
    print(f"{str(nombre_jugador):8} {puntaje_sala1:8} {puntaje_sala2:10} {puntaje_sala3:10} {puntaje_sala4:10} {puntaje_general:10} {completo:40}")
