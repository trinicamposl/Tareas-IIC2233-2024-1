from copy import copy
from collections import defaultdict
from functools import reduce
from itertools import product
from typing import Generator

from parametros import RUTA_PELICULAS, RUTA_GENEROS
from utilidades import (
    Pelicula, Genero, obtener_unicos, imprimir_peliculas,
    imprimir_generos, imprimir_peliculas_genero, imprimir_dccmax
)


# ----------------------------------------------------------------------------
# Parte 1: Cargar dataset
# ----------------------------------------------------------------------------

def cargar_peliculas(ruta: str) -> Generator:
    with open(ruta, "r") as archivo:
        #id,titulo,director,año_estreno,rating_promedio
        archivo.readline()
        for linea in archivo:
            elementos = linea.strip().split(",")
            elementos[0] = int(elementos[0])
            elementos[3] = int(elementos[3])
            elementos[4] = float(elementos[4])
            yield Pelicula(*elementos)


def cargar_generos(ruta: str) -> Generator:
    with open(ruta, "r") as archivo:
        #genero,id_pelicula
        archivo.readline()
        for linea in archivo:
            elementos = linea.strip().split(",")
            elementos[1] = int(elementos[1])
            yield Genero(*elementos)


# ----------------------------------------------------------------------------
# Parte 2: Consultas sobre generadores
# ----------------------------------------------------------------------------

def obtener_directores(generador_peliculas: Generator) -> set:
    directores = map(lambda dato: dato.director, generador_peliculas)
    return obtener_unicos(directores)


def obtener_str_titulos(generador_peliculas: Generator) -> str:
    ##revisar esto
    titulos = map(lambda x: x.titulo + ", ", generador_peliculas)
    frase = reduce(lambda x, y: x + y, titulos, "")
    frase_final = frase[:len(frase)-2]
    return frase_final


def filtrar_peliculas(
    generador_peliculas: Generator,
    director: str | None = None,
    rating_min: float | None = None,
    rating_max: float | None = None
) -> filter:
    if director.__class__ == str:
        return filter(lambda x: x.director == director, generador_peliculas)

    elif rating_min.__class__ == float:
        return filter(lambda x: x.rating >= rating_min, generador_peliculas)

    elif rating_max.__class__ == float:
        return filter(lambda x: x.rating <= rating_max, generador_peliculas)



def filtrar_peliculas_por_genero(
    generador_peliculas: Generator,
    generador_generos: Generator,
    genero: str | None = None
) -> Generator:
    if genero.__class__ == str:
        id_genero = map(lambda x : x.id_pelicula, generador_generos)
        id_peliculas = map(lambda x : x.id_pelicula, generador_peliculas)
        mezcla = product(id_peliculas, id_genero)
        primer_filtro = filter(lambda x: x[:int((len(x)/2))]*2 == x, mezcla)
        arreglo = map(lambda x: x[:int((len(x)/2))], primer_filtro) #peliculas que sirven
        estan = filter(lambda x: x.id_pelicula in arreglo, generador_peliculas)
        segundo_filtro = filter(lambda x: x.genero == genero, estan)
        return segundo_filtro

    else:
        id_genero = map(lambda x : x.id_pelicula, generador_generos)
        id_peliculas = map(lambda x : x.id_pelicula, generador_peliculas)
        mezcla = product(id_peliculas, id_genero)
        primer_filtro = filter(lambda x: x[:int((len(x)/2))]*2 == x, mezcla)
        arreglo = map(lambda x: x[:int((len(x)/2))], primer_filtro)
        arreglo_2 = map(lambda x: x, arreglo)
        estan = filter(lambda x: x.id_pelicula in arreglo, generador_peliculas)
        return arreglo_2
# ----------------------------------------------------------------------------
# Parte 3: Iterables
# ----------------------------------------------------------------------------

class DCCMax:
    def __init__(self, peliculas: list) -> None:
        self.peliculas = peliculas

    def __iter__(self):
        return IteradorDCCMax(self.peliculas)


class IteradorDCCMax:
    def __init__(self, iterable_peliculas: list) -> None:
        self.peliculas = copy(iterable_peliculas)

    def __iter__(self):
        return self

    def __next__(self) -> tuple:
        if len(self.peliculas) == 0:
            raise StopIteration()
        else:
            pelicula = self.peliculas.pop(0)
            return pelicula


if __name__ == '__main__':
    print('> Cargar películas:')
    imprimir_peliculas(cargar_peliculas(RUTA_PELICULAS))
    print()

    print('> Cargar géneros')
    imprimir_generos(cargar_generos(RUTA_GENEROS), 5)
    print()

    print('> Obtener directores:')
    generador_peliculas = cargar_peliculas(RUTA_PELICULAS)
    print(list(obtener_directores(generador_peliculas)))
    print()

    print('> Obtener string títulos')
    generador_peliculas = cargar_peliculas(RUTA_PELICULAS)
    print(obtener_str_titulos(generador_peliculas))
    print()

    print('> Filtrar películas (por director):')
    generador_peliculas = cargar_peliculas(RUTA_PELICULAS)
    imprimir_peliculas(filtrar_peliculas(
        generador_peliculas, director='Christopher Nolan'
    ))
    print('\n> Filtrar películas (rating min):')
    generador_peliculas = cargar_peliculas(RUTA_PELICULAS)
    imprimir_peliculas(filtrar_peliculas(generador_peliculas, rating_min=9.1))
    print('\n> Filtrar películas (rating max):')
    generador_peliculas = cargar_peliculas(RUTA_PELICULAS)
    imprimir_peliculas(filtrar_peliculas(generador_peliculas, rating_max=8.7))
    print()

    print('> Filtrar películas por género')
    generador_peliculas = cargar_peliculas(RUTA_PELICULAS)
    generador_generos = cargar_generos(RUTA_GENEROS)
    imprimir_peliculas_genero(filtrar_peliculas_por_genero(
        generador_peliculas, generador_generos, 'Biography'
    ))
    print()

    print('> DCC Max...')
    imprimir_dccmax(DCCMax(list(cargar_peliculas(RUTA_PELICULAS))))