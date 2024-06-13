from PyQt6.QtGui import QPixmap, QFont, QKeyEvent
from PyQt6.QtCore import pyqtSignal, QTimer, QThread, QMutex, Qt
from PyQt6.QtWidgets import QWidget, QGridLayout, QApplication
from PyQt6.QtWidgets import QLabel
import parametros as p
from funciones import diccionario
import sys


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

        self.cor_x = 0
        self.cor_y = 0
        self.xs = 1
        self.ye = 1

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
                self.thread.start()
                self.mover_arriba()

            if event.key() == Qt.Key.Key_S:
                self.thread.start()
                self.mover_abajo()

            if event.key() == Qt.Key.Key_A:
                self.thread.start()
                self.mover_izquierda()

            if event.key() == Qt.Key.Key_D:
                self.thread.start()
                self.mover_derecha()

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


if __name__ == '__main__':
    def hook(type, value, traceback) -> None:
        print(type)
        print(traceback)
    sys.__excepthook__ = hook

    app = QApplication([])
    # a = QFontDatabase.addApplicationFont(p.PATH_LETRA)
    font = QFont("Cascadia Mono SemiBold", 12)
    app.setFont(font)  # Creamos las base de la app: QApplication.
    ventana = Tablero("experto_1.txt")   # Construimos un QWidget que será nuestra ventana.

    ventana.show()  # Mostramos la ventana.
    sys.exit(app.exec())
