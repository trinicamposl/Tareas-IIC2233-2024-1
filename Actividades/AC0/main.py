from entities import Item, Usuario

def crear_usuario(tieneSub: bool):
    nuevoUsuario = Usuario(tieneSub)
    print_usuario(nuevoUsuario)
    return nuevoUsuario

# Esta función debe extraer la información sobre los productos
def cargar_items(): 
    lista = []
    a = open("./utils/items.dcc", "rt")

    # Recorrido la lista de productos para instanciar cada item.  
    for linea in a.readlines():
        linea = linea.strip()
        param = linea.split(",")
        item = Item(param[0], int(param[1]), int(param[2]))
        lista.append(item)

    return lista

from utils.pretty_print import *


def main():
    # 1) Crear usuario (con o sin suscripcion)
    miUsuario = crear_usuario(True)

    # 2) Cargar los items
    listaItems = cargar_items()

    # 3) Imprimir todos los items usando los módulos de pretty_print
    print_items(listaItems)

    # 4) Agregar todos los items a la canasta del usuario
    for elemento in listaItems:
        miUsuario.agregar_item(elemento)

    # 5) Imprimir la canasta del usuario usando los módulos de pretty_print
    print_canasta(miUsuario)  

    # 6) Generar la compra desde el usuario
    miUsuario.comprar()

    # 7) Imprimir el usuario usando los módulos de pretty_print
    print_usuario(miUsuario)

if __name__ == "__main__":
    main()