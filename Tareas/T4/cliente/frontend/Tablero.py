from PyQt6.QtGui import QPixmap, QKeyEvent, QShortcut, QKeySequence
from PyQt6.QtCore import pyqtSignal, QTimer, Qt, QUrl
from PyQt6.QtWidgets import QWidget, QGridLayout, QPushButton, QLabel, QVBoxLayout
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
import parametros as p
from funciones import diccionario


class Tiempo(QWidget):
    signal_tiempo = pyqtSignal()

    def __init__(self, nivel: str):
        super().__init__()
        self.setFixedSize(200, 50)
        self.duration = p.TIEMPO_JUEGO[nivel.split("_")[0]]
        self.label2 = QLabel()
        self.label2.setText(f'Te quedan {self.duration} segundos.')
        self.label2.show()
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

    def __init__(self, nivel: str):
        self.nivel = nivel  # nombre completo ej: intermedio_1.txt
        self.nivel_2 = nivel.split("_")[0]  # nombre dificultad
        self.tamano = p.TAMANO[self.nivel_2]
        self.grid_layout = None
        self.mute = False
        self.cor_x = 0  # estas coordenadas indican exactamente dónde está pepe (pixeles)
        self.cor_y = 0

        super().__init__()
        self.setGeometry(50, 50, 100, 100)
        self.setFixedSize(p.ANCHO_PANTALLA[self.nivel_2], p.LARGO_PANTALLA[self.nivel_2])
        self.iniciar_dibujos()
        self.instalar_atajos()

    def iniciar_dibujos(self):
        self.grid_layout = QGridLayout()
        fila = 0
        columna = 0
        for i in range((self.tamano+1)**2):
            datos = f"{fila},{columna}"
            if columna == 0 or fila == 0:
                if columna == 0 and fila == 0:
                    vacio = QLabel(self)
                else:
                    vacio = QLabel(f"{diccionario(self.nivel)[datos]}", self)
                self.grid_layout.addWidget(vacio, fila, columna)
            else:
                lechuga = QLabel(self)
                lechuga.setPixmap(QPixmap(p.LECHUGA_PATH))
                lechuga.setFixedSize(p.ANCHO_LECHUGA, p.ALTURA_LECHUGA)
                self.grid_layout.addWidget(lechuga, fila, columna)

            columna += 1
            if columna > self.tamano:
                columna = 0
                fila += 1

        self.pepa = QLabel(self)
        self.pepa.setPixmap(QPixmap(p.RUTAS["abajo"][0]))
        self.pepa.setGeometry(self.cor_x, self.cor_y, p.ANCHO_LECHUGA, p.ALTURA_LECHUGA)
        self.pepa.setWindowFlags(self.pepa.windowFlags() | Qt.WindowType.WindowStaysOnTopHint)
        self.pepa.show()

        QTimer.singleShot(100, self.definir_Pepa)

        self.tiempo_original = Tiempo(self.nivel)
        self.tiempo_original.signal_tiempo.connect(self.enviar_tiempo)
        self.grid_layout.addWidget(self.tiempo_original, 0, self.tamano + 1)
        self.salir = QPushButton("Salir")
        self.salir.setFixedHeight(p.ALTURA_LECHUGA)
        self.comprobar = QPushButton("Comprobar")
        self.comprobar.setFixedHeight(p.ALTURA_LECHUGA)
        self.pausar = QPushButton("Pausar")
        self.comprobar.setFixedHeight(p.ALTURA_LECHUGA)

        self.comprobar.clicked.connect(self.enviar_info)
        self.salir.clicked.connect(self.retirada)

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
                self.grid_layout.addWidget(vacio, i, self.tamano + 1)
        self.setLayout(self.grid_layout)

    def enviar_info(self):
        pass

    def enviar_tiempo(self):
        tiempo_og = self.grid_layout.itemAtPosition(0, self.tamano + 1).widget()
        if tiempo_og and isinstance(tiempo_og, Tiempo):
            texto = tiempo_og.label2.text()
            print(texto)
            self.signal_tiempo_restante.emit(texto)

    def retirada(self):
        self.hide()
        self.signal_salir.emit()

    def definir_Pepa(self):
        self.cor_x = self.layout().itemAtPosition(1, 1).widget().geometry().x()
        self.cor_y = self.layout().itemAtPosition(1, 1).widget().geometry().y()
        self.pepa.move(self.cor_x, self.cor_y)
        self.signal_posicion.emit([self.cor_x, self.cor_y, self.tamano])

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
        self.pepa.setPixmap(QPixmap(p.RUTAS[donde][imagen]))
        self.pepa.move(*lugar)

    def silenciar(self):
        self.signal_silenciar.emit()
        self.mute = True

    def tiempo_infinito(self):
        tiempo_og = self.grid_layout.itemAtPosition(0, self.tamano + 1).widget()
        if isinstance(tiempo_og, Tiempo):
            tiempo_og.label2.setText("Te quedan ∞ segundos.")
            tiempo_og.detener()

    def agregar_tiempo(self):
        tiempo_og = self.grid_layout.itemAtPosition(0, self.tamano + 1).widget()
        if isinstance(tiempo_og, Tiempo):
            tiempo_og.aumento(p.TIEMPO_JUEGO[self.nivel_2])

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
                file_url = QUrl.fromLocalFile(p.PATH_MUSICA_POOP)
                self.media_player_mp3.setSource(file_url)
                audio = QAudioOutput(self)
                audio.setVolume(0.5)
                self.media_player_mp3.setAudioOutput(audio)
                self.media_player_mp3.play()
            imagen.setPixmap(QPixmap(p.POOP_PATH))
            QTimer.singleShot(2000, lambda: imagen.setPixmap(QPixmap(p.LECHUGA_PATH)))
        elif accion == "vaciar":
            if not self.mute:
                self.media_player_mp3 = QMediaPlayer(self)
                file_url = QUrl.fromLocalFile(p.PATH_MUSICA_COMER)
                self.media_player_mp3.setSource(file_url)
                audio = QAudioOutput(self)
                audio.setVolume(0.5)
                self.media_player_mp3.setAudioOutput(audio)
                self.media_player_mp3.play()
                QTimer.singleShot(1000, lambda: self.media_player_mp3.stop())
            imagen.setPixmap(QPixmap())
