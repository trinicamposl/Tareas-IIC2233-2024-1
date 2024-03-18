class Item:
    # Item necesita un nombre, un precio y los puntos que obtiene el usuario al comprarlo
    def __init__(self, nombre: str, precio: int, puntos: int):
        self.nombre = nombre
        self.puntos = puntos
        self.precio = precio

class Usuario:
    # Usuario tiene o no subscripción
    # Además, por defecto tiene una canasta vacía y 0 puntos adquiridos
    def __init__(self, esta_subscrito: bool):
        self.suscripcion = esta_subscrito
        self.canasta = []
        self.puntos = 0

    # Definimos un método para agregar un objeto Item a la canasta
    def agregar_item(self, item: Item):
        # Si el usuario está subscrito, recibe el doble de puntos
        if self.suscripcion:
            item.puntos *= 2
        # Luego, agregamos el item a la canasta
        self.canasta.append(item)

    # Definimos un método para comprar todos los Items de la canasta
    # y agregar los puntos ganados por la compras
    def comprar(self):
        # Por cada item, aumentamos la cantidad de puntos que tenemos
        for item in self.canasta:
            # Aquí hacemos una interacción entre una instancia Usuario con la instancia Item
            self.puntos += item.puntos
        # Limpiamos nuestra canasta
        self.canasta = []

# imprimir al usuario
def print_usuario(usuario) -> None:
    if usuario.suscripcion:
        print(f"> Usuario con suscripcion. Puntos: {usuario.puntos}")
    else:
        print(f"> Usuario sin suscripcion. Puntos: {usuario.puntos}")

# imprimir la canasta
def print_canasta(usuario) -> None:
    print("> Canasta actual del usuario:")
    for i in range(len(usuario.canasta)):
        print(
            f"\t{i + 1}) {usuario.canasta[i].nombre}: "
            f"${usuario.canasta[i].precio} / {usuario.canasta[i].puntos} puntos"
        )

# imprimir todos los items de la lista
def print_items(items) -> None:
    print("> Items para elegir:")
    for i in range(len(items)):
        print(
            f"{i+1}) {items[i].nombre}: ${items[i].precio} / {items[i].puntos} puntos"
        )
def cargar_items(): #Esta función debe extraer la información sobre los productos
    lista = []
    a = open(items.dcc, r)
    for i in a:
        i.split(",")
        b = Usuario(self, i[0], i[1], i[2])
        lista.append[b]
    return lista

def crear_usuario(tiene_suscrpicion:bool):
    print_usuario(usuario)
    return a

if __name__ == "__main__":
    crear_usuario(self)
    cargar_items()
    print_items(items)
    for i in range(len(items)):
        agregar_item(self, Item: i)
    print_canasta(usuario)
    self.comprar(self)
    print_usuario(self)
    # 7) Imprimir el usuario usando los módulos de pretty_print

