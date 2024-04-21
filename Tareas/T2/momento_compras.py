from funciones import menu_de_tienda, revisar_unidades, lista_gatos, seleccion_gato, menu_de_inicio
from clases import indice
from parametros import precio_cab, precio_mag, precio_gue, precio_armadura
from parametros import precio_cura, precio_lanza, precio_cura
from parametros import precio_pergamino as pergamino
from sys import exit
import random

precio = [precio_mag, precio_gue, precio_cab, precio_armadura, precio_lanza, pergamino, precio_cura]

def compra(ejercito, ronda):
    eleccion = input()
    while eleccion != "8":
        if not eleccion.isnumeric():
            print("*"*40)
            print("Por favor indica un NÚMERO del 1 al 8")
            print("*"*40)
            eleccion = input()

        else:
            if eleccion in ["1","2","3","4","5","6","7"]:
                #lista de gatos tiene (magos, caballeros, guerreros)
                if eleccion == "1": #mago
                    if revisar_unidades()[0]:
                        if ejercito.oro >= precio_mag:
                            ejercito.oro -= precio_mag
                            aleatorio = random.randint(0, len(lista_gatos()[0]) - 1)
                            gato = lista_gatos()[0][aleatorio]
                            ejercito.agregar_ejercito(gato)
                            print(f"Has adquirido a {gato.nombre}, un {gato.tipo}")
                            menu_de_tienda(ejercito.oro, *precio)
                            eleccion = input()
                        else:
                            print("*"*40)
                            print("No tienes oro suficiente para comprar un Gato Mago D:")
                            menu_de_tienda(ejercito.oro, *precio)
                            eleccion = input()
                    else:
                        print(revisar_unidades[1])
                        exit()

                elif eleccion == "2": #guerrero
                    if revisar_unidades()[0]:
                        if ejercito.oro >= precio_gue:
                            ejercito.oro -= precio_gue
                            aleatorio = random.randint(0, len(lista_gatos()[2]) - 1) 
                            gato = lista_gatos()[2][aleatorio]
                            ejercito.agregar_ejercito(gato)
                            print(f"Has adquirido a {gato.nombre}, un {gato.tipo}")
                            menu_de_tienda(ejercito.oro, *precio)
                            eleccion = input()

                        else:
                            print("*"*40)
                            print("No tienes oro suficiente para comprar un Gato Guerrero D:")
                            menu_de_tienda(ejercito.oro, *precio)
                            eleccion = input()
                    else:
                        print(revisar_unidades[1])
                        exit()
                
                elif eleccion == "3": #caballero
                    if revisar_unidades()[0]:
                        if ejercito.oro >= precio_cab:
                            ejercito.oro -= precio_cab
                            aleatorio = random.randint(0, len(lista_gatos()[1]) - 1)
                            gato = lista_gatos()[1][aleatorio]
                            ejercito.agregar_ejercito(gato)
                            print(f"Has adquirido a {gato.nombre}, un {gato.tipo}")
                            menu_de_tienda(ejercito.oro, *precio)
                            eleccion = input()

                        else:
                            print("*"*40)
                            print("No tienes oro suficiente para comprar un Gato Mago D:")
                            menu_de_tienda(ejercito.oro, *precio)
                            eleccion = input()
                    else:
                        print(revisar_unidades[1])
                        exit()
                
                elif eleccion == "4": #armadura
                    opciones = []
                    for gato in ejercito.combatientes:
                        if gato.tipo == "Gato Guerrero" or gato.tipo == "Gato Mago":
                            opciones.append(gato)
                    if len(opciones) != 0:
                        if ejercito.oro >= precio_armadura:
                            seleccion_gato(opciones)
                            decision = input()
                            if not decision.isnumeric():
                                while not decision.isnumeric():
                                    print("Elige un NÚMERO!")
                                    print("*"*40)
                                    decision = input()
                            if decision.isnumeric():
                                while int(decision) not in list(range(1, len(opciones)+1)):
                                    print("Elige un número DENTRO DE LAS OPCIONES!")
                                    seleccion_gato(opciones)
                                    print("*"*40)
                                    decision = input()
                                    while not decision.isnumeric():
                                        print("Elige un NÚMERO!")
                                        print("*"*40)
                                        seleccion_gato(opciones)
                                        decision = input() 
                                compra = opciones[int(decision)-1]
                                for elemento in ejercito.combatientes:
                                    if elemento.nombre == compra.nombre:
                                        cual = indice(elemento, ejercito.combatientes)
                                        ejercito.combatientes.pop(cual)
                                        nuevo = elemento.evolucionar("Armadura")
                                        ejercito.agregar_ejercito(nuevo)
                                        tipo_nuevo = nuevo.tipo
                                        break
                                print("*"*40)
                                print(f"Has evolucionado tu {compra.tipo} a {tipo_nuevo}")
                                ejercito.oro -= precio_armadura
                                menu_de_tienda(ejercito.oro, *precio)
                                eleccion = input()
                               
                        else:
                            print("*"*40)
                            print("No tienes suficiente oro para comprar una armadura D:")
                            menu_de_tienda(ejercito.oro, *precio)
                            eleccion = input()
                        
                    else:
                        print("No puedes utilizar este item con tu ejército actual")
                        menu_de_tienda(ejercito.oro, *precio)
                        eleccion = input()

                elif eleccion == "5": #pergamino
                    opciones = []
                    for gato in ejercito.combatientes:
                        if gato.tipo == "Gato Guerrero" or gato.tipo == "Gato Caballero":
                            opciones.append(gato)
                    if len(opciones) != 0:
                        if ejercito.oro >= pergamino:
                            seleccion_gato(opciones)
                            decision = input()
                            if not decision.isnumeric():
                                while not decision.isnumeric():
                                    print("Elige un NÚMERO!")
                                    print("*"*40)
                                    decision = input()
                            if decision.isnumeric():
                                while int(decision) not in list(range(1, len(opciones)+1)):
                                    print("Elige un número DENTRO DE LAS OPCIONES!")
                                    seleccion_gato(opciones)
                                    print("*"*40)
                                    decision = input()
                                    while not decision.isnumeric():
                                        print("Elige un NÚMERO!")
                                        print("*"*40)
                                        seleccion_gato(opciones)
                                        decision = input() 
                                compra = opciones[int(decision)-1]
                                for elemento in ejercito.combatientes:
                                    if elemento.nombre == compra.nombre:
                                        cual = indice(elemento, ejercito.combatientes)
                                        ejercito.combatientes.pop(cual)
                                        nuevo = elemento.evolucionar("Pergamino")
                                        ejercito.agregar_ejercito(nuevo)
                                        tipo_nuevo = nuevo.tipo
                                        break
                                print("*"*40)
                                print(f"Has evolucionado tu {compra.tipo} a {tipo_nuevo}")
                                ejercito.oro -= pergamino
                                menu_de_tienda(ejercito.oro, *precio)
                                eleccion = input()
                               
                        else:
                            print("*"*40)
                            print("No tienes suficiente oro para comprar un pergamino D:")
                            menu_de_tienda(ejercito.oro, *precio)
                            eleccion = input()
                        
                    else:
                        print("No puedes utilizar este item con tu ejército actual")
                        print("*"*40)
                        menu_de_tienda(ejercito.oro, *precio)
                        eleccion = input()

                elif eleccion == "6": #lanza
                    opciones = []
                    for gato in ejercito.combatientes:
                        if gato.tipo == "Gato Mago" or gato.tipo == "Gato Caballero":
                            opciones.append(gato)
                    if len(opciones) != 0:
                        if ejercito.oro >= precio_lanza:
                            seleccion_gato(opciones)
                            decision = input()
                            if not decision.isnumeric():
                                while not decision.isnumeric():
                                    print("Elige un NÚMERO!")
                                    print("*"*40)
                                    decision = input()
                            if decision.isnumeric():
                                while int(decision) not in list(range(1, len(opciones)+1)):
                                    print("Elige un número DENTRO DE LAS OPCIONES!")
                                    seleccion_gato(opciones)
                                    print("*"*40)
                                    decision = input()
                                    while not decision.isnumeric():
                                        print("Elige un NÚMERO!")
                                        print("*"*40)
                                        seleccion_gato(opciones)
                                        decision = input() 
                                compra = opciones[int(decision)-1]
                                for elemento in ejercito.combatientes:
                                    if elemento.nombre == compra.nombre:
                                        cual = indice(elemento, ejercito.combatientes)
                                        ejercito.combatientes.pop(cual)
                                        nuevo = elemento.evolucionar("Lanza")
                                        ejercito.agregar_ejercito(nuevo)
                                        tipo_nuevo = nuevo.tipo
                                        break
                                print("*"*40)
                                print(f"Has evolucionado tu {compra.tipo} a {tipo_nuevo}")
                                ejercito.oro -= precio_lanza
                                menu_de_tienda(ejercito.oro, *precio)
                                eleccion = input()
                               
                        else:
                            print("*"*40)
                            print("No tienes suficiente oro para comprar una lanza D:")
                            menu_de_tienda(ejercito.oro, *precio)
                            eleccion = input()
                        
                    else:
                        print("No puedes utilizar este item con tu ejército actual")
                        menu_de_tienda(ejercito.oro, *precio)
                        eleccion = input()

                elif eleccion == "7": #curar_ejercito
                    if ejercito.oro >= precio_cura:
                        for gato in ejercito.combatientes:
                            gato.curarse = precio_cura #damn
                        print("*"*40) 
                        print("Se ha curado al ejército con éxito! :D")
                        ejercito.oro -= precio_cura
                        menu_de_tienda(ejercito.oro, *precio)
                        eleccion = input()
                    else:
                        print("*"*40)
                        print("No tienes oro suficiente para curar tu ejército D:")
                        menu_de_tienda(ejercito.oro, *precio)
                        eleccion = input()                        

            else:
                print("Por favor elige un NÚMERO entre 1 y 8")
                print("*"*40)
                eleccion = input()
    
    menu_de_inicio(ejercito.oro, ronda)        

