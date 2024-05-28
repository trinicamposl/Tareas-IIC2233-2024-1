from typing import Generator
from os import path
from funciones import arreglo, cambio, resultado
from functools import reduce
from collections import Counter, namedtuple
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
                yield cambio(elementos, tipo_generator)
        else:
            for linea in archivo:
                separacion = linea.strip().split("[")
                lista = list(arreglo(separacion[1][:-1].split(", "), "lista"))
                datos = list(arreglo(separacion[0][:-1].split(","), "datos"))
                datos.append(lista)
                yield cambio(datos, tipo_generator)


# 1 GENERADOR


def animales_segun_edad(generador_animales: Generator,
                        comparador: str, edad: int) -> Generator:
    if comparador == ">":  # listo
        yield from map(lambda x: x.nombre, filter(lambda x: x.edad > edad, generador_animales))
    elif comparador == "<":
        yield from map(lambda x: x.nombre, filter(lambda x: x.edad < edad, generador_animales))
    else:
        yield from map(lambda x: x.nombre, filter(lambda x: x.edad == edad, generador_animales))


def animales_que_votaron_por(generador_votos: Generator,
                             id_candidato: int) -> Generator:  # listo
    gen = generador_votos
    m = map(lambda x: x.id_animal_votante, filter(lambda x: x.id_candidato == id_candidato, gen))
    yield from m


def cantidad_votos_candidato(generador_votos: Generator,
                             id_candidato: int) -> int:  # listo
    a = map(lambda x: 1, (filter(lambda x: x.id_candidato == id_candidato, generador_votos)))
    return (reduce(lambda x, y: x + y, a, 0))


def ciudades_distritos(generador_distritos: Generator) -> Generator:  # listo
    yield from {x.provincia for x in generador_distritos}


def especies_postulantes(generador_candidatos: Generator,
                         postulantes: int) -> Generator:  # listo?
    cantidad = Counter(x.especie for x in generador_candidatos)
    especies = (str(tipo) for tipo, cant in cantidad.items() if cant >= postulantes)
    for especie in especies:
        yield especie


def pares_candidatos(generador_candidatos: Generator) -> Generator:  # listo
    lista = combinations([i.nombre for i in generador_candidatos], 2)
    arreglo = filter(lambda x: len(x) > 1, lista)
    yield from arreglo


def votos_alcalde_en_local(generador_votos: Generator, candidato: int,
                           local: int) -> Generator:  # listo
    gen = generador_votos
    yield from filter(lambda x: x.id_candidato == candidato and x.id_local == local, gen)


def locales_mas_votos_comuna(generador_locales: Generator,
                             cantidad_minima_votantes: int, id_comuna: int) -> Generator:  # listo
    min = cantidad_minima_votantes
    g = generador_locales
    c = id_comuna
    f = (x.id_local for x in g if x.id_comuna == c and len(x.id_votantes) >= min)
    yield from f


# 2 GENERADORES


def votos_candidato_mas_votado(generador_votos: Generator) -> Generator:  # listo
    copia = [i for i in generador_votos]
    mayores = Counter(voto.id_candidato for voto in copia)  # id_candidato, cantidad
    numero = mayores.most_common()[0][1]
    filt = (int(tipo) for tipo, cant in mayores.items() if cant == numero)
    inicial = 0
    for elemento in filt:
        final = inicial
        if int(elemento) > final:
            final = int(elemento)
            inicial = int(elemento)
    yield from map(lambda x: x.id_voto, filter(lambda x: x.id_candidato == final, copia))


def animales_segun_edad_humana(generador_animales: Generator,
                               generador_ponderadores: Generator, comparador: str,
                               edad: int) -> Generator:  # listo
    animales = [i for i in generador_animales]
    pond = {i.especie: i.ponderador for i in generador_ponderadores}
    if comparador == ">":
        cumplen = filter(lambda x: x if x.edad*pond[x.especie] > edad else None, animales)
    elif comparador == "<":
        cumplen = filter(lambda x: x if x.edad*pond[x.especie] < edad else None, animales)
    elif comparador == "=":
        cumplen = filter(lambda x: x if x.edad*pond[x.especie] == edad else None, animales)
    yield from map(lambda x: x.nombre, cumplen)


def animal_mas_viejo_edad_humana(generador_animales: Generator,
                                 generador_ponderadores: Generator) -> Generator:  # listo
    pond = {i.especie: i.ponderador for i in generador_ponderadores}
    animales = [i for i in generador_animales]
    edades = map(lambda x: x.edad*pond[x.especie], animales)
    edad_max = max([i for i in edades])
    utiles = filter(lambda x: x if x.edad*pond[x.especie] == edad_max else None, animales)
    yield from map(lambda x: x.nombre, utiles)


def votos_por_especie(generador_candidatos: Generator,
                      generador_votos: Generator) -> Generator:  # listo
    candidatos = [i for i in generador_candidatos]
    votos = [i for i in generador_votos]
    especie = {x.id_candidato: x.especie for x in candidatos}
    nuevo = map(lambda x: especie[x.id_candidato], votos)
    cuentas = Counter(especie for especie in nuevo)
    especies = set(i.especie for i in candidatos)
    for elemento in especies:
        yield elemento, cuentas[elemento]


def hallar_region(generador_distritos: Generator,
                  generador_locales: Generator, id_animal: int) -> str:  # listo
    dist = [i for i in generador_distritos]
    locales = [i for i in generador_locales]
    donde_vota = next(filter(lambda x: x if id_animal in x.id_votantes else None, locales))
    donde_vive = next(filter(lambda x: x if donde_vota.id_comuna == x.id_comuna else None, dist))
    return donde_vive.region


def max_locales_distrito(generador_distritos: Generator,
                         generador_locales: Generator) -> Generator:  # listo
    dist = [i for i in generador_distritos]
    loc = [i for i in generador_locales]
    l_c = {i.id_local: i.id_comuna for i in loc}
    c_d = {i.id_comuna: i.id_distrito for i in dist}
    cuentas = {i.id_local: c_d[l_c[i.id_local]] for i in loc}
    mayores = Counter(cuentas[i.id_local] for i in loc)  # id_distrito, cantidad
    numero = mayores.most_common()[0][1]  # no funciona para cuando una comuna tiene mas locales
    filt = [dist for dist, cant in mayores.items() if cant >= numero]
    sirven = filter(lambda x: x if x.id_distrito in filt else None, dist)
    listo = {i for i in map(lambda x: x.nombre, sirven)}
    yield from listo


def votaron_por_si_mismos(generador_candidatos: Generator,
                          generador_votos: Generator) -> Generator:  # listo
    gen_votos = generador_votos
    gen = generador_candidatos
    filtro = filter(lambda x: x if x.id_candidato == x.id_animal_votante else None, gen_votos)
    mismos = [x.id_candidato for x in filtro]
    final = map(lambda x: x.nombre, filter(lambda x: x if x.id_candidato in mismos else None, gen))
    yield from final


def ganadores_por_distrito(generador_candidatos: Generator,
                           generador_votos: Generator) -> Generator:  # listo
    votos = [i for i in generador_votos]
    candidatos = [i for i in generador_candidatos]
    cantidad = set(i.id_distrito_postulacion for i in candidatos)
    nombre_candidato = {x.id_candidato: x.nombre for x in candidatos}
    mayor = Counter(voto.id_candidato for voto in votos)  # id_candidato, cantidad
    totales = namedtuple("totales", ["id", "distrito", "cantidad"])
    datos = [(i.id_candidato, i.id_distrito_postulacion, mayor[i.id_candidato]) for i in candidatos]
    info = [totales(*dato) for dato in datos]
    for distrito in cantidad:
        especificos = [candidato for candidato in info if candidato.distrito == distrito]
        if len(especificos) != 1:  # no hay solo un candidato
            opciones = combinations([i for i in especificos], 2)
            for combinacion in opciones:
                mas = (max(combinacion, key=lambda x: x.cantidad)).cantidad
                sirven = [candidato for candidato in combinacion if candidato.cantidad == mas]
                for candidato in [nombre_candidato[candidato.id] for candidato in sirven]:
                    yield candidato


# 3 o MAS GENERADORES


def mismo_mes_candidato(generador_animales: Generator,
                        generador_candidatos: Generator, generador_votos: Generator,
                        id_candidato: str) -> Generator:  # listo
    if int(id_candidato) in [i.id_candidato for i in generador_candidatos]:
        id = int(id_candidato)
        a = [i for i in generador_animales]
        votos = [i for i in generador_votos]
        fecha = {i.id: i.fecha_nacimiento.split("/") for i in a}
        filtro = filter(lambda x: x.id_candidato == id, votos)
        mes = fecha[id_candidato][1]
        year = fecha[id_candidato][0]
        filtro_2 = filter(lambda x: fecha[x.id_animal_votante][0] == year or
                          fecha[x.id_animal_votante][1] == mes, filtro)
        yield from map(lambda x: x.id_animal_votante, filtro_2)


def edad_promedio_humana_voto_comuna(generador_animales: Generator,
                                     generador_ponderadores: Generator, generador_votos: Generator,
                                     id_candidato: int, id_comuna: int) -> float:  # listo
    animales = [i for i in generador_animales]
    ponderadores = [i for i in generador_ponderadores]
    pond = {i.especie: i.ponderador for i in ponderadores}
    especie = {i.id: i.especie for i in animales}
    com = {i.id: i.id_comuna for i in animales}
    edad = {i.id: i.edad for i in animales}
    utiles = filter(lambda x: x.id_candidato == id_candidato and
                    com[x.id_animal_votante] == id_comuna, generador_votos)
    lista = [i.id_animal_votante for i in utiles]
    nueva_lista = map(lambda x: edad[x]*pond[especie[x]], lista)
    return resultado(sum(nueva_lista), len(lista))


def votos_interespecie(generador_animales: Generator,
                       generador_votos: Generator, generador_candidatos: Generator,
                       misma_especie: bool = False,) -> Generator:  # listo
    an = [i for i in generador_animales]
    votos = [i for i in generador_votos]
    vot = {x.id_animal_votante: x.id_candidato for x in votos}
    especie = {x.id: x.especie for x in an}
    if misma_especie:
        util = filter(lambda x: especie[vot[x.id]] == especie[x.id] if x.id in vot else None, an)
    else:
        util = filter(lambda x: especie[vot[x.id]] != especie[x.id] if x.id in vot else None, an)
    yield from util


def porcentaje_apoyo_especie(generador_animales: Generator,
                             generador_candidatos: Generator,
                             generador_votos: Generator) -> Generator:  # listo
    an = [i for i in generador_animales]
    votos = [i for i in generador_votos]
    candidatos = [i for i in generador_candidatos]
    especie_c = {i.id_candidato: i.especie for i in candidatos}
    es = {x.id: x.especie for x in an}
    voto = {x.id_animal_votante: x.id_candidato for x in votos}
    vot = {x.id_animal_votante: x.id_candidato for x in votos}
    totales = Counter(es[i.id] for i in an)  # especie, cantidad
    voto_especie = {x.id: es[x.id] == especie_c.get(voto[x.id], "no") for x in an if x.id in vot}
    # voto_especie -> id : bool
    parciales = Counter(voto[i.id_animal_votante] for i in votos if
                        voto_especie[i.id_animal_votante] is True)
    for candidato in candidatos:
        parcial = parciales[candidato.id_candidato]
        total = totales[candidato.especie]
        if total != 0:
            porcentaje = round((parcial/total)*100)
            yield (candidato.id_candidato, porcentaje)
        else:
            yield (candidato.id_candidato, 0)


def votos_validos(generador_animales: Generator,
                  generador_votos: Generator, generador_ponderadores) -> int:  # listo
    ponderadores = [i for i in generador_ponderadores]
    animales = [i for i in generador_animales]
    v = [i for i in generador_votos]
    pond = {i.especie: float(i.ponderador) for i in ponderadores}
    specie = {x.id: x.especie for x in animales}
    ed = {x.id: int(x.edad) for x in animales}
    f = filter(lambda x: float(ed[x.id_animal_votante]*pond[specie[x.id_animal_votante]]) >= 18, v)
    return reduce(lambda x, y: x + y, map(lambda x: 1, f), 0)


def cantidad_votos_especie_entre_edades(generador_animales: Generator,
                                        generador_votos: Generator, generador_ponderador: Generator,
                                        especie: str, edad_minima: int, edad_maxima: int) -> str:
    ponderadores = [i for i in generador_ponderador]  # listo
    animales = [i for i in generador_animales]
    v = [i for i in generador_votos]
    pond = {i.especie: float(i.ponderador) for i in ponderadores}
    specie = {x.id: x.especie for x in animales}
    ed = {x.id: int(x.edad) for x in animales}
    filt = filter(lambda x: specie[x.id_animal_votante] == especie, v)
    f = filter(lambda x: edad_minima < float(ed[x.id_animal_votante] *
                                             pond[specie[x.id_animal_votante]]) < edad_maxima, filt)
    suma = reduce(lambda x, y: x + y, map(lambda x: 1, f), 0)
    texto = f"Hubo {suma} votos emitidos por animales entre {edad_minima} y {edad_maxima} años de"
    return texto + f" la especie {especie}."


def distrito_mas_votos_especie_bisiesto(generador_animales: Generator,
                                        generador_votos: Generator, generador_distritos: Generator,
                                        especie: str) -> str:  # listo
    animales = [i for i in generador_animales]
    votos = [i for i in generador_votos]
    edad = {x.id: x.fecha_nacimiento.split("/")[0] for x in animales}
    especies = {x.id: x.especie for x in animales}
    distritos = [i for i in generador_distritos]
    distrito = {x.id_comuna: x.id_distrito for x in distritos}
    aplican = filter(lambda x: especies[x.id_animal_votante] == especie and
                     int(edad[x.id_animal_votante]) % 4 == 0, votos)
    comuna = {x.id: x.id_comuna for x in animales}
    cuentas = Counter(distrito[comuna[elemento.id_animal_votante]] for elemento in aplican)
    if len(cuentas) != 0:
        numero = cuentas.most_common()[0][1]
        filt = (int(dist) for dist, cant in cuentas.items() if cant == numero)
        final = min([i for i in filt])
        texto = f"El distrito {final} fue el que tuvo más votos emitidos por animales de"
        return f"{texto} la especie {especie} nacidos en año bisiesto."
    else:
        district = min(map(lambda x: x.id_distrito, [i for i in distritos]))
        texto = f"El distrito {district} fue el que tuvo más votos emitidos por animales de"
        return f"{texto} la especie {especie} nacidos en año bisiesto."


def votos_validos_local(generador_animales: Generator,
                        generador_votos: Generator, generador_ponderadores: Generator,
                        id_local: int) -> Generator:
    ponderadores = [i for i in generador_ponderadores]  # listo
    animales = [i for i in generador_animales]
    votos = [i for i in generador_votos]
    pond = {i.especie: float(i.ponderador) for i in ponderadores}
    ed = {x.id: int(x.edad) for x in animales}
    especie = {x.id: x.especie for x in animales}
    filtro = filter(lambda x: x.id_local == id_local, votos)
    f = filter(lambda x: float(ed[x.id_animal_votante]*pond[especie[x.id_animal_votante]]) >= 18,
               filtro)
    yield from map(lambda x: x.id_voto, f)


def votantes_validos_por_distritos(generador_animales: Generator,
                                   generador_distritos: Generator, generador_locales: Generator,
                                   generador_votos: Generator,
                                   generador_ponderadores: Generator) -> Generator:
    dist = [i for i in generador_distritos]
    loc = [i for i in generador_locales]
    an = [i for i in generador_animales]
    pond = {i.especie: i.ponderador for i in generador_ponderadores}
    votos = [i for i in generador_votos]
    c_d = {i.id_comuna: i.id_distrito for i in dist}  # dist = com1*locales_en_com1
    l_c = {i.id_local: i.id_comuna for i in loc}
    especie = {i.id: i.especie for i in an}
    voto = {i.id_animal_votante: i.id_candidato for i in votos}
    edad = {i.id: float(pond[especie[i.id]]*i.edad) >= 18 for i in an}
    