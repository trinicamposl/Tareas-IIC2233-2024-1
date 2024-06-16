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

LECHUGA_PATH = path.join("assets", "sprites", "lechuga.png")
ANCHO_LECHUGA = 20
ALTURA_LECHUGA = 20
TIEMPO_PASOS = 100

lista_tamano = [["novato", 3], ["intermedio", 10], ["experto", 20]]
TAMANO = {i[0]: i[1] for i in lista_tamano}

lista_nivel = [["novato", 0], ["intermedio", 1], ["experto", 2]]
NIVEL = {i[0]: i[1] for i in lista_nivel}

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
PASOS = [6, 6, 6]

pantalla_ancho = [["novato", 300], ["intermedio", 550], ["experto", 900]]
ANCHO_PANTALLA = {i[0]: i[1] for i in pantalla_ancho}

pantalla_largo = [["novato", 200], ["intermedio", 450], ["experto", 650]]
LARGO_PANTALLA = {i[0]: i[1] for i in pantalla_largo}
