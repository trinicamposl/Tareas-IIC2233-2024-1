from funciones import menu_de_tienda, revisar_unidades, lista_gatos, seleccion_gato, convertir_gato
from parametros import precio_cab, precio_mag, precio_gue, precio_armadura
from parametros import precio_cura, precio_lanza, precio_pergamino
from sys import exit
import random

def compra(Ejercito):
    eleccion = input()
    while eleccion != "8":
        if not eleccion.isnumeric():
            print("Por favor indica un número del 1 al 8")
            eleccion = input()

        else:
            if eleccion in [1,2,3,4,5,6,7,8]:
                #lista de gatos tiene (magos, caballeros, guerreros)
                if eleccion == "1": #mago
                    print("*"*20)
                    if revisar_unidades()[0]:
                        if Ejercito.oro >= precio_mag:
                            Ejercito.oro -= precio_mag
                            aleatorio = random.randint(0, len(lista_gatos[0]))
                            gato = lista_gatos[0][aleatorio]
                            Ejercito.combatientes.append(gato)
                            print(f"Has adquirido a {gato.nombre}, un {gato.tipo}")
                            print("*"*20)
                            menu_de_tienda(Ejercito.oro)
                            eleccion = input()
                        else:
                            print("No tienes oro suficiente para comprar un Gato Mago D:")
                            print("*"*20)
                            menu_de_tienda(Ejercito.oro)
                            eleccion = input()
                    else:
                        print(revisar_unidades[1])
                        exit()

                elif eleccion == "2": #guerrero
                    print("*"*20)
                    if revisar_unidades()[0]:
                        if Ejercito.oro >= precio_gue:
                            Ejercito.oro -= precio_gue
                            aleatorio = random.randint(0, len(lista_gatos[2])) #aqui se elije n°
                            gato = lista_gatos[2][aleatorio] #aqui saco el gato aleatoriamente
                            Ejercito.combatientes.append(gato)
                            print(f"Has adquirido a {gato.nombre}, un {gato.tipo}")
                            print("*"*20)
                            menu_de_tienda(Ejercito.oro)
                            eleccion = input()

                        else:
                            print("No tienes oro suficiente para comprar un Gato Guerrero D:")
                            print("*"*20)
                            menu_de_tienda(Ejercito.oro)
                            eleccion = input()
                    else:
                        print(revisar_unidades[1])
                        exit()
                
                elif eleccion == "3": #caballero
                    print("*"*20)
                    if revisar_unidades()[0]:
                        if Ejercito.oro >= precio_cab:
                            Ejercito.oro -= precio_cab
                            aleatorio = random.randint(0, len(lista_gatos[1]))
                            gato = lista_gatos[1][aleatorio]
                            Ejercito.combatientes.append(gato)
                            print(f"Has adquirido a {gato.nombre}, un {gato.tipo}")
                            print("*"*20)
                            menu_de_tienda(Ejercito.oro)
                            eleccion = input()

                        else:
                            print("No tienes oro suficiente para comprar un Gato Mago D:")
                            print("*"*20)
                            menu_de_tienda(Ejercito.oro)
                            eleccion = input()
                    else:
                        print(revisar_unidades[1])
                        exit()
                
                elif eleccion == "4": #armadura
                    opciones = []
                    for gato in Ejercito.combatientes:
                        if gato.tipo == "Gato Guerrero" or gato.tipo == "Gato Mago":
                            opciones.append(gato)
                    if len(opciones) != 0:
                        if Ejercito.oro >= precio_armadura:
                            seleccion_gato(opciones)
                            decision = input()
                            if not decision.isnumeric():
                                while not decision.isnumeric():
                                    print("Elige un número!")
                                    decision = input()
                            else:
                                while decision not in list(range(1, len(opciones) + 1)):
                                    print("Elige un número dentro de las opciones")
                                    print("*"*20)
                                    decision = input()
                                compra = opciones[int(decision)+1]
                                for elemento in Ejercito.combatientes:
                                    if elemento.nombre == compra.nombre:
                                        if elemento.tipo == "Gato Mago":
                                            elemento = CaballeroArcano(convertir_gato(elemento))
                                        else:
                                            elemento = Paladin(convertir_gato(elemento))
                                Ejercito.oro -= precio_armadura
                                print("*"*20)
                                menu_de_tienda(Ejercito.oro)
                                eleccion = input()
                               
                        else:
                            print("No tienes suficiente oro para comprar una armadura D:")
                            menu_de_tienda(Ejercito.oro)
                            eleccion = input()
                        
                    else:
                        print("No puedes utilizar este item con tu ejército actual")
                        menu_de_tienda(Ejercito.oro)
                        eleccion = input()

                elif eleccion == "5": #pergamino
                    pass

                elif eleccion == "6": #lanza
                    pass
                elif eleccion == "7": #curar_ejercito
                    pass
                elif eleccion == "8": #salir a menu
                    pass


            else:
                print("Por favor elige un número entre 1 y 8")
            