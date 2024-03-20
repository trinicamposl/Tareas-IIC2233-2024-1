def numero_estacion(lista: list, nombre: str): 
    #este método retorna cuál es el índice de la estación
    contador = 0
    for estacion in lista:
        if estacion == nombre:
            numero = contador
        contador =+1
    return numero

def hay_tunel(red, inicio, destino): 
    #este método retorna si existe un tunel o no
    numero_inicio = numero_estacion(red, inicio)
    numero_destino = numero_estacion(red, destino)
    if red[numero_inicio][numero_destino] == 0:
        return False
    else:
        return True
     
a = ["A", "B", "C", "D"]
print(numero_estacion(a,"A"))
    