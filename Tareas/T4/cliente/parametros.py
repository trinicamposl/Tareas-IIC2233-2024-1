from os import path
IMAGEN_PATH = path.join("assets", "sprites", "logo.png")
ANCHO_IMAGEN = 300
ALTURA_IMAGEN = 100
ANCHO_JUEGO = 600
ALTURA_JUEGO = 480
PATH_MUSICA_FONDO = path.join("assets", "sonidos", "musica_1.wav")
TIEMPO_APARICION = 45
TIEMPO_DURACION = 10
TIEMPO_ADICIONAL = 35
lista_tiempos = [["novato", 60], ["intermedio", 300], ["experto", 600]]
TIEMPO_JUEGO = {i[0]: i[1] for i in lista_tiempos}
PATH_LETRA = path.join("Minecraft.ttf")
LECHUGA_PATH = path.join("assets", "sprites", "lechuga.png")
ANCHO_LECHUGA = 30
ALTURA_LECHUGA = 10
lista_tamano = [["novato", 3], ["intermedio", 10], ["experto", 20]]
TAMANO = {i[0]: i[1] for i in lista_tamano}
