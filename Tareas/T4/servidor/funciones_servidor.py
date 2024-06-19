import json
from os import path


def leer_json(path: str) -> dict:
    with open(path, encoding="utf-8") as archivo:
        return json.load(archivo)


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


def revisar(lista):
    archivo = lista[0]
    intento = lista[1]
    return intento == transformar_archivo(archivo)


def transformar_archivo(archivo):
    lista = []
    ruta = path.join("assets", "solucion_puzzles", archivo)
    with open(ruta, encoding="utf-8") as archivo:
        for linea in archivo:
            lista_2 = []
            datos = linea.strip()
            for elemento in datos:
                lista_2.append(int(elemento))
            lista.append(lista_2)
    return lista
