from utilidades import Animales, Candidatos, Distritos, Locales, Votos, Ponderador

def arreglo(algo):
    if algo.isdigit():
        algo = int(algo)
    elif "." in algo:
        algo = float(algo)

def cambio(lista, tipo):
    if tipo == "animales":
        return Animales(*lista)
    elif tipo == "candidatos":
        return Candidatos(*lista)
    elif tipo == "distritos":
        return Distritos(*lista)
    elif tipo == "ponderador":
        return Ponderador(*lista)
    elif tipo == "votos":
        return Votos(*lista)
    elif tipo == "distritos":
        return Distritos(*lista)