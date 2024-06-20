from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtGui import QPixmap, QKeyEvent
from PyQt6.QtCore import Qt, pyqtSignal, QUrl
from PyQt6.QtWidgets import QHBoxLayout, QWidget, QComboBox, QFormLayout, QLineEdit
from PyQt6.QtWidgets import QLabel, QPushButton, QScrollArea, QVBoxLayout, QDialogButtonBox, QDialog
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

    def actualizar_contenido(self):
        jugadores = reversed(salon_fama())
        # Limpiar el contenido actual del QVBoxLayout
        for i in (range(self.vbox.count())):
            widget = self.vbox.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

        for elemento in jugadores:
            label = QLabel(elemento)
            self.vbox.addWidget(label)

        self.widget.setLayout(self.vbox)
        self.scroll.update()


class Popup(QDialog):
    def __init__(self, texto):
        super().__init__()

        self.setWindowTitle("HELLO!")

        QBtn = QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel(texto)
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)
        self.setWindowFlags(self.windowFlags() | Qt.WindowType.WindowStaysOnTopHint)
        self.setGeometry(210, 280, 200, 100)


class VentanaInicio(QWidget):

    signal_intentar_empezar = pyqtSignal(str)
    signal_empezar = pyqtSignal(str)
    signal_empezo_juego = pyqtSignal(bool)
    signal_datos = pyqtSignal(list)
    signal_popup = pyqtSignal()
    signal_parar_tiempo = pyqtSignal()

    def __init__(self) -> None:
        super().__init__()
        self.iniciar_dibujos()
        self.iniciar_musica()
        # Creamos el popup en caso que no se cumplan las condiciones de usuario
        self.ventana_popup = Popup(p.texto_reglas)
        self.ventana_popup_perdiste = Popup(p.texto_perdiste)
        self.silenciado = False

    def iniciar_dibujos(self) -> None:
        self.setGeometry(30, 50, p.ANCHO_JUEGO, p.ALTURA_JUEGO)
        self.setWindowTitle("Ventana de Inicio")
        # Creamos el selector que vamos a necesitar en nuestra ventana de Inicio
        self.selector_puzzle = QComboBox()
        self.selector_puzzle.addItems(archivos())
        # Creamos el usuario
        self.usuario = QFormLayout()
        self.linea_texto = QLineEdit()
        self.usuario.addRow("Elige tu usuario:", self.linea_texto)
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
        self.signal_popup.connect(self.popup)

    def popup(self):
        # aquí conecto el cerrar el popup a activar todo
        self.ventana_popup.accepted.connect(lambda: self.boton_ingresar.setEnabled(True))
        self.ventana_popup.rejected.connect(lambda: self.boton_ingresar.setEnabled(True))
        self.ventana_popup.accepted.connect(lambda: self.selector_puzzle.setEnabled(True))
        self.ventana_popup.rejected.connect(lambda: self.selector_puzzle.setEnabled(True))
        self.ventana_popup.accepted.connect(lambda: self.linea_texto.setEnabled(True))
        self.ventana_popup.rejected.connect(lambda: self.linea_texto.setEnabled(True))
        self.ventana_popup.show()

        # aquí conecto el abrir el popup a bloquear
        if self.ventana_popup.isVisible():
            self.boton_ingresar.setEnabled(False)
            self.selector_puzzle.setEnabled(False)
            self.linea_texto.setEnabled(False)

    def iniciar_musica(self) -> None:
        # ponemos la música
        self.media_player_mp3 = QMediaPlayer(self)
        file_url = QUrl.fromLocalFile(p.PATH_MUSICA_FONDO)
        self.media_player_mp3.setSource(file_url)
        audio = QAudioOutput(self)
        audio.setVolume(0.25)
        self.media_player_mp3.setAudioOutput(audio)
        self.media_player_mp3.play()
        self.media_player_mp3.setLoops(-1)

    def enviar_info(self) -> None:
        # Le avisamos al backend la dificultad mediante la señal.
        usuario = self.usuario.itemAt(1).widget().text()
        self.signal_intentar_empezar.emit(usuario)

    def recibir_info(self, variable) -> None:
        if variable:
            usuario = self.usuario.itemAt(1).widget().text()
            nivel = self.selector_puzzle.currentText()
            self.signal_empezo_juego.emit(True)
            self.signal_datos.emit([usuario, nivel])

        else:
            self.signal_empezo_juego.emit(False)

    def keyPressEvent(self, event: QKeyEvent) -> None:
        if event.key() == Qt.Key.Key_Enter or event.key() == Qt.Key.Key_Return:
            self.enviar_info()

    def retirada(self):
        sys.exit()

    def volver(self):
        self.show()
        self.signal_parar_tiempo.emit()

    def volver_perdido(self):
        self.ventana_popup_perdiste.accepted.connect(lambda: self.boton_ingresar.setEnabled(True))
        self.ventana_popup_perdiste.rejected.connect(lambda: self.boton_ingresar.setEnabled(True))
        self.ventana_popup_perdiste.accepted.connect(lambda: self.selector_puzzle.setEnabled(True))
        self.ventana_popup_perdiste.rejected.connect(lambda: self.selector_puzzle.setEnabled(True))
        self.ventana_popup_perdiste.accepted.connect(lambda: self.linea_texto.setEnabled(True))
        self.ventana_popup_perdiste.rejected.connect(lambda: self.linea_texto.setEnabled(True))
        self.ventana_popup_perdiste.show()

        # aquí conecto el abrir el popup a bloquear
        if self.ventana_popup_perdiste.isVisible():
            self.boton_ingresar.setEnabled(False)
            self.selector_puzzle.setEnabled(False)
            self.linea_texto.setEnabled(False)
        self.show()
        if not self.silenciado:
            media_player_mp3 = QMediaPlayer(self)
            file_url = QUrl.fromLocalFile(p.PATH_MUSICA_PERDEDORA)
            media_player_mp3.setSource(file_url)
            audio = QAudioOutput(self)
            audio.setVolume(0.5)
            media_player_mp3.setAudioOutput(audio)
            media_player_mp3.play()

        self.signal_parar_tiempo.emit()

    def silenciar(self):
        self.media_player_mp3.stop()
        self.silenciado = True

    def actualizar_salon(self):
        self.sala.actualizar_contenido()
