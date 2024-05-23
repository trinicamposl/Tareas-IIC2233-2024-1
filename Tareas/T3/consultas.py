from typing import Generator
from os import join
from utilidades
# ----------------------------------------------------------------------
# COMPLETAR
# ----------------------------------------------------------------------

# CARGA DE DATOS

def cargar_datos(tipo_generator: str, tamano: str):
    nombre = f"{tipo_generator}".cvs
    ruta = join("test_publicos", "data", tamano, nombre)
    tipo = tipo_generator[0].uppercase() + tipo_generator[1:]
    with open(ruta, "r", encoding = latin-1) as archivo:
        #id,titulo,director,año_estreno,rating_promedio
        archivo.readline()
        for linea in archivo:
            elementos = linea.strip().split(",")
            elementos[0] = int(elementos[0])
            elementos[3] = int(elementos[3])
            elementos[4] = float(elementos[4])
            yield tipo(*elementos)

# 1 GENERADOR

def animales_segun_edad(generador_animales: Generator,
    comparador: str, edad: int) -> Generator:
    # COMPLETAR
    pass


def animales_que_votaron_por(generador_votos: Generator,
    id_candidato: int) -> Generator:    
    # COMPLETAR
    pass


def cantidad_votos_candidato(generador_votos: Generator,
    id_candidato: int) -> int:
    # COMPLETAR
    pass


def ciudades_distritos(generador_distritos: Generator) -> Generator:
    # COMPLETAR
    pass


def especies_postulantes(generador_candidatos: Generator,
    postulantes: int) ->Generator:
    # COMPLETAR
    pass


def pares_candidatos(generador_candidatos: Generator) -> Generator:
    # COMPLETAR
    pass


def votos_alcalde_en_local(generador_votos: Generator, candidato: int,
    local: int) -> Generator:
    # COMPLETAR
    pass


def locales_mas_votos_comuna (generador_locales: Generator,
    cantidad_minima_votantes: int, id_comuna: int) -> Generator:
    # COMPLETAR
    pass


def votos_candidato_mas_votado(generador_votos: Generator) -> Generator:
    # COMPLETAR 
    pass


def animales_segun_edad_humana(generador_animales: Generator,
    generador_ponderadores: Generator, comparador: str,
    edad: int) -> Generator:
    # COMPLETAR
    pass


# 2 GENERADORES

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