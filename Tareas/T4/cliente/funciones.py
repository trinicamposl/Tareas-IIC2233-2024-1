from os import path, listdir


def archivos():
    ruta = path.join("assets", "base_puzzles")
    return listdir(ruta)


def salon_fama():
    ruta = path.join("puntaje.txt")
    with open(ruta, "r", encoding="UTF-8") as archivo:
        lista = [i.strip().split("---") for i in archivo]
        puntajes = sorted(lista, key=lambda x: int(x[1]))
        nueva = []
        for elemento in puntajes:
            nueva.append(f"{elemento[0]} - {elemento[1]}")
        return nueva
