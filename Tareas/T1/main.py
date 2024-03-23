from red import RedMetro
from sys import argv
from sys import exit
import os 
from funciones import imprimir_menu

nombres = argv
archivo = f"{nombres[0]}.txt"
estacion = nombres[1]
camino = os.path.join("data", archivo)
existe = os.path.exists(camino)
metro = RedMetro([], [])

if existe:
    metro.cambiar_planos(f"{nombres[0]}.txt")
    if estacion in metro.estaciones:
        print ('{:^40}'.format(f"Se cargó la red {nombres[0]}"))
        print('{:^40}'.format(f"Escogiste la estación: {nombres[1]}"))
        imprimir_menu()
        opcion = input()
        while opcion != 4 or opcion != "4":
            if opcion.isnumeric():
                if opcion == 1 or opcion == 2 or opcion == 3:

            else:
                print("El texto ingresado no es válido, por favor introduce un número entre 1 y 4")
                print ('{:^40}'.format(f"Se cargó la red {nombres[0]}"))
                print('{:^40}'.format(f"Escogiste la estación: {nombres[1]}"))
                imprimir_menu()
                opcion = input()
        

    else:
        print("La estación que escogiste no se encuentra en la red solicitada, intenta de nuevo")
else: 
    print("El archivo que escogiste no existe, intenta de nuevo")



