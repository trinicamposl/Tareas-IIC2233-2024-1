from typing import Generator
from os import path
from funciones import arreglo, cambio
from functools import reduce
from collections import Counter
from itertools import combinations
# CARGA DE DATOS

def cargar_datos(tipo_generator: str, tamano: str):
    nombre = f"{tipo_generator}.csv"
    ruta = path.join("data", tamano, nombre)
    with open(ruta, "r", encoding="latin-1") as archivo:
        archivo.readline()
        if tipo_generator != "locales":
            for linea in archivo:
                elementos = linea.strip().split(",")
                yield cambio(list(map(arreglo, elementos)), tipo_generator)
        else:
            for linea in archivo:
                separacion = linea.strip().split("[")
                lista = list(map(arreglo, separacion[1][:-1].split(", ")))
                datos = list(map(arreglo, separacion[0][:-1].split(",")))
                datos.append(lista)
                yield cambio(datos, tipo_generator)

# 1 GENERADOR

def animales_segun_edad(generador_animales: Generator,
    comparador: str, edad: int) -> Generator:
    if comparador == ">": #listo
        yield from map(lambda x: x.nombre, filter(lambda x: x.edad > edad, generador_animales))
    elif comparador == "<":
        yield from map(lambda x: x.nombre, filter(lambda x: x.edad < edad, generador_animales))
    else:
        yield from map(lambda x: x.nombre, filter(lambda x: x.edad  == edad, generador_animales))

def animales_que_votaron_por(generador_votos: Generator,
    id_candidato: int) -> Generator: #listo
    gen = generador_votos
    m = map(lambda x: x.id_animal_votante, filter(lambda x: x.id_candidato == id_candidato, gen))
    yield from m

def cantidad_votos_candidato(generador_votos: Generator,
    id_candidato: int) -> int: #listo
    a = map(lambda x: 1, (filter(lambda x: x.id_candidato == id_candidato, generador_votos)))
    return (reduce(lambda x, y: x + y, a, 0))

def ciudades_distritos(generador_distritos: Generator) -> Generator: #listo
    yield from {x.provincia for x in generador_distritos}

def especies_postulantes(generador_candidatos: Generator,
    postulantes: int) -> Generator: #listo?
    cantidad = Counter(x.especie for x in generador_candidatos)
    especies = (str(tipo) for tipo, cant in cantidad.items() if cant >= postulantes)
    return {x for x in especies}

def pares_candidatos(generador_candidatos: Generator) -> Generator: #listo
    lista = combinations([i.nombre for i in generador_candidatos], 2)
    arreglo = filter(lambda x: len(x) > 1, lista)
    yield from arreglo

def votos_alcalde_en_local(generador_votos: Generator, candidato: int,
    local: int) -> Generator: #listo
    gen = generador_votos
    yield from filter(lambda x: x.id_candidato == candidato and x.id_local == local, gen)

def locales_mas_votos_comuna (generador_locales: Generator,
    cantidad_minima_votantes: int, id_comuna: int) -> Generator:
    min = cantidad_minima_votantes
    gen = generador_locales
    comuna = filter(lambda x: x.id_comuna == id_comuna, gen)
    yield from map(lambda x: x.id_local, comuna)

def votos_candidato_mas_votado(generador_votos: Generator) -> Generator:
    votos = map(lambda x: x.id_candidato, generador_votos)
    mayores = Counter(votos).most_common(3)
    mayor = reduce(lambda x, y : max(x, y), mayores[0], 0)
    yield map(lambda x: x.id_voto, filter(lambda x: x.id_candidato == mayor, generador_votos))

# 2 GENERADORES

def animales_segun_edad_humana(generador_animales: Generator,
    generador_ponderadores: Generator, comparador: str,
    edad: int) -> Generator:
    # COMPLETAR
    pass

def animal_mas_viejo_edad_humana(generador_animales: Generator,
    generador_ponderadores: Generator) -> Generator:
    # COMPLETAR
    pass


def votos_por_especie(generador_candidatos: Generator,
    generador_votos: Generator) -> Generator:
    # COMPLETAR
    pass


def hallar_region(generador_distritos: Generator,
    generador_locales: Generator, id_animal: int) -> str:
    # COMPLETAR
    pass


def max_locales_distrito(generador_distritos: Generator,
    generador_locales: Generator) -> Generator:
    # COMPLETAR
    pass


def votaron_por_si_mismos(generador_candidatos: Generator,
    generador_votos: Generator) -> Generator:
    # COMPLETAR
    pass


def ganadores_por_distrito(generador_candidatos: Generator,
    generador_votos: Generator) -> Generator:
    # COMPLETAR
    pass


# 3 o MAS GENERADORES

def mismo_mes_candidato(generador_animales: Generator,
    generador_candidatos: Generator, generador_votos: Generator,
    id_candidato: str) -> Generator:
    # COMPLETAR
    pass


def edad_promedio_humana_voto_comuna(generador_animales: Generator,
    generador_ponderadores: Generator, generador_votos: Generator,
    id_candidato: int, id_comuna:int ) -> float:
    # COMPLETAR
    pass


def votos_interespecie(generador_animales: Generator,
    generador_votos: Generator, generador_candidatos: Generator,
    misma_especie: bool = False,) -> Generator:
    # COMPLETAR
    pass


def porcentaje_apoyo_especie(generador_animales: Generator,
    generador_candidatos: Generator, generador_votos: Generator) -> Generator:
    # COMPLETAR
    pass


def votos_validos(generador_animales: Generator,
    generador_votos: Generator, generador_ponderadores) -> int:
    # COMPLETAR
    pass


def cantidad_votos_especie_entre_edades(generador_animales: Generator,
    generador_votos: Generator, generador_ponderador: Generator,
    especie: str, edad_minima: int, edad_maxima: int) -> str:
    # COMPLETAR
    pass


def distrito_mas_votos_especie_bisiesto(generador_animales: Generator,
    generador_votos: Generator, generador_distritos: Generator,
    especie: str) -> str:
    # COMPLETAR 
    pass


def votos_validos_local(generador_animales: Generator,
    generador_votos: Generator, generador_ponderadores: Generator,
    id_local: int) -> Generator:
    # COMPLETAR
    pass


def votantes_validos_por_distritos(generador_animales: Generator,
    generador_distritos: Generator, generador_locales: Generator,
    generador_votos: Generator, generador_ponderadores: Generator) -> Generator:
    # COMPLETAR
    pass