from red import RedMetro
from sys import argv
from sys import exit
import os 
from funciones import imprimir_menu
from dcciudad.pyc import imprimir_red


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
                if int(opcion) == 1:
                    imprimir_red(metro.red, metro.estaciones)
                    print ('{:^40}'.format("*********************************"))
                    print ('{:^40}'.format(f"La red actual es {nombres[0]}"))
                    print('{:^40}'.format(f"Escogiste la estación: {nombres[1]}"))
                    imprimir_menu()
                    opcion = input()
                
                elif int(opcion) == 2:
                    metodo = metro.ciclo_mas_corto(estacion)
                    print (metodo)
                    print ('{:^40}'.format("*********************************"))
                    print ('{:^40}'.format(f"La red actual es {nombres[0]}"))
                    print('{:^40}'.format(f"Escogiste la estación: {nombres[1]}"))
                    imprimir_menu()
                    opcion = input()
                
                elif int(opcion) == 3:
                    print ('{:^40}'.format("Escoja su destino:"))
                    destino = input()
                    print ('{:^40}'.format("¿Cuántas estaciones intermedias desea?"))
                    p_intermedias = int(input())
                    asegurar = metro.asegurar_ruta(estacion, destino, p_intermedias)
                    print(asegurar)
                    print ('{:^40}'.format("*********************************"))
                    print ('{:^40}'.format(f"La red actual es {nombres[0]}"))
                    print('{:^40}'.format(f"Escogiste la estación: {nombres[1]}"))
                    imprimir_menu()
                    opcion = input()

                elif int(opcion) == 4:
                    exit()

                else:
                    print("El número que ingresaste no está dentro de las opciones.")
                    print("Por favor ingresa un número válido:")
                    print ('{:^40}'.format("*********************************"))
                    print ('{:^40}'.format(f"La red actual es {nombres[0]}"))
                    print('{:^40}'.format(f"Escogiste la estación: {nombres[1]}"))
                    imprimir_menu()
                    opcion = input()

            else:
                print("El texto ingresado no es válido, por favor introduce un número entre 1 y 4")
                print ('{:^40}'.format(f"La red actual es {nombres[0]}"))
                print('{:^40}'.format(f"Escogiste la estación: {nombres[1]}"))
                imprimir_menu()
                opcion = input()
        

    else:
        print("La estación que escogiste no se encuentra en la red solicitada.")
        print("Intenta correr el programa de nuevo")
        print ('{:^40}'.format("*********************************"))
else: 
    print("El archivo que escogiste no existe, intenta de nuevo")
    print("Intenta correr el programa de nuevo")
    print ('{:^40}'.format("*********************************"))
