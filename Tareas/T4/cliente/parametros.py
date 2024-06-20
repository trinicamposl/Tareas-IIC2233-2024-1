from os import path

TIEMPO_APARICION = 28
TIEMPO_DURACION = 5
TIEMPO_TRANSICION = 2
PUNTAJE_INF = 200
CONSTANTE = 1000
ANCHO_IMAGEN = 300
ALTURA_IMAGEN = 100
ANCHO_JUEGO = 850
ALTURA_JUEGO = 620
ANCHO_LECHUGA = 20
ALTURA_LECHUGA = 20

path_musica = [["victoria", path.join("assets", "sonidos", "juego_ganado.wav")],
               ["pena", path.join("assets", "sonidos", "juego_perdido.wav")],
               ["sandia", path.join("assets", "sonidos", "obtener_sandia.wav")],
               ["fondo", path.join("assets", "sonidos", "musica_1.wav")],
               ["poop", path.join("assets", "sonidos", "poop.wav")],
               ["comer", path.join("assets", "sonidos", "comer.wav")]]
PATH_MUSICA = {i[0]: i[1] for i in path_musica}

IMAGEN_PATH = path.join("assets", "sprites", "logo.png")
POOP_PATH = path.join("assets", "sprites", "poop.png")
SANDIA_PATH = path.join("assets", "sprites", "sandia.png")
LECHUGA_PATH = path.join("assets", "sprites", "lechuga.png")

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

pasos = [[3, 37], [10, 14], [20, 7]]
PASOS = {i[0]: i[1] for i in pasos}

lista_tiempo_adicional = [["novato", 30], ["intermedio", 150], ["experto", 300]]
TIEMPO_ADICIONAL = {i[0]: i[1] for i in lista_tiempo_adicional}

lista_tiempos = [["novato", 30], ["intermedio", 300], ["experto", 600]]
TIEMPO_JUEGO = {i[0]: i[1] for i in lista_tiempos}

lista_tamano = [["novato", 3], ["intermedio", 10], ["experto", 20]]
TAMANO = {i[0]: i[1] for i in lista_tamano}

lista_tamano_inv = [[3, "novato"], [10, "intermedio"], [20, "experto"]]
TAMANO_INV = {i[0]: i[1] for i in lista_tamano_inv}


pantalla_ancho = [["novato", 350], ["intermedio", 550], ["experto", 850]]
ANCHO_PANTALLA = {i[0]: i[1] for i in pantalla_ancho}

dim = [["novato", (100, 100)], ["intermedio", (50, 50)], ["experto", (20, 20)]]
DIM = {i[0]: i[1] for i in dim}

pantalla_largo = [["novato", 200], ["intermedio", 450], ["experto", 630]]
LARGO_PANTALLA = {i[0]: i[1] for i in pantalla_largo}

texto = "Tu usuario tiene que:\n- Tener al menos una mayúscula\n"
texto_2 = "- Tener al menos un número\n- Solo tiene que utilizar letras y números"
texto_reglas = texto + texto_2

texto_perdiste = "Se te acabó el tiempo D:\n        Perdiste!"

letra = [["novato", 20], ["intermedio", 12], ["experto", 10]]
LETRA = {i[0]: i[1] for i in letra}
