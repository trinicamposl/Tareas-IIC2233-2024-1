from sys import argv
from sys import exit
from funciones import archivo_correcto
from juego import comienzo_juego

nombres = argv

if len(nombres) == 2: #me dieron la cantidad correcta de parametros
    dificultad = nombres[1]
    archivo = nombres[1] + ".txt"
    if dificultad == "facil":
        if archivo_correcto(archivo)[0]:
            comienzo_juego(dificultad, 0)

        else:
            print(archivo_correcto(archivo)[1])
            exit()

    elif dificultad == "intermedio":
        if archivo_correcto(archivo)[0]:
            comienzo_juego(dificultad, 0)

        else:
            print(archivo_correcto(archivo)[1])
            exit()

    elif dificultad == "dificil":
        if archivo_correcto(archivo)[0]:
            comienzo_juego(dificultad, 0)

        else:
            print(archivo_correcto(archivo)[1])
            exit()

    else:
        print("El nivel de dificultad que escogiste no está correcto. Intenta de nuevo")
        print("Recuerda que la dificultad puede ser 'facil', 'intermedio' o 'dificil'")

        exit()

else: #me faltó la dificultad o me dieron más parámetros
    print("La cantidad de parámetros no coincide con la pedida, por favor intenta de nuevo")
    print("Recuerda que la dificultad puede ser 'facil', 'intermedio' o 'dificil'")
    exit()




