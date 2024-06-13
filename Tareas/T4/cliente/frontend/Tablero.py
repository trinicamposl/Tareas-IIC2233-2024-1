from PyQt6.QtGui import QPixmap, QFont, QKeyEvent
from PyQt6.QtCore import pyqtSignal, QTimer, QThread, QMutex, Qt
from PyQt6.QtWidgets import QWidget, QGridLayout, QApplication, QPushButton, QLabel
import parametros as p
from funciones import diccionario
import sys
from TiempoBotones import Tiempo


class Thread(QThread):
    fin = pyqtSignal()

    def run(self):
        self.fin.emit()


class Tablero(QWidget):
    signal_izq = pyqtSignal(str)
    signal_der = pyqtSignal(str)
    signal_arriba = pyqtSignal(str)
    signal_abajo = pyqtSignal(str)

    def __init__(self, nivel: str):

        nivel_2 = nivel.split("_")[0]
        self.tamano = p.TAMANO[nivel_2]
        self.dificultad = p.NIVEL[nivel_2]
        super().__init__()
        self.setGeometry(50, 50, 100, 100)
        self.setFixedSize(p.ANCHO_PANTALLA[nivel_2], p.LARGO_PANTALLA[nivel_2])

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
                lechuga.setFixedSize(p.ANCHO_LECHUGA[self.dificultad],
                                     p.ALTURA_LECHUGA[self.dificultad])
                grid_layout.addWidget(lechuga, fila, columna)

            columna += 1
            if columna > self.tamano:
                columna = 0
                fila += 1

        self.tiempo = Tiempo(nivel)
        grid_layout.addWidget(self.tiempo, 0, self.tamano + 1)
        self.salir = QPushButton("Salir")
        self.salir.setFixedHeight(p.ALTURA_LECHUGA[self.dificultad])
        self.comprobar = QPushButton("Comprobar")
        self.comprobar.setFixedHeight(p.ALTURA_LECHUGA[self.dificultad])

        self.comprobar.clicked.connect(self.enviar_info)
        self.salir.clicked.connect(self.retirada)

        for i in range(self.tamano):
            if i == 1:
                grid_layout.addWidget(self.salir, i, self.tamano + 1)
            elif i == 2:
                grid_layout.addWidget(self.comprobar, i, self.tamano + 1)
            else:
                vacio = QLabel("")
                grid_layout.addWidget(vacio, i, self.tamano + 1)

        self.cor_x = 0  # estas coordenadas indican exactamente dónde está pepe (pixeles)
        self.cor_y = 0
        self.xs = 1  # mientras que estas indican en que cuadrado está (matriz de lechugas de nxn)
        self.ye = 1
        self.pepa = QLabel(self)
        self.pepa.setPixmap(QPixmap(p.RUTAS["abajo"][0][1]))
        self.pepa.setGeometry(self.cor_x, self.cor_y, p.ANCHO_LECHUGA[self.dificultad],
                              p.ALTURA_LECHUGA[self.dificultad])
        self.pepa.setWindowFlags(self.pepa.windowFlags() | Qt.WindowType.WindowStaysOnTopHint)

        self.thread = Thread()
        self.thread.fin.connect(self.thread_fin)

        self.mutex = QMutex()

        QTimer.singleShot(100, self.definir_Pepa)

    def definir_Pepa(self):
        self.cor_x = self.layout().itemAtPosition(self.xs, self.ye).widget().geometry().x()
        self.cor_y = self.layout().itemAtPosition(self.xs, self.ye).widget().geometry().y()
        QTimer.singleShot(100, lambda: self.mover_final("abajo", 0))

    def keyPressEvent(self, event: QKeyEvent) -> None:
        if not self.thread.isRunning() and self.mutex.tryLock():
            if event.key() == Qt.Key.Key_W:
                if self.ye != 0:
                    self.thread.start()
                    self.mover_arriba()
                else:
                    pass

            if event.key() == Qt.Key.Key_S:
                if self.ye != self.tamano + 1:
                    self.thread.start()
                    self.mover_abajo()
                else:
                    pass

            if event.key() == Qt.Key.Key_A:
                if self.ye != 0:
                    self.thread.start()
                    self.mover_izquierda()
                else:
                    pass

            if event.key() == Qt.Key.Key_D:
                if self.xs != self.tamano + 1:
                    self.thread.start()
                    self.mover_derecha()
                else:
                    pass

    def mover_abajo(self, paso=0):
        if paso < 4:
            self.cor_y += p.PASOS[self.dificultad]
            self.mover_pepa("abajo", paso)
            QTimer.singleShot(100, lambda: self.mover_abajo(paso + 1))
        else:
            self.xs += 1
            QTimer.singleShot(100, lambda: self.mover_final("abajo", 0))
            self.thread.fin.connect(self.thread_fin)

    def mover_arriba(self, paso=0):
        if paso < 4:
            self.cor_y -= p.PASOS[self.dificultad]
            self.mover_pepa("arriba", paso)
            QTimer.singleShot(100, lambda: self.mover_arriba(paso + 1))
        else:
            self.xs -= 1
            QTimer.singleShot(100, lambda: self.mover_final("abajo", 0))
            self.thread.fin.connect(self.thread_fin)

    def mover_izquierda(self, paso=0):
        if paso < 4:
            self.cor_x -= p.PASOS[self.dificultad]
            self.mover_pepa("izquierda", paso)
            QTimer.singleShot(100, lambda: self.mover_izquierda(paso + 1))
        else:
            self.ye -= 1
            QTimer.singleShot(100, lambda: self.mover_final("abajo", 0))
            self.thread.fin.connect(self.thread_fin)

    def mover_derecha(self, paso=0):
        if paso < 4:
            self.cor_x += p.PASOS[self.dificultad]
            self.mover_pepa("derecha", paso)
            QTimer.singleShot(100, lambda: self.mover_derecha(paso + 1))
        else:
            self.ye += 1
            QTimer.singleShot(100, lambda: self.mover_final("abajo", 0))
            self.thread.fin.connect(self.thread_fin)

    def mover_pepa(self, donde, imagen):
        self.pepa.setPixmap(QPixmap(p.RUTAS[donde][imagen][1]))
        self.pepa.move(self.cor_x, self.cor_y)

    def mover_final(self, donde, imagen):
        self.cor_x = self.layout().itemAtPosition(self.xs, self.ye).widget().geometry().x()
        self.cor_y = self.layout().itemAtPosition(self.xs, self.ye).widget().geometry().y()
        self.pepa.move(self.cor_x, self.cor_y)
        self.pepa.setPixmap(QPixmap(p.RUTAS[donde][imagen][1]))
        self.mutex.unlock()

    def thread_fin(self):
        self.thread.quit()

    def retirada(self):
        self.hide()
        sys.exit()

    def enviar_info(self):
        pass
