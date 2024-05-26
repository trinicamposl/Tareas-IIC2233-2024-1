from utilidades import Animales, Candidatos, Distritos, Locales, Votos, Ponderador


def arreglo(algo):
    if algo.__class__ != list:
        if algo.isdigit():
            algo = int(algo)
        elif "." in algo:
            algo = float(algo)
        return algo


def cambio(lista, tipo):
    if tipo == "animales":
        return Animales(*lista)
    elif tipo == "candidatos":
        return Candidatos(*lista)
    elif tipo == "distritos":
        return Distritos(*lista)
    elif tipo == "ponderadores":
        return Ponderador(*lista)
    elif tipo == "votos":
        return Votos(*lista)
    elif tipo == "distritos":
        return Distritos(*lista)
    elif tipo == "locales":
        return Locales(*lista)


def resultado(suma, contador):
    if contador == 0:
        return 0
    else:
        return suma/contador
