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

def imprimir_menu():
    #esto imprime mi menú (lo hice para que fuera más ordenado el main.py)
    print('{:^40}'.format('Menú de Opciones'))
    print('{:<40}'.format('      #1 : Mostrar red'))
    print('{:<40}'.format('      #2 : Encontrar ciclo más corto'))
    print('{:<40}'.format('      #3 : Asegurar ruta'))
    print('{:<40}'.format('      #4 : Salir del programa'))
    print('{:^40}'.format('Eliga su opción; 1, 2, 3 o 4'))