from os import path, listdir


def archivos():
    ruta = path.join("assets", "base_puzzles")
    lista = listdir(ruta)
    return sorted(lista, key=lambda x: x[3:6])


def salon_fama():
    ruta = path.join("puntaje.txt")
    with open(ruta, "r", encoding="UTF-8") as archivo:
        lista = [i.strip().split("---") for i in archivo]
        puntajes = sorted(lista, key=lambda x: int(x[1]))
        nueva = []
        for elemento in puntajes:
            nueva.append(f"{elemento[0]} - {elemento[1]}")
        return nueva


def diccionario(nivel):
    ruta = path.join("assets", "base_puzzles", nivel)
    with open(ruta, "r", encoding="UTF-8") as archivo:
        columna = archivo.readline().strip().split(";")
        fila = archivo.readline().strip().split(";")
        for i in range(len(fila)):
            if fila[i] == "-":
                fila[i] = ""
            else:
                linea = fila[i].split(",")
                fila[i] = " ".join(linea)

        for i in range(len(columna)):
            if columna[i] == "-":
                columna[i] = ""
            else:
                linea = columna[i].split(",")
                columna[i] = "\n".join(linea)

        diccionario = {}
        for i in range(len(columna)):
            diccionario["0,"+str(i + 1)] = columna[i]

        for i in range(len(fila)):
            diccionario[str(i + 1)+",0"] = fila[i]
        return diccionario
