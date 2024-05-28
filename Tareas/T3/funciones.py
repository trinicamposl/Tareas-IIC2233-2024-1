from utilidades import Animales, Candidatos, Distritos, Locales, Votos, Ponderador


def arreglo(algo, tipo):
    if tipo == "lista":
        if algo[0] != "":
            for i in range(len(algo)):
                algo[i] = int(algo[i])
            return algo
        else:
            lista = []
            return lista

    else:
        algo[0] = int(algo[0])
        algo[2] = int(algo[2])
        return algo


def cambio(lista, tipo):
    if tipo == "animales":
        lista[0] = int(lista[0])
        lista[3] = int(lista[3])
        lista[4] = float(lista[4])
        lista[5] = int(lista[5])
        return Animales(*lista)

    elif tipo == "candidatos":
        lista[0] = int(lista[0])
        lista[2] = int(lista[2])
        return Candidatos(*lista)

    elif tipo == "distritos":
        lista[0] = int(lista[0])
        lista[2] = int(lista[2])
        return Distritos(*lista)

    elif tipo == "ponderadores":
        lista[1] = float(lista[1])
        return Ponderador(*lista)

    elif tipo == "votos":
        lista[0] = int(lista[0])
        lista[1] = int(lista[1])
        lista[2] = int(lista[2])
        lista[3] = int(lista[3])
        return Votos(*lista)

    elif tipo == "locales":
        return Locales(*lista)


def resultado(suma, contador):
    if contador == 0:
        return 0
    else:
        return suma/contador
