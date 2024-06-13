from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtGui import QPixmap, QKeyEvent, QFont
from PyQt6.QtCore import Qt, pyqtSignal, QUrl
from PyQt6.QtWidgets import QHBoxLayout, QWidget, QComboBox, QFormLayout, QLineEdit
from PyQt6.QtWidgets import QLabel, QPushButton, QScrollArea, QVBoxLayout, QApplication
from funciones import salon_fama, archivos
import parametros as p
import sys


class VentanaSala(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setGeometry(0, 0, 500, 600)
        self.setWindowTitle('Salón de la Fama')
        # salón de la fama?
        self.scroll = QScrollArea()
        self.widget = QWidget()
        self.vbox = QVBoxLayout()
        jugadores = reversed(salon_fama())
        for elemento in jugadores:
            object = QLabel(elemento)
            self.vbox.addWidget(object)

        self.widget.setLayout(self.vbox)

        # Scroll Area Properties
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)
        layout_principal = QVBoxLayout()
        layout_principal.addWidget(self.scroll)
        self.setLayout(layout_principal)


class VentanaInicio(QWidget):

    signal_intentar_empezar = pyqtSignal(list)
    signal_empezar = pyqtSignal(list)
    signal_usuario = pyqtSignal(str)

    def __init__(self) -> None:

        super().__init__()
        self.iniciar_dibujos()
        self.iniciar_musica()

    def iniciar_dibujos(self) -> None:
        self.setGeometry(30, 50, p.ANCHO_JUEGO, p.ALTURA_JUEGO)
        self.setWindowTitle("Ventana de Inicio")
        # Creamos el selector que vamos a necesitar en nuestra ventana de Inicio
        self.selector_puzzle = QComboBox(self)
        self.selector_puzzle.addItems(reversed(archivos()))
        # Creamos el usuario
        self.usuario = QFormLayout()
        self.usuario.addRow("Elige tu usuario:", QLineEdit())
        # Creamos el selector de nivel
        self.selector = QFormLayout()
        self.selector.addRow("Elige el nivel:", self.selector_puzzle)
        # Creamos el botón de inicio
        self.boton_ingresar = QPushButton("Comenzar juego", self)
        self.boton_salir = QPushButton("Salir", self)
        # Creamos imagen
        self.imagen = QLabel(self)
        self.imagen.setGeometry(0, 0, p.ANCHO_IMAGEN, p.ALTURA_IMAGEN)
        self.imagen.setPixmap(QPixmap(p.IMAGEN_PATH))
        # Creamos el layout de nuestra ventana y agregamos los elementos
        self.sala = VentanaSala()
        sala = QVBoxLayout()
        sala.addWidget(QLabel("   Salón de la Fama", self))
        sala.addWidget(self.sala)

        layout_1 = QHBoxLayout()  # botones
        layout_1.addStretch()
        layout_1.addWidget(self.boton_ingresar)
        layout_1.addWidget(self.boton_salir)

        layout_2 = QVBoxLayout()  # selectores
        layout_2.addLayout(self.selector)
        layout_2.addStretch()
        layout_2.addLayout(self.usuario)

        layout_3 = QVBoxLayout()  # botones + selectores
        layout_3.addLayout(layout_2)
        layout_3.addStretch()
        layout_3.addLayout(layout_1)

        layout_4 = QHBoxLayout()  # botones, selectores y salon
        layout_4.addLayout(sala)
        layout_4.addSpacing(20)
        layout_4.addLayout(layout_3)

        logo = QHBoxLayout()  # imagen
        logo.addStretch()
        logo.addWidget(self.imagen)
        logo.addStretch()

        layout = QVBoxLayout()  # todo
        layout.addLayout(logo)
        layout.addLayout(layout_4)

        self.setLayout(layout)
        self.show()

        self.boton_ingresar.clicked.connect(self.enviar_info)
        self.boton_salir.clicked.connect(self.retirada)

    def iniciar_musica(self) -> None:
        # ponemos la música
        self.media_player_mp3 = QMediaPlayer(self)
        file_url = QUrl.fromLocalFile(p.PATH_MUSICA_FONDO)
        self.media_player_mp3.setSource(file_url)
        audio = QAudioOutput(self)
        audio.setVolume(0.25)
        self.media_player_mp3.setAudioOutput(audio)
        self.media_player_mp3.play()

    def enviar_info(self) -> None:
        # Le avisamos al backend la dificultad mediante la señal.
        nivel = self.selector_puzzle.currentText()
        usuario = self.usuario.text()
        self.signal_intentar_empezar.emit([usuario, nivel])

    def recibir_info(self) -> None:
        if self.signal_empezar.connect():
            self.hide()
        else:
            self.actualizar_salon()
            self.show()

    def keyPressEvent(self, event: QKeyEvent) -> None:
        if event.key() == Qt.Key.Key_Enter or event.key() == Qt.Key.Key_Return:
            self.enviar_info()

    def retirada(self):
        sys.exit()


if __name__ == '__main__':
    def hook(type, value, traceback) -> None:
        print(type)
        print(traceback)
    sys.__excepthook__ = hook

    app = QApplication([])
    # a = QFontDatabase.addApplicationFont(p.PATH_LETRA)
    font = QFont("Cascadia Mono SemiBold", 12)
    app.setFont(font)  # Creamos las base de la app: QApplication.
    ventana = VentanaInicio()   # Construimos un QWidget que será nuestra ventana.
    ventana.show()  # Mostramos la ventana.
    sys.exit(app.exec())
