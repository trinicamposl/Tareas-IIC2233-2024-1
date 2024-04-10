import os

def archivo_correcto(archivo):
    camino = os.path.join("data", archivo)
    with open((camino), "rt") as texto:
        lineas = texto.readlines()
        if len(lineas) == 3:
            tres_rondas = []
            ronda = []
            for linea in lineas:
                jugadores = linea.split(";")
                for jugador in jugadores:
                    gato = jugador.split(",")
                    if len(gato) != 7:
                        texto = "Tu archivo no cumple con los parámetros necesario para cada"
                        return (False, (texto + " jugador. Intenta de nuevo"))
                    else:
                        orden = [gato[1], gato[2], gato[3], gato[4], gato[5], gato[6]]   
                        if revisar_parametros(orden) == False:
                            texto = "Los parámetros del archivo no cumplen los requisitos. "
                            return (False, texto + "Intenta de nuevo")
            return (True, 0)
                        
        else:
            return (False, "Tu archivo tiene más rondas de las que se permiten. Intenta de nuevo")

def revisar_parametros(vida_maxima, vida, poder, defensa, agilidad, resistencia):
    rango100 = list(range(1,100))
    rango20 = list(range(20))
    rango10 = list(range(10))
    if int(vida_maxima) in rango100:
        if int(vida) >= 0 and int(vida) <= int(vida_maxima):
            if poder in rango10:
                if defensa in rango20:
                    if agilidad in rango10:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False





    