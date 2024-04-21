import os
from parametros import precio_cab, precio_mag, precio_gue, precio_armadura
from parametros import precio_cura, precio_lanza, precio_pergamino
from clases import Mago, Caballero, Guerrero

def archivo_correcto(archivo):
    camino = os.path.join("data", archivo)
    with open((camino), "rt") as texto:
        lineas = texto.readlines()
        if len(lineas) == 3:
            for linea in lineas:
                jugadores = linea.split(";")
                for jugador in jugadores:
                    gato = jugador.split(",")
                    if len(gato) != 7:
                        texto = "Tu archivo no cumple con los parámetros necesario para cada"
                        return (False, (texto + " jugador. Intenta de nuevo"))
                    else:
                        if not revisar_parametros(gato[2], gato[3], gato[4], gato[5], gato[6]):
                            texto = "Los parámetros del archivo no cumplen los requisitos. "
                            return (False, texto + "Intenta de nuevo")
            return (True, 0)
                        
        else:
            return (False, "Tu archivo tiene más rondas de las que se permiten. Intenta de nuevo")

def revisar_parametros(vida_maxima, defensa, poder, agilidad, resistencia):
    rango100 = list(range(0,101))
    rango20 = list(range(1,21))
    rango10 = list(range(1,11))
    if int(vida_maxima) in rango100:
        if int(poder) in rango10:
            if int(defensa) in rango20:
                if int(agilidad) in rango10:
                    if int(resistencia) in rango10:
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

#def revisar_parametros_unidades(tipo, vida_maxima, defensa, poder, agilidad, resistencia):
    rango100 = list(range(0,101))
    rango20 = list(range(1,21))
    rango10 = list(range(1,11))
    if int(vida_maxima) in rango100:
        if int(poder) in rango10:
            if int(defensa) in rango20:
                if int(agilidad) in rango10:
                    if int(resistencia) in rango10:
                        if tipo == "MAG" or tipo == "CAB" or tipo =="GUE":
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
    else:
        return False

def menu_de_inicio(plata, ronda):
    #esto imprime mi menú de inicio (lo hice para que fuera más ordenado el main.py)
    print("*"*40)
    print('{:^40}'.format('Menú de Inicio'))
    print("")
    print('{:^40}'.format(f"Oro disponible: {plata}"))
    print('{:^38}'.format(f"Ronda actual: {ronda}"))
    print("")  
    print('{:<40}'.format('      #1 : Tienda'))
    print('{:<40}'.format('      #2 : Ejército'))
    print('{:<40}'.format('      #3 : Combatir'))
    print("")
    print('{:<40}'.format('      #4 : Salir del programa'))
    print("")
    print('{:^40}'.format('Elige tu opción; 1, 2, 3 ó 4'))
    print("*"*40)

def menu_de_tienda(plata):
    from parametros import precio_cab, precio_mag, precio_gue, precio_armadura ##revisar!!!!
    from parametros import precio_cura, precio_lanza, precio_pergamino
    #esto imprime mi menú de tienda (lo hice para que fuera más ordenado el main.py)
    print("*"*40)
    print('{:^40}'.format('Tienda'))
    print("")
    print('{:^40}'.format(f"Oro disponible: {plata}"))
    print("                                Precio")  
    print('{:<40}'.format(f'      #1 : Gato Mago              {precio_mag}'))
    print('{:<40}'.format(f'      #2 : Gato Guerrero          {precio_gue}'))
    print('{:<40}'.format(f'      #3 : Gato Caballero         {precio_cab}'))
    print('{:<40}'.format(f'      #4 : Ítem Armadura          {precio_armadura}'))
    print('{:<40}'.format(f'      #5 : Ítem Pergamino         {precio_pergamino}'))
    print('{:<40}'.format(f'      #6 : Ítem Lanza             {precio_lanza}'))
    print('{:<40}'.format(f'      #7 : Curar Ejército         {precio_cura}'))
    print("")
    print('{:<40}'.format('      #8 : Volver al Menú de Inicio'))
    print("")
    print('{:^40}'.format('Elige tu opción; 1, 2, 3, 4, 5, 6, 7 ó 8'))
    print("*"*40)

def revisar_unidades():
    """
    Esta función revisa si los gatos que puedo comprar están permitidos y tienens 
    sus parámetros correctos

    """
    camino = os.path.join("data", "unidades.txt")
    with open((camino), "rt") as texto:
        lineas = texto.readlines()
        for linea in lineas:
            gato = linea.split(",")
            if len(gato) != 7:
                texto = "Tu archivo unidades están mal hecho. No puedes jugar D:"
                return (False, texto)                
            else:  
                if revisar_parametros(gato[2], gato[3], gato[4], gato[5], gato[6]) == False:
                    texto = "Los parámetros de tu archivo unidades no cumplen los requisitos. "
                    return (False, texto + "No puedes jugar D:")
                if gato[1] != "CAB" and gato[1] != "MAG" and gato[1] != "GUE":
                    texto = "Tus unidades tenian gatos que no se pueden comprar. No puedes jugar D:"
                    return (False, texto)
        return (True, 0)

def lista_gatos(): #esta funcion me agrupa los gatos según el tipo en una lista de listas
    #me devuelve la lista en orden (magos, caballeros, guerreros) asumiendo que el archivo esta bien
    camino = os.path.join("data", "unidades.txt")
    guerreros = []
    caballeros = []
    magos = []
    with open((camino), "rt") as texto:
        lineas = texto.readlines()
        for linea in lineas:
            gato = linea.split(",")
            variables = [gato[0], gato[2], gato[3], gato[4], gato[5], gato[6]]
            if gato[1] == "MAG":
                magos.append(Mago(*variables))
            elif gato[1] == "CAB":
                caballeros.append(Caballero(*variables))
            elif gato[1] == "GUE":
                guerreros.append(Guerrero(*variables))
    return (magos, caballeros, guerreros)

def seleccion_gato(lista):
    print('{:^40}'.format('*** Selecciona un gato***'))
    print("")
    for i in range(len(lista)):
        gato = lista[i]
        print('{:<40}'.format(f'      #{i+1} : {gato.tipo}, llamado {gato.nombre}'))
    
    print('{:^40}'.format('Elige tu opción;'))

def indice(gato, lista):
    for i in range (len(lista)):
        if lista[i].nombre == gato.nombre:
            return i






