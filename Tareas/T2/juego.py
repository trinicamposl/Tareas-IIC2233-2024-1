from funciones import menu_de_inicio, menu_de_tienda, archivo_a_equipo
from momento_compras import compra
from sys import exit
from clases import Ejercito
from parametros import PRECIO_ARMADURA, PRECIO_CAB, PRECIO_GUE
from parametros import PRECIO_MAG, PRECIO_LANZA, PRECIO_CURA, ORO_GANADO
from parametros import PRECIO_PERGAMINO as pergamino

precio = [PRECIO_MAG, PRECIO_GUE, PRECIO_CAB, PRECIO_ARMADURA, PRECIO_LANZA, pergamino, PRECIO_CURA]

def combatir_funcion(dificultad, ejercito):
    contrincantes = archivo_a_equipo(dificultad)
    enemigo = contrincantes[ejercito.ronda - 1]
    enemigo_clase = Ejercito()
    for elemento in enemigo:
        enemigo_clase.agregar_ejercito(elemento)
    if ejercito.combatir(enemigo_clase)[0]:
        print((ejercito.combatir(enemigo_clase))[1])
        ejercito.oro += ORO_GANADO
        ejercito.ronda += 1
        if ejercito.ronda == 4:
            print("Has ganado!!!!")
            print("Lograste vencer a Gatochico, ahora puedes dormir en paz :D")
            exit()
        comienzo_juego(dificultad, ejercito)

    else:
        print(ejercito.combatir(enemigo_clase)[1])
        comienzo_juego(dificultad, 0)
    return enemigo




def comienzo_juego(dificultad, ejercito):
    if ejercito == 0:
        ejercito = Ejercito()
    menu_de_inicio(ejercito.oro, ejercito.ronda)
    decision = input()
    while decision != "4":
        if not decision.isnumeric():
            print("*"*40)
            print("Por favor indica un NÚMERO del 1 al 4")
            menu_de_inicio(ejercito.oro, ejercito.ronda)
            decision = input()
            print("*"*40)

        else:
            if decision in ["1","2","3"]:
                if decision == "1":
                    menu_de_tienda(ejercito.oro, *precio)
                    compra(ejercito, ejercito.ronda)
                    decision = input()
                    print("*"*40)

                elif decision == "2":
                    print("*"*40)
                    ejercito.__str__()
                    print("*"*40)
                    menu_de_inicio(ejercito.oro, ejercito.ronda)
                    decision = input()
                    print("*"*40)

                elif decision == "3":
                    if len(ejercito.combatientes) == 0:
                        print("No tienes ningun combatiente, no puedes pelear aún")
                        comienzo_juego(dificultad)
                    combatir_funcion(dificultad, ejercito)

            else:
                print("Por favor elige un número entero ENTRE LAS OPCIONES")
                menu_de_inicio(ejercito.oro, ejercito.ronda)
                decision = input()
                print("*"*40)

    print("Hasta el próximo combate :D")
    exit()