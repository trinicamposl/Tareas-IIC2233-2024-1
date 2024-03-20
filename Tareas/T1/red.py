from dcciudad import elevar_matriz
from dcciudad import alcanzable
from funciones import indice
from funciones import hay_tunel

class RedMetro:
    def __init__(self, red: list, estaciones: list) -> None:
        self.red = red
        self.estaciones = estaciones

    def informacion_red(self) -> list:
        cantidad_estaciones = len(self.estaciones) 
        lista = []
        for estacion in self.red:
            contador = 0
            for tunel in estacion:
                contador = contador + tunel
            lista.append(contador)
        return [cantidad_estaciones, lista]

    def agregar_tunel(self, inicio: str, destino: str) -> int:
        numero_inicio = indice(self.estaciones, inicio)
        numero_destino = indice(self.estaciones, destino)
        if self.red[numero_inicio][numero_destino] == 0:
           self.red[numero_inicio][numero_destino] = 1
           return RedMetro.informacion_red(self)[1][numero_inicio]
        else:
            return -1 #ya hay tunel

    def tapar_tunel(self, inicio: str, destino: str) -> int:
        numero_inicio = indice(self.estaciones, inicio)
        numero_destino = indice(self.estaciones, destino)
        if self.red[numero_inicio][numero_destino] != 0:
           self.red[numero_inicio][numero_destino] = 0
           return RedMetro.informacion_red(self)[1][numero_inicio]
        if self.red[numero_inicio][numero_destino] == 0:
            return -1 #nunca existió el tunel
        
    def invertir_tunel(self, estacion_1: str, estacion_2: str) -> bool:
        hay_ida = hay_tunel(self.red, self.estaciones, estacion_1, estacion_2)
        hay_vuelta = hay_tunel(self.red, self.estaciones, estacion_2, estacion_1)
        if hay_ida and hay_vuelta:
            return True
        elif hay_ida and not hay_vuelta:
            RedMetro.agregar_tunel(self, estacion_2, estacion_1)
            RedMetro.tapar_tunel(self, estacion_1, estacion_2 )
            return True
        elif not hay_ida  and hay_vuelta:
            RedMetro.agregar_tunel(self, estacion_1, estacion_2)
            RedMetro.tapar_tunel(self, estacion_2, estacion_1)
            return True
        else:
            return False

    def nivel_conexiones(self, inicio: str, destino: str) -> str:
        numero_inicio = indice(self.estaciones, inicio)
        numero_destino = indice(self.estaciones, destino)
        red_2 = elevar_matriz(self.red, 2) #con un intermediario
        existe = alcanzable(self.red, numero_inicio, numero_destino)
        un_paso = hay_tunel(self.red, self.estaciones, inicio, destino)
        dos_pasos = hay_tunel(red_2, self.estaciones, inicio, destino)
        if existe:
            if un_paso:
                return "túnel directo"
            elif dos_pasos:
                return "estación intermedia"
            else:
                return "muy lejos"
        else:
            return "no hay ruta"

    def rutas_posibles(self, inicio: str, destino: str, p_intermedias: int) -> int:
        pass

    def ciclo_mas_corto(self, estacion: str) -> int:
        pass

    def estaciones_intermedias(self, inicio: str, destino: str) -> list:
        pass

    def estaciones_intermedias_avanzado(self, inicio: str, destino: str) -> list:
        pass

    def cambiar_planos(self, nombre_archivo: str) -> bool:
        pass

    def asegurar_ruta(self, inicio: str, destino: str, p_intermedias: int) -> list:
        pass