def indice(lista: list, nombre: str): 
    #este método retorna cuál es el índice de la estación
    for numero in range (len(lista)+1):
        if lista[numero] == nombre:
           return numero

def hay_tunel(red: list, nombres_estaciones: list, inicio: str, destino: str): 
    #este método retorna si existe un tunel o no
    numero_inicio = indice(nombres_estaciones, inicio)
    numero_destino = indice(nombres_estaciones, destino)
    if red[numero_inicio][numero_destino] == 0:
        return False
    else:
        return True




    