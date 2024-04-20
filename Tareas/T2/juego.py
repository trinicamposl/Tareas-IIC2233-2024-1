from funciones import menu_de_inicio, menu_de_tienda
from momento_compras import compra 
from sys import exit

def combatir():
    pass

def comienzo_juego(Ejercito):
    menu_de_inicio()
    decision = input()
    while decision != "4":
        if not decision.isnumeric():
            print("Por favor indica un número del 1 al 4")
            menu_de_inicio()
            decision = input()

        else:
            if decision in [1,2,3,4]:
                if decision == "1":
                    menu_de_tienda()
                    compra(Ejercito)

                elif decision == "2":
                    print(Ejercito)
                    print("*"*20)
                    menu_de_tienda()
                    decision = input()

                elif decision == "3":
                    combatir()
                
                elif decision == "4":
                    print("Hasta el próximo combate :D")
                    exit()

            else:
                print("Por favor elige un número entre 1 y 4")
    
    print("Hasta el próximo combate :D")
    exit()
            

        