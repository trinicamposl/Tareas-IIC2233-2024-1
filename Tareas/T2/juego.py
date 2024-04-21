from funciones import menu_de_inicio, menu_de_tienda
from momento_compras import compra 
from sys import exit
from clases import Ejercito
def combatir():
    pass

def comienzo_juego():
    ejercito = Ejercito()
    ronda = 1 #ARREGLARRRRR
    menu_de_inicio(ejercito.oro, ronda)
    decision = input()
    while decision != "4":
        if not decision.isnumeric():
            print("Por favor indica un NÚMERO del 1 al 4")
            menu_de_inicio(ejercito.oro, ronda)
            decision = input()
            print("*"*20)

        else:
            if decision in ["1","2","3"]:
                if decision == "1":
                    print("*"*20)
                    menu_de_tienda(ejercito.oro)
                    compra(ejercito, ronda)
                    decision = input()
                    print("*"*20)

                elif decision == "2":
                    print("*"*20)
                    ejercito.__str__()
                    print("*"*20)
                    menu_de_inicio(ejercito.oro, ronda)
                    decision = input()
                    print("*"*20)

                elif decision == "3":
                    combatir()

            else:
                print("Por favor elige un número entero ENTRE LAS OPCIONES")
                decision = input()
                print("*"*20)
    
    print("Hasta el próximo combate :D")
    exit()