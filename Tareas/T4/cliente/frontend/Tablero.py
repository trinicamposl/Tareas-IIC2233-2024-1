from PyQt6.QtGui import QMouseEvent, QPixmap, QKeyEvent, QShortcut, QKeySequence, QFont
from PyQt6.QtCore import pyqtSignal, QTimer, Qt, QUrl
from PyQt6.QtWidgets import QWidget, QGridLayout, QPushButton, QLabel, QVBoxLayout
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
import parametros as p
from funciones import diccionario


class Sandia(QLabel):
    signal_apretaron_sandia = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setPixmap(QPixmap(p.SANDIA_PATH))
        self.setWindowFlags(self.windowFlags() | Qt.WindowType.WindowStaysOnTopHint)

    def mousePressEvent(self, ev: QMouseEvent | None) -> None:
        self.signal_apretaron_sandia.emit()
        super().mousePressEvent(ev)


class Tiempo(QWidget):
    signal_tiempo = pyqtSignal()

    def __init__(self, nivel: str):
        super().__init__()
        self.setFixedSize(200, 50)
        self.nivel = nivel.split("_")[0]
        self.duration = p.TIEMPO_JUEGO[self.nivel]
        self.label2 = QLabel()
        self.label2.setText(f'Te quedan {self.duration} segundos.')
        self.label2.setFont(QFont("Cascadia Mono SemiBold", 10))
        self.label2.show()
        self.label2.setAlignment(Qt.AlignmentFlag.AlignBottom)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(1000)
        self.perdiste = False

        layout = QVBoxLayout()
        layout.addWidget(self.label2)
        self.setLayout(layout)

    def update(self):
        self.label2.setText(f'Te quedan {self.duration} segundos.')
        self.duration -= 1

        if self.duration < 0:
            self.timer.stop()
        self.signal_tiempo.emit()

    def aumento(self, cuanto):
        self.duration += cuanto

    def detener(self):
        self.timer.stop()


class Tablero(QWidget):
    signal_posicion = pyqtSignal(list)
    signal_salir = pyqtSignal()
    signal_agregar_pepa = pyqtSignal()
    signal_mover = pyqtSignal(str)
    signal_silenciar = pyqtSignal()
    signal_dar_coordenadas = pyqtSignal(list)
    signal_relleno = pyqtSignal()
    signal_tiempo_restante = pyqtSignal(str)
    signal_comprobar = pyqtSignal(int)
    signal_ganaste = pyqtSignal()
    signal_perdiste = pyqtSignal()
    signal_pausa = pyqtSignal()

    def __init__(self, nivel: str):
        self.nivel = nivel  # nombre completo ej: intermedio_1.txt
        self.nivel_2 = nivel.split("_")[0]  # nombre dificultad
        self.tamano = p.TAMANO[self.nivel_2]
        self.grid_layout = None
        self.mute = False
        self.cor_x = 0  # estas coordenadas indican exactamente dónde está pepe (pixeles)
        self.cor_y = 0

        super().__init__()
        self.setGeometry(30, 40, p.ANCHO_JUEGO, p.ALTURA_JUEGO)
        self.setFixedSize(p.ANCHO_JUEGO, p.ALTURA_JUEGO)
        self.iniciar_dibujos()
        self.instalar_atajos()

    def iniciar_dibujos(self):
        self.grid_layout = QGridLayout()
        for fila in range((self.tamano + 1)):
            for columna in range(self.tamano + 1):
                datos = f"{fila},{columna}"
                if columna == 0 or fila == 0:
                    if columna == 0 and fila == 0:
                        vacio = QLabel()
                        vacio.setPixmap(QPixmap())
                        vacio.setFixedSize(*p.DIM[self.nivel_2])
                    else:
                        if fila != self.tamano + 1 and columna != self.tamano + 1:
                            vacio = QLabel(f"{diccionario(self.nivel)[datos]}", self)
                            if fila == 0:  # numeros de arriba
                                donde = Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignBottom
                                vacio.setAlignment(donde)
                            else:  # numeros de al lado
                                donde = Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignCenter
                                vacio.setAlignment(donde)
                        vacio.setFont(QFont("Cascadia Mono SemiBold", p.LETRA[self.nivel_2]))
                    self.grid_layout.addWidget(vacio, fila, columna)
                else:
                    lechuga = QLabel(self)
                    lechuga.setPixmap(QPixmap(p.LECHUGA_PATH).scaled(*p.DIM[self.nivel_2]))
                    self.grid_layout.addWidget(lechuga, fila, columna)

        self.pepa = QLabel(self)
        self.pepa.setPixmap(QPixmap(p.RUTAS["abajo"][0]).scaled(*p.DIM[self.nivel_2]))
        self.pepa.move(self.cor_x, self.cor_y)
        self.pepa.setWindowFlags(self.pepa.windowFlags() | Qt.WindowType.WindowStaysOnTopHint)
        self.pepa.show()

        QTimer.singleShot(100, self.definir_Pepa)

        self.tiempo_original = Tiempo(self.nivel)
        self.tiempo_original.signal_tiempo.connect(self.enviar_tiempo)
        self.grid_layout.addWidget(self.tiempo_original, 0, self.tamano + 1)
        self.salir = QPushButton("Salir")
        self.salir.setFont(QFont("Cascadia Mono SemiBold", p.LETRA[self.nivel_2]))
        self.salir.setFixedHeight(p.DIM[self.nivel_2][0])
        self.comprobar = QPushButton("Comprobar")
        self.comprobar.setFont(QFont("Cascadia Mono SemiBold", p.LETRA[self.nivel_2]))
        self.comprobar.setFixedHeight(p.DIM[self.nivel_2][0])
        self.pausar = QPushButton("Pausar")
        self.pausar.setFixedHeight(p.DIM[self.nivel_2][0])
        self.pausar.setFont(QFont("Cascadia Mono SemiBold", p.LETRA[self.nivel_2]))

        self.comprobar.clicked.connect(self.enviar_info)
        self.pausar.clicked.connect(self.pausa)
        self.salir.clicked.connect(self.retirada)
        self.signal_ganaste.connect(self.sonidos("victoria"))
        self.signal_perdiste.connect(self.sonidos("pena"))

        for i in range(self.tamano + 1):
            if i == 1:
                self.grid_layout.addWidget(self.salir, i, self.tamano + 1)
            elif i == 2:
                self.grid_layout.addWidget(self.comprobar, i, self.tamano + 1)
            elif i == 3:
                self.grid_layout.addWidget(self.pausar, i, self.tamano + 1)
            else:
                vacio = QLabel("")
                vacio.setPixmap(QPixmap())
                vacio.setFixedHeight(p.ANCHO_LECHUGA)
                self.grid_layout.addWidget(vacio, i, self.tamano + 1)
        self.setLayout(self.grid_layout)

        self.sandia = Sandia(self)
        self.sandia.show()
        self.sandia.signal_apretaron_sandia.connect(self.sandia_presionada)

    def enviar_info(self):
        tiempo_og = self.grid_layout.itemAtPosition(0, self.tamano + 1).widget()
        if tiempo_og and isinstance(tiempo_og, Tiempo):
            texto = tiempo_og.label2.text()
            if texto.split(" ")[2].isnumeric():
                segundos = int(texto.split(" ")[2])
            else:
                segundos = -1
        self.signal_comprobar.emit(segundos)

    def enviar_tiempo(self):
        tiempo_og = self.grid_layout.itemAtPosition(0, self.tamano + 1).widget()
        if tiempo_og and isinstance(tiempo_og, Tiempo):
            texto = tiempo_og.label2.text()
            self.signal_tiempo_restante.emit(texto)

    def retirada(self):
        self.hide()
        self.signal_salir.emit()

    def definir_Pepa(self):
        self.cor_x = self.layout().itemAtPosition(1, 1).widget().geometry().x()
        self.cor_y = self.layout().itemAtPosition(1, 1).widget().geometry().y()
        self.pepa.move(self.cor_x, self.cor_y)
        self.signal_posicion.emit([self.cor_x, self.cor_y, self.tamano])
        self.sandia.hide()

    def instalar_atajos(self) -> None:
        self.cheatcode_silenciar = QShortcut(QKeySequence("M, U, T, E"), self)
        self.cheatcode_inf = QShortcut(QKeySequence("I, N, F"), self)
        self.cheatcode_inf.activated.connect(self.tiempo_infinito)
        self.cheatcode_silenciar.activated.connect(self.silenciar)

    def keyPressEvent(self, event: QKeyEvent) -> None:
        if event.key() == Qt.Key.Key_W:
            self.signal_mover.emit("arriba")

        if event.key() == Qt.Key.Key_S:
            self.signal_mover.emit("abajo")

        if event.key() == Qt.Key.Key_A:
            self.signal_mover.emit("izquierda")

        if event.key() == Qt.Key.Key_D:
            self.signal_mover.emit("derecha")

        if event.key() == Qt.Key.Key_G:
            self.signal_relleno.emit()

    def mover_pepa(self, elemento):
        donde = elemento[0]
        imagen = elemento[1]
        lugar = elemento[2]
        self.pepa.setPixmap(QPixmap(p.RUTAS[donde][imagen]).scaled(*p.DIM[self.nivel_2]))
        self.pepa.move(*lugar)

    def silenciar(self):
        self.signal_silenciar.emit()
        self.mute = True

    def tiempo_infinito(self):
        tiempo_og = self.grid_layout.itemAtPosition(0, self.tamano + 1).widget()

        if isinstance(tiempo_og, Tiempo):
            tiempo_og.label2.setText("Te quedan ∞ segundos.")
            tiempo_og.detener()
            self.signal_tiempo_restante.emit("infinito")

    def agregar_tiempo(self):
        tiempo_og = self.grid_layout.itemAtPosition(0, self.tamano + 1).widget()
        if isinstance(tiempo_og, Tiempo):
            tiempo_og.aumento(p.TIEMPO_ADICIONAL[self.nivel_2])

    def dar_coordenadas(self, datos):
        x = self.layout().itemAtPosition(*datos).widget().geometry().x()
        y = self.layout().itemAtPosition(*datos).widget().geometry().y()
        self.signal_dar_coordenadas.emit([x, y])

    def rellenar(self, que):
        accion = que[0]
        donde = que[1]
        imagen = self.grid_layout.itemAtPosition(*donde).widget()
        if accion == "rellenar":
            if not self.mute:
                self.media_player_mp3 = QMediaPlayer(self)
                file_url = QUrl.fromLocalFile(p.PATH_MUSICA["poop"])
                self.media_player_mp3.setSource(file_url)
                audio = QAudioOutput(self)
                audio.setVolume(0.5)
                self.media_player_mp3.setAudioOutput(audio)
                self.media_player_mp3.play()
            imagen.setPixmap(QPixmap(p.POOP_PATH).scaled(*p.DIM[self.nivel_2]))
            QTimer.singleShot(p.TIEMPO_TRANSICION * 1000,
                              lambda: imagen.setPixmap(QPixmap(p.LECHUGA_PATH).
                                                       scaled(*p.DIM[self.nivel_2])))
        elif accion == "vaciar":
            if not self.mute:
                self.media_player_mp3 = QMediaPlayer(self)
                file_url = QUrl.fromLocalFile(p.PATH_MUSICA["comer"])
                self.media_player_mp3.setSource(file_url)
                audio = QAudioOutput(self)
                audio.setVolume(0.5)
                self.media_player_mp3.setAudioOutput(audio)
                self.media_player_mp3.play()
                QTimer.singleShot(1000, lambda: self.media_player_mp3.stop())
            imagen.setPixmap(QPixmap())

    def aparecer_sandia(self, datos):
        self.sandia.show()
        self.sandia.move(*datos)
        self.empezar_tiempo_sandia()

    def sandia_presionada(self):
        self.sandia.hide()
        self.sonidos("sandia")
        self.agregar_tiempo()

    def empezar_tiempo_sandia(self):
        QTimer.singleShot(p.TIEMPO_DURACION*1000, lambda: self.revisar_sandia())

    def revisar_sandia(self):
        if self.sandia.isVisible:
            self.sandia.hide()

    def sonidos(self, que):
        if not self.mute:
            self.media_player_mp3 = QMediaPlayer(self)
            file_url = QUrl.fromLocalFile(p.PATH_MUSICA[que])
            self.media_player_mp3.setSource(file_url)
            audio = QAudioOutput(self)
            audio.setVolume(0.5)
            self.media_player_mp3.setAudioOutput(audio)
            self.media_player_mp3.play()

    def pausa(self):
        tiempo_og = self.grid_layout.itemAtPosition(0, self.tamano + 1).widget()
        if isinstance(tiempo_og, Tiempo):
            if tiempo_og.label2.text() != "Te quedan ∞ segundos.":
                tiempo_og.timer.stop()
        self.signal_pausa.emit()

    def despausa(self):
        tiempo_og = self.grid_layout.itemAtPosition(0, self.tamano + 1).widget()
        if isinstance(tiempo_og, Tiempo):
            if tiempo_og.label2.text() != "Te quedan ∞ segundos.":
                tiempo_og.timer.start()
