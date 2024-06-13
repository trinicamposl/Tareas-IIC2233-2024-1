from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtGui import QFont, QPixmap, QMouseEvent, QKeyEvent
from PyQt6.QtCore import Qt, pyqtSignal, QUrl, QTimer
from PyQt6.QtWidgets import QHBoxLayout, QWidget, QComboBox, QFormLayout, QLineEdit, QGridLayout
from PyQt6.QtWidgets import QLabel, QPushButton, QScrollArea, QVBoxLayout, QApplication
import parametros as p
from funciones import archivos, salon_fama, diccionario
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


class Tablero(QWidget):
    signal_izq = pyqtSignal(str)
    signal_der = pyqtSignal(str)
    signal_arriba = pyqtSignal(str)
    signal_abajo = pyqtSignal(str)

    def __init__(self, nivel: str):

        self.tamano = p.TAMANO[nivel.split("_")[0]]
        super().__init__()
        self.setGeometry(100, 100, 300, 300)
        self.cor_x = 0  # estas coordenadas indican exactamente dónde está pepe (pixeles)
        self.cor_y = 0
        self.xs = 1  # mientras que estas indican en que cuadrado está (matriz de lechugas de nxn)
        self.ye = 1

        grid_layout = QGridLayout()
        self.setLayout(grid_layout)
        fila = 0
        columna = 0
        for i in range((self.tamano+1)**2):
            datos = f"{fila},{columna}"
            if columna == 0 or fila == 0:
                if columna == 0 and fila == 0:
                    vacio = QLabel(self)
                else:
                    vacio = QLabel(f"{diccionario(nivel)[datos]}", self)
                grid_layout.addWidget(vacio, fila, columna)
            else:
                lechuga = QLabel(self)
                lechuga.setPixmap(QPixmap(p.LECHUGA_PATH))
                lechuga.setGeometry(0, 0, p.ANCHO_LECHUGA, p.ALTURA_LECHUGA)
                grid_layout.addWidget(lechuga, fila, columna)
            columna += 1
            if columna > self.tamano:
                columna = 0
                fila += 1

        self.pepa = QLabel(self)
        self.pepa.setPixmap(QPixmap(p.PATH_DOWN[0]))
        self.pepa.setGeometry(self.cor_x, self.cor_y, p.ANCHO_LECHUGA, p.ALTURA_LECHUGA)
        self.pepa.setWindowFlags(self.pepa.windowFlags() | Qt.WindowType.WindowStaysOnTopHint)

        QTimer.singleShot(100, self.definir_Pepa)

    def definir_Pepa(self):
        self.cor_x = self.layout().itemAtPosition(self.xs, self.ye).widget().geometry().x()
        self.cor_y = self.layout().itemAtPosition(self.xs, self.ye).widget().geometry().y()
        QTimer.singleShot(100, self.mover_pepa)

    def keyPressEvent(self, event: QKeyEvent) -> None:
        if event.key() == Qt.Key.Key_W:
            self.signal_arriba.emit("arriba")
            if True: # if self.signal_arriba.connect():
                self.mover_arriba()

        if event.key() == Qt.Key.Key_S:
            self.signal_abajo.emit("abajo")
            if True:  # if self.signal_abajo.connect():
                self.mover_abajo()

        if event.key() == Qt.Key.Key_A:
            self.signal_izq.emit("izquierda")
            if True:  # if self.signal_abajo.connect():
                self.mover_izquierda()

        if event.key() == Qt.Key.Key_D:
            self.signal_abajo.emit("derecha")
            if True:  # if self.signal_abajo.connect():
                self.mover_derecha()

    def mover_abajo(self):
        self.xs += 1
        for i in range(4):
            self.cor_y += 6
            QTimer.singleShot(200, self.mover_pepa)
            self.pepa.setPixmap(QPixmap(p.PATH_DOWN[i]))

    def mover_arriba(self):
        self.xs -= 1
        for i in range(4):
            self.cor_y -= 6
            QTimer.singleShot(200, self.mover_pepa)
            self.pepa.setPixmap(QPixmap(p.PATH_UP[i]))

    def mover_izquierda(self):
        self.ye -= 1
        for i in range(4):
            self.cor_x -= 6
            QTimer.singleShot(200, self.mover_pepa)
            self.pepa.setPixmap(QPixmap(p.PATH_LEFT[i]))

    def mover_derecha(self):
        self.ye += 1
        for i in range(4):
            self.cor_x += 6
            QTimer.singleShot(200, self.mover_pepa)
            self.pepa.setPixmap(QPixmap(p.PATH_RIGHT[i]))

    def mover_pepa(self):
        self.pepa.move(self.cor_x, self.cor_y)  # y aquí se mueve realmente
        self.cor_x = self.layout().itemAtPosition(self.xs, self.ye).widget().geometry().x()
        self.cor_y = self.layout().itemAtPosition(self.xs, self.ye).widget().geometry().y()


class Tiempo(QWidget):
    def __init__(self, nivel: str):
        super().__init__()
        self.duration = p.TIEMPO_JUEGO[nivel.split("_")[0]]
        self.label2 = QLabel()
        self.label2.setStyleSheet('border: 1px solid black')
        self.label2.setText(f'Te quedan {self.duration} segundos.')
        self.label2.show()
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(1000)

    def update(self):
        self.label2.setText(f'Te quedan {self.duration} segundos.')
        self.duration -= 1

        if self.duration < 0:
            self.timer.stop()
            exit()  # perdiste!

    def aumento(self, cuanto):
        pass


class VentanaJuego(QWidget):
    senal_click_pantalla = pyqtSignal(int, int)

    def __init__(self) -> None:
        super().__init__()
        # Tamaño de mi Ventana
        self.setGeometry(30, 50, p.ANCHO_JUEGO, p.ALTURA_JUEGO)

        # # QLabel para el Background (imagen de fondo)
        # self.background = QLabel(self)
        # self.background.setPixmap(QPixmap(p.FONDO_PATH))
        # self.background.setScaledContents(True)
        # self.background.setGeometry(0, 0, p.ANCHO_JUEGO, p.ALTURA_JUEGO)

        # Importante el QLabel sea transparente a los eventos del mouse.
        # self.background.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)

        # QLabel para la Vida
        self.label_tiempo = QLabel(self)
        self.label_tiempo.setFont(QFont("Arial", 17))
        self.label_tiempo.setGeometry(90, 10, 280, 50)
        self.label_tiempo.setStyleSheet("color: white")

        self.labels_meteorito = {}  # id: label
        # Defino la QPixmap para cada meteorito
        self.pixmap_meteorito = QPixmap(p.METEORO_PATH)

        # QLabel para la mira del disparo
        self.label_disparo = QLabel(self)
        self.label_disparo.setPixmap(QPixmap(p.MIRA_PATH))
        self.label_disparo.setScaledContents(True)
        self.label_disparo.setGeometry(-100, -100, 100, 100)

        self.personalizarMouse()

    def personalizarMouse(self) -> None:
        """
        Este método se encarga de personalizar el mouse para que sea invisible,
        se detecte siempre su movimiento y los QLabel no interfieren an la detección
        de los eventos del mouse.
        """
        # Ventana pueda seguir en todo momento el movimiento del mouse y
        self.setMouseTracking(True)

        # Que el mouse sea invisible
        self.setCursor(Qt.CursorShape.BlankCursor)

        # El QLabel de la mira sea transparente a los eventos del mouse.
        self.label_disparo.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)

        # El QLabel con las vidas sea transparente a los eventos del mouse.
        self.label_vida.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)

    def empezar_juego(self) -> None:
        self.show()

    def mousePressEvent(self, event: QMouseEvent) -> None:
        """
        Método encargado de avisar al backend cada vez que presionamos
        con el mouse.

        Este método tiene 1 error 😱.
        """
        if event.button() == Qt.MouseButton.LeftButton:
            # Ronda 4.1
            # ERROR 😱: no se define x, y
            # Actual ❌: no había nada sobre x e y.
            # Solución : usar event.pos().x() e event.pos().y()
            x = event.pos().x()
            y = event.pos().y()
            self.senal_click_pantalla.emit(x, y)

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        """
        Método encargado de mover visualmente la mira de disparo cada vez
        que se mueve el mouse
        """
        x = event.pos().x()
        y = event.pos().y()
        # Hacemos -50 para que la imagen esté centrada al mouse
        self.label_disparo.move(x - 50, y - 50)

    def actualizar_poblacion(self, texto: str) -> None:
        """
        Método encargado de actualizar la cantidad de vidas en la ventana
        """
        self.label_vida.setText(texto)
        self.label_vida.resize(self.label_vida.sizeHint())

    def aparecer_meteorito(self, id_meteorito: int, x: int, y: int) -> None:
        """
        Método encargado de generar visualmente un meteorito en la ventana
        """
        # Definir label de meteorito
        label = QLabel(self)
        label.setPixmap(self.pixmap_meteorito)
        label.setScaledContents(True)
        label.setGeometry(x, y, p.ANCHO_METEORO, p.ALTURA_METEORO)

        # Este QLabel sea transparente a los eventos del mouse.
        label.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)

        # Guardar QLabel en nuestro diccionario
        self.labels_meteorito[id_meteorito] = label

        # Asegurar que la mira de disparo sig sobre todo lo demás QLabel
        self.label_disparo.raise_()

        # Mostrar imagen
        label.show()

    def remover_meteorito(self, id_meteorito: int) -> None:
        """
        Método encargado de eliminar visualmente un meteorito en la ventana.
        En este caso, solo lo escondemos.

        Tarea para la casa: Investigar como eliminar elementos y
        no solo ocultarlos
        """
        self.labels_meteorito[id_meteorito].hide()

    def mover_meteorito(self, id_meteorito, x, y) -> None:
        """
        Método encargado de mover visualmente un meteorito en la ventana
        """
        label: QLabel = self.labels_meteorito[id_meteorito]
        label.move(x, y)


if __name__ == '__main__':
    def hook(type, value, traceback) -> None:
        print(type)
        print(traceback)
    sys.__excepthook__ = hook

    app = QApplication([])
    # a = QFontDatabase.addApplicationFont(p.PATH_LETRA)
    font = QFont("Cascadia Mono SemiBold", 12)
    app.setFont(font)  # Creamos las base de la app: QApplication.
    ventana = Tablero("novato_1.txt")   # Construimos un QWidget que será nuestra ventana.
    ventana.show()  # Mostramos la ventana.
    sys.exit(app.exec())
