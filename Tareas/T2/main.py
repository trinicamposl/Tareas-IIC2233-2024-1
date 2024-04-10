from sys import argv
from sys import exit
import os
from funciones import archivo_correcto

nombres = argv
dificultad = nombres[1]
archivo = nombres[1] + ".txt"
camino = os.path.join("data", archivo)
existe = os.path.exists(camino)

if existe:
    if len(nombres) == 2: #me dieron la cantidad correcta de parametros
        if dificultad == "facil":
            if archivo_correcto(camino)[0]:
                pass

            else:
                print(archivo_correcto(camino)[1])
                exit()

        elif dificultad == "intermedia":
            if archivo_correcto(camino)[0]:
                pass

            else:
                print(archivo_correcto(camino)[1])
                exit()

        elif dificultad == "dificil":
            if archivo_correcto(camino)[0]:
                pass

            else:
                print(archivo_correcto(camino)[1])
                exit()
        
        else:
            print("El nivel de dificultad que escogiste no está correcto. Intenta de nuevo")
            exit()

    else: #me faltó la dificultad o me dieron más parámetros 
        print("La cantidad de parámetros no coincide con la pedida, por favor intenta de nuevo")
        exit()

else:
    print("El nivel de dificultad que escogiste no está correcto. Intenta de nuevo")
    exit()



