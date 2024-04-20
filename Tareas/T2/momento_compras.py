from funciones import menu_de_tienda, revisar_unidades, lista_gatos
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
                if eleccion == "1":
                    print("*"*20)
                    if revisar_unidades()[0]:
                        if Ejercito.oro >= precio_mag:
                            Ejercito.oro -= precio_mag
                            aleatorio = random.randint(0, len(lista_gatos[0]))
                            gato = lista_gatos[0][aleatorio]
                            Ejercito.combatientes.append(gato)
                        else:
                            print("No tienes oro suficiente para comprar un Gato Mago D:")
                            print("*"*20)
                            menu_de_tienda()
                            eleccion = input()
                    else:
                        print(revisar_unidades[1])
                        exit()


                elif eleccion == "2":
                    print("*"*20)
                    if revisar_unidades()[0]:
                        if Ejercito.oro >= precio_gue:
                            Ejercito.oro -= precio_gue
                            aleatorio = random.randint(0, len(lista_gatos[2])) #aqui se elije n°
                            gato = lista_gatos[2][aleatorio] #aqui saco el gato aleatoriamente
                            Ejercito.combatientes.append(gato)
                        else:
                            print("No tienes oro suficiente para comprar un Gato Guerrero D:")
                            print("*"*20)
                            menu_de_tienda()
                            eleccion = input()
                    else:
                        print(revisar_unidades[1])
                        exit()
                
                elif eleccion == "3":
                    print("*"*20)
                    if revisar_unidades()[0]:
                        if Ejercito.oro >= precio_cab:
                            Ejercito.oro -= precio_cab
                            aleatorio = random.randint(0, len(lista_gatos[1]))
                            gato = lista_gatos[1][aleatorio]
                            Ejercito.combatientes.append(gato)
                        else:
                            print("No tienes oro suficiente para comprar un Gato Guerrero D:")
                            print("*"*20)
                            menu_de_tienda()
                            eleccion = input()
                    else:
                        print(revisar_unidades[1])
                        exit()
                
                elif eleccion == "4":
                    pass
                elif eleccion == "5":
                    pass
                elif eleccion == "6":
                    pass
                elif eleccion == "7":
                    pass
                elif eleccion == "8":
                    pass


            else:
                print("Por favor elige un número entre 1 y 8")
            