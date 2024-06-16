from PyQt6.QtCore import QObject, pyqtSignal, QTimer, QMutex, QThread
import parametros as p


class Thread(QThread):
    fin = pyqtSignal()

    def run(self):
        self.fin.emit()


class Usuario(QObject):
    signal_intentar_empezar = pyqtSignal(str)
    signal_empezar = pyqtSignal(bool)
    signal_datos = pyqtSignal(list)
    signal_crear_tablero = pyqtSignal(str)
    signal_empezar_tiempo = pyqtSignal()
    signal_comprobar = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.puede = False
        self.signal_empezar_tiempo.connect(self.empezar_tiempo)
        self.signal_comprobar.connect(self.terminar)
        self.timer = QTimer(self)
        self.tiempo = 0

    def revisar_texto(self, texto):
        if texto.isalnum() and texto.lower() != texto:
            for elemento in texto:
                if elemento in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    self.puede = True
        self.signal_empezar.emit(self.puede)

    def guardar_datos(self, lista):
        self.nombre = lista[0]
        self.nivel = lista[1]
        self.signal_crear_tablero.emit(self.nivel)

    def empezar_tiempo(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.actualizar_tiempo)
        self.timer.start(1000)

    def actualizar_tiempo(self):
        self.tiempo += 1

    def reiniciar_tiempo(self):
        self.timer.stop()
        self.tiempo = 0
    
    def terminar(self):
        self.timer.stop()


class Tablero(QObject):
    signal_inicial = pyqtSignal(list)
    signal_crear_pepa = pyqtSignal()
    signal_agregar_pepa = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.thread = Thread()
        self.thread.fin.connect(self.thread_fin)
        self.dificultad = None
        self.timer_sandia = QTimer(self)
        self.x = 0
        self.y = 0

        self.mutex = QMutex()
        self.posiciones = None
        self.signal_inicial.connect(self.posiciones_pepa)

    def posiciones_pepa(self, lista):
        self.x = lista[0]
        self.y = lista[1]
        self.dificultad = lista[2]
        self.signal_agregar_pepa.emit()

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

