from dcciudad import elevar_matriz
from dcciudad import alcanzable
from funciones import indice
from funciones import hay_tunel
import os 

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
        numero_inicio = indice(self.estaciones, inicio)
        numero_final = indice(self.estaciones, destino)
        red = elevar_matriz(self.red, p_intermedias + 1)
        cuantas = red[numero_inicio][numero_final]
        return cuantas

    def ciclo_mas_corto(self, estacion: str) -> int:
        for numero in range (1, len(self.estaciones)+1):
            red = elevar_matriz(self.red, numero)
            tunel = hay_tunel(red, self.estaciones, estacion, estacion)
            if tunel:
                return numero -1
        return -1  

    def estaciones_intermedias(self, inicio: str, destino: str) -> list:
        numero_inicio = indice(self.estaciones, inicio)
        numero_final = indice(self.estaciones, destino)
        lista = []
        for numero in range (len(self.estaciones)):
            if self.red[numero_inicio][numero] == 1:
                lista.append(numero) #esto toma todos los caminos que pueden salir del inicio
        lista_intermedios = []
        for estacion in lista:
            if self.red[estacion][numero_final] == 1:
                lista_intermedios.append(self.estaciones[estacion])
        return lista_intermedios

    def estaciones_intermedias_avanzado(self, inicio: str, destino: str) -> list:
        numero_inicio = indice(self.estaciones, inicio)
        numero_final = indice(self.estaciones, destino)
        salen = []
        for numero in range (len(self.estaciones)):
            if self.red[numero_inicio][numero] == 1:
                salen.append(numero) #toma los caminos a donde se puede salir del inicio
        llegan = []
        for numero in range (len(self.estaciones)):
            if self.red[numero][numero_final] == 1:
                llegan.append(numero) #toma todos los caminos que pueden llegar al final
        rutas = []
        for tren in salen:
            for metro in llegan:
                if self.red[tren][metro] == 1:
                    estacion_1 = self.estaciones[tren]
                    estacion_2 = self.estaciones[metro]
                    rutas.append([estacion_1, estacion_2])
        return rutas
    
    def cambiar_planos(self, nombre_archivo: str) -> bool:
        camino = os.path.join("data", nombre_archivo)
        existe = os.path.exists(camino)
        if existe:
            with open((camino), "rt") as texto:
                n = int(texto.readline())
                estaciones = []
                for i in range (n):
                    estaciones.append(texto.readline().strip())
                numeros = texto.readline().split(",")

                for i in range (len(numeros)):
                            numeros[i] = int(numeros[i]) 
                
                red = []
                for i in range(0,n**2, n):
                    red.append(numeros[i:i+n])  
                    #esta lista en teoría va separando los nombres de las estaciones

                self.red = red 
                self.estaciones = estaciones
                return True
        else:
            return False

    def asegurar_ruta(self, inicio: str, destino: str, p_intermedias: int) -> list:
        numero_inicio = indice(self.estaciones, inicio)
        numero_final = indice(self.estaciones, destino)
        nueva_red = self.red[:]
        red_pedida = elevar_matriz(self.red, p_intermedias + 1)
        if p_intermedias == 0:
            if self.red[numero_inicio][numero_final] == 1:
                return nueva_red
            else:
                return []
        if p_intermedias == 1:
            lista = []
            for numero in range (len(self.estaciones)):
                if self.red[numero_inicio][numero] == 1:
                    lista.append(numero) #esto toma todos los caminos que pueden salir del inicio
            lista_intermedios = []
            for estacion in lista:
                if self.red[estacion][numero_final] == 1:
                    lista_intermedios.append(self.estaciones[estacion]) #esto toma los que llegan
            for columna in range (len(self.estaciones)):
                for fila in range (len(self.estaciones)):
                    nueva_red[columna][fila] = 0 #acá reseteo toda la lista a 0
            for i in range (len(lista_intermedios) +1):
                intermedio = indice(self.estaciones, lista_intermedios[i])
                nueva_red[numero_inicio][intermedio] = 1
                nueva_red[intermedio][numero_final] = 1
                if alcanzable(nueva_red, numero_inicio, numero_final):
                    return nueva_red
            return []
        if p_intermedias == 2:
            salen = []
            for numero in range (len(self.estaciones)):
                if self.red[numero_inicio][numero] == 1:
                    salen.append(numero) #toma los caminos a donde se puede salir del inicio
            llegan = []
            for numero in range (len(self.estaciones)):
                if self.red[numero][numero_final] == 1:
                    llegan.append(numero) #toma todos los caminos que pueden llegar al final
            rutas = []
            for tren in salen:
                for metro in llegan:
                    if self.red[tren][metro] == 1:
                        estacion_1 = self.estaciones[tren]
                        estacion_2 = self.estaciones[metro]
                        rutas.append([estacion_1, estacion_2]) #lista de intermedias 
            for columna in range (len(self.estaciones)):
                for fila in range (len(self.estaciones)):
                    nueva_red[columna][fila] = 0 #acá reseteo toda la lista a 0
            for elemento in rutas:
                intermedio_1 = elemento[0]
                intermedio_2 = elemento[1]
                int_1 = indice(self.estaciones, intermedio_1)
                int_2 = indice(self.estaciones, intermedio_2)
                nueva_red[numero_inicio][int_1] = 1
                nueva_red[int_1][int_2] = 1
                nueva_red[int_2][numero_final] = 1
                if alcanzable(nueva_red, numero_inicio, numero_final):
                    return nueva_red
            return []
        if p_intermedias == 3:
            salen = []
            for numero in range (len(self.estaciones)):
                if self.red[numero_inicio][numero] == 1:
                    salen.append(numero) #toma los caminos a donde se puede salir del inicio
            llegan = []
            for numero in range (len(self.estaciones)):
                if self.red[numero][numero_final] == 1:
                    llegan.append(numero) #toma todos los caminos que pueden llegar al final
            rutas = []
            for tren in salen:
                for metro in llegan:
                    if self.red[tren][metro] == 1:
                        estacion_1 = self.estaciones[tren]
                        estacion_2 = self.estaciones[metro]
                        rutas.append([estacion_1, estacion_2]) #lista de intermedias 
            for columna in range (len(self.estaciones)):
                for fila in range (len(self.estaciones)):
                    nueva_red[columna][fila] = 0 #acá reseteo toda la lista a 0
            for elemento in rutas:
                intermedio_1 = elemento[0]
                intermedio_2 = elemento[1]
                int_1 = indice(self.estaciones, intermedio_1)
                int_2 = indice(self.estaciones, intermedio_2)
                nueva_red[numero_inicio][int_1] = 1
                nueva_red[int_1][int_2] = 1
                nueva_red[int_2][numero_final] = 1
                if alcanzable(nueva_red, numero_inicio, numero_final):
                    return nueva_red
            return []

               
    
                