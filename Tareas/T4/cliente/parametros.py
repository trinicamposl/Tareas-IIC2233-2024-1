from os import path
IMAGEN_PATH = path.join("assets", "sprites", "logo.png")
ANCHO_IMAGEN = 300
ALTURA_IMAGEN = 100
ANCHO_JUEGO = 600
ALTURA_JUEGO = 480
PATH_MUSICA_FONDO = path.join("assets", "sonidos", "musica_1.wav")
PATH_MUSICA_PERDEDORA = path.join("assets", "sonidos", "juego_perdido.wav")
PATH_MUSICA_COMER = path.join("assets", "sonidos", "comer.wav")
PATH_MUSICA_POOP = path.join("assets", "sonidos", "poop.wav")
POOP_PATH = path.join("assets", "sprites", "poop.png")
SANDIA_PATH = path.join("assets", "sprites", "sandia.png")
TIEMPO_APARICION = 28
TIEMPO_DURACION = 5
TIEMPO_TRANSICION = 2
PUNTAJE_INF = 200
CONSTANTE = 1000
LECHUGA_PATH = path.join("assets", "sprites", "lechuga.png")
ANCHO_LECHUGA = 20
ALTURA_LECHUGA = 20
TIEMPO_PASOS = 100
NUMERO_GRANDE = 2147483647  # para el loop de la música, era el máximo
PASOS = 7

lista_tiempo_adicional = [["novato", 30], ["intermedio", 150], ["experto", 300]]
TIEMPO_ADICIONAL = {i[0]: i[1] for i in lista_tiempo_adicional}

lista_tiempos = [["novato", 30], ["intermedio", 300], ["experto", 600]]
TIEMPO_JUEGO = {i[0]: i[1] for i in lista_tiempos}

lista_tamano = [["novato", 3], ["intermedio", 10], ["experto", 20]]
TAMANO = {i[0]: i[1] for i in lista_tamano}

lista_tamano_inv = [[3, "novato"], [10, "intermedio"], [20, "experto"]]
TAMANO_INV = {i[0]: i[1] for i in lista_tamano_inv}

paths = [["abajo", [path.join("assets", "sprites", "pepa", "down_0.png"),
                    path.join("assets", "sprites", "pepa", "down_1.png"),
                    path.join("assets", "sprites", "pepa", "down_2.png"),
                    path.join("assets", "sprites", "pepa", "down_3.png")]],
         ["arriba", [path.join("assets", "sprites", "pepa", "up_0.png"),
                     path.join("assets", "sprites", "pepa", "up_1.png"),
                     path.join("assets", "sprites", "pepa", "up_2.png"),
                     path.join("assets", "sprites", "pepa", "up_3.png")]],
         ["izquierda", [path.join("assets", "sprites", "pepa", "left_0.png"),
                        path.join("assets", "sprites", "pepa", "left_1.png"),
                        path.join("assets", "sprites", "pepa", "left_2.png"),
                        path.join("assets", "sprites", "pepa", "left_3.png")]],
         ["derecha", [path.join("assets", "sprites", "pepa", "right_0.png"),
                      path.join("assets", "sprites", "pepa", "right_1.png"),
                      path.join("assets", "sprites", "pepa", "right_2.png"),
                      path.join("assets", "sprites", "pepa", "right_3.png")]]]
RUTAS = {i[0]: i[1] for i in paths}

pantalla_ancho = [["novato", 300], ["intermedio", 550], ["experto", 900]]
ANCHO_PANTALLA = {i[0]: i[1] for i in pantalla_ancho}

pantalla_largo = [["novato", 200], ["intermedio", 450], ["experto", 650]]
LARGO_PANTALLA = {i[0]: i[1] for i in pantalla_largo}
