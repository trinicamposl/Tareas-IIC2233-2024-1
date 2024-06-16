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
TIEMPO_APARICION = 45
TIEMPO_DURACION = 10

lista_tiempo_adicional = [["novato", 30], ["intermedio", 150], ["experto", 300]]
TIEMPO_JUEGO = {i[0]: i[1] for i in lista_tiempo_adicional}

lista_tiempos = [["novato", 30], ["intermedio", 300], ["experto", 600]]
TIEMPO_JUEGO = {i[0]: i[1] for i in lista_tiempos}

LECHUGA_PATH = path.join("assets", "sprites", "lechuga.png")
ANCHO_LECHUGA = 20
ALTURA_LECHUGA = 20
TIEMPO_PASOS = 100

lista_tamano = [["novato", 3], ["intermedio", 10], ["experto", 20]]
TAMANO = {i[0]: i[1] for i in lista_tamano}

NUMERO_GRANDE = 2147483647

PATHS = [["abajo", [path.join("assets", "sprites", "pepa", "down_0.png"),
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
RUTAS = {i[0]: i[1] for i in PATHS}
PASOS = 7
pantalla_ancho = [["novato", 300], ["intermedio", 550], ["experto", 900]]
ANCHO_PANTALLA = {i[0]: i[1] for i in pantalla_ancho}

pantalla_largo = [["novato", 200], ["intermedio", 450], ["experto", 650]]
LARGO_PANTALLA = {i[0]: i[1] for i in pantalla_largo}

# pasos_diccionario_y = [["arriba", -7], ["abajo", 7], ["izquierda", 0], ["derecha", 0]]
# PASOS_Y = {i[0]: i[1] for i in pasos_diccionario_y}

# pasos_diccionario_x = [["arriba", 0], ["abajo", 0], ["izquierda", -7], ["derecha", 7]]
# PASOS_X = {i[0]: i[1] for i in pasos_diccionario_x}

# avance_diccionario_x = [["arriba", -1], ["abajo", 1], ["izquierda", 0], ["derecha", 0]]
# AVANCE_X = {i[0]: i[1] for i in avance_diccionario_x}

# avance_diccionario_Y = [["arriba", 0], ["abajo", 0], ["izquierda", -1], ["derecha", 1]]
# AVANCE_Y = {i[0]: i[1] for i in avance_diccionario_x}

POOP_PATH = path.join("assets", "sprites", "poop.png")
