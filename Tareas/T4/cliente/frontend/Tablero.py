from PyQt6.QtGui import QPixmap, QKeyEvent
from PyQt6.QtCore import Qt, pyqtSignal, QTimer
from PyQt6.QtWidgets import QWidget, QGridLayout
from PyQt6.QtWidgets import QLabel
import parametros as p
from funciones import diccionario


class Tablero(QWidget):
    signal_izq = pyqtSignal(str)
    signal_der = pyqtSignal(str)
    signal_arriba = pyqtSignal(str)
    signal_abajo = pyqtSignal(str)

    def __init__(self, nivel: str):

        self.tamano = p.TAMANO[nivel.split("_")[0]]
        self.dificultad = p.NIVEL[nivel.split("_")[0]]
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
                lechuga.setGeometry(0, 0, p.ANCHO_LECHUGA[self.dificultad],
                                    p.ALTURA_LECHUGA[self.dificultad])
                grid_layout.addWidget(lechuga, fila, columna)
            columna += 1
            if columna > self.tamano:
                columna = 0
                fila += 1

        self.pepa = QLabel(self)
        self.pepa.setPixmap(QPixmap(p.RUTAS["abajo"][0][1]))
        self.pepa.setGeometry(self.cor_x, self.cor_y, p.ANCHO_LECHUGA[self.dificultad],
                              p.ALTURA_LECHUGA[self.dificultad])
        self.pepa.setWindowFlags(self.pepa.windowFlags() | Qt.WindowType.WindowStaysOnTopHint)

        QTimer.singleShot(100, self.definir_Pepa)

    def definir_Pepa(self):
        self.cor_x = self.layout().itemAtPosition(self.xs, self.ye).widget().geometry().x()
        self.cor_y = self.layout().itemAtPosition(self.xs, self.ye).widget().geometry().y()
        QTimer.singleShot(100, lambda: self.mover_final("abajo", 0))

    def keyPressEvent(self, event: QKeyEvent) -> None:
        if event.key() == Qt.Key.Key_W:
            self.signal_arriba.emit("arriba")
            if True:  # if self.signal_arriba.connect():
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

    def mover_abajo(self, paso=0):
        if paso < 4:
            self.cor_y += p.PASOS[self.dificultad]
            QTimer.singleShot(100, lambda: self.mover_pepa("abajo", paso))
            QTimer.singleShot(100, lambda: self.mover_abajo(paso + 1))
        else:
            self.xs += 1
            QTimer.singleShot(100, lambda: self.mover_final("abajo", 0))

    def mover_arriba(self, paso=0):
        if paso < 4:
            self.cor_y -= p.PASOS[self.dificultad]
            QTimer.singleShot(100, lambda: self.mover_pepa("arriba", paso))
            QTimer.singleShot(100, lambda: self.mover_arriba(paso + 1))
        else:
            self.xs -= 1
            QTimer.singleShot(100, lambda: self.mover_final("abajo", 0))

    def mover_izquierda(self, paso=0):
        if paso < 4:
            self.cor_x -= p.PASOS[self.dificultad]
            QTimer.singleShot(100, lambda: self.mover_pepa("izquierda", paso))
            QTimer.singleShot(100, lambda: self.mover_izquierda(paso + 1))
        else:
            self.ye -= 1
            QTimer.singleShot(100, lambda: self.mover_final("abajo", 0))

    def mover_derecha(self, paso=0):
        if paso < 4:
            self.cor_x += p.PASOS[self.dificultad]
            QTimer.singleShot(100, lambda: self.mover_pepa("derecha", paso))
            QTimer.singleShot(100, lambda: self.mover_derecha(paso + 1))
        else:
            self.ye += 1
            QTimer.singleShot(100, lambda: self.mover_final("abajo", 0))

    def mover_pepa(self, donde, imagen):
        self.pepa.move(self.cor_x, self.cor_y)  # y aquí se mueve realmente
        self.pepa.setPixmap(QPixmap(p.RUTAS[donde][imagen][1]))

    def mover_final(self, donde, imagen):
        self.cor_x = self.layout().itemAtPosition(self.xs, self.ye).widget().geometry().x()
        self.cor_y = self.layout().itemAtPosition(self.xs, self.ye).widget().geometry().y()
        self.pepa.move(self.cor_x, self.cor_y)
        self.pepa.setPixmap(QPixmap(p.RUTAS[donde][imagen][1]))
