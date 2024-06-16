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
    signal_mover = pyqtSignal(list)
    signal_pedir_coordenadas = pyqtSignal(list)
    signal_enviar_accion = pyqtSignal(list)
    signal_perdiste = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.thread = Thread()
        self.thread.fin.connect(self.thread_fin)
        self.tamano = None
        self.timer_sandia = QTimer(self)  # revisar
        self.x = 0  # posiciones pixeles
        self.y = 0
        self.m_x = 1  # posiciones cuadricula
        self.m_y = 1
        self.tiempo_restante = None

        self.mutex = QMutex()
        self.posiciones = None
        self.signal_inicial.connect(self.posiciones_pepa)

        self.lechugas = None

    def posiciones_pepa(self, lista):
        self.x = lista[0]
        self.y = lista[1]
        self.tamano = lista[2]
        self.lechugas = [[1 for x in range(self.tamano)] for i in range(self.tamano)]
        self.signal_agregar_pepa.emit()

    def mover(self, donde):
        if not self.thread.isRunning() and self.mutex.tryLock():
            self.thread.start()
            if donde == "arriba":
                self.mover_arriba()
            elif donde == "abajo":
                self.mover_abajo()
            elif donde == "izquierda":
                self.mover_izquierda()
            elif donde == "derecha":
                self.mover_derecha()

    def mover_abajo(self, paso=0):  # si alcanzo mejorar esto para que no este acoplado
        if self.m_x != self.tamano:
            if paso < 4:
                self.y += p.PASOS
                self.signal_mover.emit(("abajo", paso, [self.x, self.y]))
                QTimer.singleShot(100, lambda: self.mover_abajo(paso + 1))
            else:
                self.m_x += 1
                QTimer.singleShot(100, lambda:
                                  self.signal_pedir_coordenadas.emit([self.m_x, self.m_y]))
        else:
            self.mutex.unlock()
            self.thread.fin.connect(self.thread_fin)

    def mover_arriba(self, paso=0):
        if self.m_x != 1:
            if paso < 4:
                self.y -= p.PASOS
                self.signal_mover.emit(("arriba", paso, [self.x, self.y]))
                QTimer.singleShot(100, lambda: self.mover_arriba(paso + 1))
            else:
                self.m_x -= 1
                QTimer.singleShot(100, lambda:
                                  self.signal_pedir_coordenadas.emit([self.m_x, self.m_y]))
        else:
            self.mutex.unlock()
            self.thread.fin.connect(self.thread_fin)

    def mover_izquierda(self, paso=0):
        if self.m_y != 1:
            if paso < 4:
                self.x -= p.PASOS
                self.signal_mover.emit(("izquierda", paso, [self.x, self.y]))
                QTimer.singleShot(100, lambda: self.mover_izquierda(paso + 1))
            else:
                self.m_y -= 1
                QTimer.singleShot(100, lambda:
                                  self.signal_pedir_coordenadas.emit([self.m_x, self.m_y]))
        else:
            self.mutex.unlock()
            self.thread.fin.connect(self.thread_fin)

    def mover_derecha(self, paso=0):
        if self.m_y != self.tamano:
            if paso < 4:
                self.x += p.PASOS
                self.signal_mover.emit(("derecha", paso, [self.x, self.y]))
                QTimer.singleShot(100, lambda: self.mover_derecha(paso + 1))
            else:
                self.m_y += 1
                QTimer.singleShot(100, lambda:
                                  self.signal_pedir_coordenadas.emit([self.m_x, self.m_y]))
        else:
            self.mutex.unlock()
            self.thread.fin.connect(self.thread_fin)

    def mover_final(self, datos):
        self.x = datos[0]
        self.y = datos[1]
        self.signal_mover.emit(("abajo", 0, datos))
        self.mutex.unlock()
        self.thread.fin.connect(self.thread_fin)

    def thread_fin(self):
        self.thread.quit()

    def relleno(self):
        print(self.lechugas, self.m_x, self.m_y)
        if self.lechugas[self.m_x - 1][self.m_y - 1] == 1:
            self.signal_enviar_accion.emit(["vaciar", [self.m_x, self.m_y]])
            self.lechugas[self.m_x - 1][self.m_y - 1] = 0
        else:
            self.signal_enviar_accion.emit(["rellenar", [self.m_x, self.m_y]])
            self.lechugas[self.m_x - 1][self.m_y - 1] = 1

    def actualizar_restante(self, dato):
        self.tiempo_restante = int(dato.split(" ")[2])
        if self.tiempo_restante <= 0:
            self.signal_perdiste.emit()
