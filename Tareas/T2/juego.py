from funciones import menu_de_inicio, menu_de_tienda, archivo_a_equipo
from momento_compras import compra 
from sys import exit
from clases import Ejercito
from parametros import precio_armadura, precio_cab, precio_gue
from parametros import precio_mag, precio_lanza, precio_cura
from parametros import precio_pergamino as pergamino

precio = [precio_mag, precio_gue, precio_cab, precio_armadura, precio_lanza, pergamino, precio_cura]

def combatir(dificultad, ejercito):
    contrincantes = archivo_a_equipo(dificultad)
    enemigo = contrincantes[ejercito.ronda]
    for i in range(3):
        if ejercito.combatir(enemigo)[0]:
            ejercito.ronda += 1
        else:
            print(ejercito.combatir(combatir)[1])
            comienzo_juego(dificultad)




def comienzo_juego(dificultad):
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
                    combatir(dificultad,ejercito)

            else:
                print("Por favor elige un número entero ENTRE LAS OPCIONES")
                decision = input()
                print("*"*40)
    
    print("Hasta el próximo combate :D")
    exit()