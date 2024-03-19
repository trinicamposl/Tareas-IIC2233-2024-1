import dcciudad
from funciones import numero_estacion
class RedMetro:
    def __init__(self, red: list, estaciones: list) -> None:
        self.red = red
        self.estaciones = estaciones


    def informacion_red(self) -> list:
        numero_estaciones = len(self.estaciones) 
        lista = []
        for estacion in range(numero_estaciones):
            contador = 0
            for tunel in range(numero_estaciones):
                contador+= tunel
            lista.append(contador)
        return [numero_estaciones, lista]

    def agregar_tunel(self, inicio: str, destino: str) -> int:
        numero_inicio = numero_estacion(self.estaciones, inicio)
        numero_destino = numero_estacion(self.estaciones, destino)
        cambio = numero_inicio, numero_destino
        if self.red[cambio] == 0:
           self.red[cambio] = 1
           return RedMetro.informacion_red(self)[1][numero_inicio]
        else:
            return -1 #ya hay tunel

    def tapar_tunel(self, inicio: str, destino: str) -> int:
        numero_inicio = numero_estacion(self.estaciones, inicio)
        numero_destino = numero_estacion(self.estaciones, destino)
        cambio = numero_inicio, numero_destino
        if self.red[cambio] != 0:
           self.red[cambio] = 0
           return RedMetro.informacion_red(self)[1][numero_inicio]
        if self.red[cambio] == 0:
            return -1 #nunca existió el tunel
        
    def invertir_tunel(self, estacion_1: str, estacion_2: str) -> bool:
        numero_inicio = numero_estacion(self.estaciones, estacion_1)
        numero_destino = numero_estacion(self.estaciones, estacion_2)
        tunel_ida = RedMetro.agregar_tunel(self, estacion_1, estacion_2) 
        tunel_vuelta = RedMetro.agregar_tunel(self, estacion_2, estacion_1) 
        if (tunel_ida == -1) and (tunel_vuelta == -1):
            return True
        elif (tunel_ida == -1) and (tunel_vuelta != -1):
            RedMetro.agregar_tunel(self, estacion_2, estacion_1)
            RedMetro.tapar_tunel(self, estacion_1, estacion_2 )
            return True
        elif (tunel_ida != -1) and (tunel_vuelta == -1):
            RedMetro.agregar_tunel(self, estacion_1, estacion_2)
            RedMetro.tapar_tunel(self, estacion_2, estacion_1)
            return True
        else:
            return False




    def nivel_conexiones(self, inicio: str, destino: str) -> str:
        pass

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