from os import path, listdir
import json


def archivos():
    ruta = path.join("assets", "base_puzzles")
    lista = listdir(ruta)
    return sorted(lista, key=lambda x: x[3:6])


def salon_fama():
    ruta = path.join("copia.txt")
    with open(ruta, "r", encoding="UTF-8") as archivo:
        lista = [i.strip().split("---") for i in archivo]
        puntajes = sorted(lista, key=lambda x: float(x[1]))
        nueva = []
        for elemento in puntajes:
            nueva.append(f"{elemento[0]} - {elemento[1]}")
        return nueva


def info(alnum, mayusc, numero):
    print(f"alnum: {alnum}, mayus: {mayusc}, numero: {numero}")
    if alnum and mayusc:
        texto = "Tu usuario tiene que:\n- Tener al menos un número\n"
    elif alnum and numero:
        texto = "Tu usuario tiene que:\n- Tener al menos una mayúscula\n"
    elif alnum and not mayusc and not numero:
        texto_1 = "Tu usuario tiene que:\n- Tener al menos una mayúscula\n"
        texto_2 = "- Tener al menos un número"
        texto = texto_1 + texto_2
    elif mayusc and numero:
        texto = "Tu usuario tiene que:\n- Contener solo letras y números"
    elif numero and not mayusc and not alnum:
        texto_1 = "Tu usuario tiene que:\n- Tener al menos una mayúscula\n"
        texto_2 = "- Contener solo letras y números"
        texto = texto_1 + texto_2
    elif mayusc and not numero and not alnum:
        texto_1 = "Tu usuario tiene que:\n"
        texto_2 = "- Tener al menos un número\n- Solo tiene que utilizar letras y números"
        texto = texto_1 + texto_2
    else:
        texto_1 = "Tu usuario tiene que:\n- Tener al menos una mayúscula\n"
        texto_2 = "- Tener al menos un número\n- Contener solo letras y números"
        texto = texto_1 + texto_2
    return texto


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
                fila[i] += " "

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


def codificar(mensaje):
    mensaje_final = bytearray()
    largo = len(mensaje).to_bytes(4, "big")
    mensaje_final += bytearray(largo)
    chunks_completos = len(mensaje) // 25
    cantidad_faltante = len(mensaje) % 25
    for i in range(0, chunks_completos):
        numero_bloque_bytes = i.to_bytes(3, "big")
        posicion_inicial = i * 25
        posicion_final = (i * 25) + 25
        bloque = mensaje[posicion_inicial:posicion_final]
        mensaje_final += bytearray(numero_bloque_bytes)
        mensaje_final += bloque

    if cantidad_faltante != 0:  # hay un chunk incompleto
        numero_bloque = chunks_completos
        numero_bloque_bytes = numero_bloque.to_bytes(3, "big")
        posicion_inicial = numero_bloque * 25
        posicion_final = (numero_bloque * 25) + cantidad_faltante
        bloque = mensaje[posicion_inicial:posicion_final]
        mensaje_final += bytearray(numero_bloque_bytes)
        mensaje_final += bloque
        for i in range(cantidad_faltante, 25):
            mensaje_final += bytearray(b'\x00')
    return mensaje_final


def decodificar(msg: bytearray) -> bytearray:
    """Decodifica un mensaje codificado"""
    mensaje_preliminar = bytearray()
    largo = decodificar_largo(msg)
    mensaje = msg[4:]
    lista_bytes = [mensaje[i:i+28] for i in range(0, len(mensaje), 28)]
    for chunk in lista_bytes:
        sub_chunk = chunk[3:]  # ignora datos
        mensaje_preliminar += sub_chunk

    mensaje_decodificado = mensaje_preliminar[:largo]  # ignorar \x00
    return mensaje_decodificado


def decodificar_largo(mensaje: bytearray) -> int:
    bytes_largo = mensaje[0:4]
    return int.from_bytes(bytes_largo, byteorder="big")


def leer_json(nombre: str) -> dict:
    ruta = path.join("backend", nombre)
    with open(ruta, encoding="utf-8") as archivo:
        return json.load(archivo)
