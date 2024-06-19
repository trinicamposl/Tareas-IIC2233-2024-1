from PyQt6.QtCore import QObject, pyqtSignal, QTimer, QMutex, QThread
from threading import Thread
import socket
import pickle
import parametros as p
import random
from funciones import decodificar, codificar


class thread_modificado(QThread):
    fin = pyqtSignal()

    def run(self):
        self.fin.emit()


class Usuario(QObject):
    signal_enviar_alerta = pyqtSignal(str)
    signal_actualizar_conectado = pyqtSignal()
    signal_cerrar_ventana = pyqtSignal()
    signal_intentar_empezar = pyqtSignal(str)
    signal_empezar = pyqtSignal(bool)
    signal_datos = pyqtSignal(list)
    signal_crear_tablero = pyqtSignal(str)
    signal_empezar_tiempo = pyqtSignal()
    signal_comprobar = pyqtSignal()
    signal_tiempo_final = pyqtSignal(int)
    signal_estaba_mal = pyqtSignal()
    signal_pedir_tablero = pyqtSignal()
    signal_ganaste = pyqtSignal(float)

    def __init__(self, host: str, puerto: str):
        super().__init__()
        self.puede = False
        self.signal_empezar_tiempo.connect(self.empezar_tiempo)
        self.signal_comprobar.connect(self.terminar)
        self.timer = QTimer(self)
        self.tiempo = 0
        self.socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = puerto
        self.puntaje = None
        self.tamano = None
        self.conectar()

    def conectar(self) -> None:
        """Establece la conexión con el servidor"""
        try:
            self.socket_cliente.connect((self.host, self.port))
            thread_escuchar_servidor = Thread(target=self.escuchar_servidor,
                                              args=(self.socket_cliente,),
                                              daemon=True)
            thread_escuchar_servidor.start()
            self.signal_actualizar_conectado.emit()
        except ConnectionError:
            QTimer.singleShot(1000, lambda: self.cerrar_programa("No se pudo establecer conexión"
                                                                 " con el servidor."))
            # Ordena el cierre del programa

    def escuchar_servidor(self, socket_servidor: socket.socket) -> None:
        """(Debe llamarse como Thread). Lee al servidor"""
        while True:
            try:
                bytes_largo_datos = socket_servidor.recv(4)
                largo_datos = int.from_bytes(bytes_largo_datos, byteorder="big")
                respuesta = bytearray()
                respuesta += bytearray(bytes_largo_datos)
                bytes_totales = ((25 + 3) * ((largo_datos // 25))) + 3
                if largo_datos % 25 != 0:
                    bytes_totales += (25 + 4)  # Chunk extra
                if len(bytes_largo_datos) == 0:
                    # Desconexión.
                    break
                # Lectura de los bytes
                while len(respuesta) < bytes_totales:
                    bytes_lectura = min(4096, (bytes_totales) - len(respuesta))
                    respuesta_bytes = socket_servidor.recv(bytes_lectura)
                    respuesta += bytearray(respuesta_bytes)
                # Desencriptación y obtención del objeto
                obj = decodificar(respuesta)
                texto = pickle.loads(obj)
                if texto:
                    with open(p.PATH_PUNTAJES, "a", encoding="utf-8") as archivo:
                        archivo.write(f"{self.nombre}---{self.puntaje}\n")
                        self.signal_ganaste.emit(self.puntaje)
                else:
                    self.signal_estaba_mal.emit()
            except ConnectionError:
                self.cerrar_programa("Se ha perdido la conexión con el servidor.")
                break

    def enviar_informacion(self, datos: object) -> None:
        """Envía la información al socket del servidor"""
        try:
            codificado = (codificar(pickle.dumps(datos)))
            self.socket_cliente.sendall(codificado)
        except BrokenPipeError:
            self.cerrar_programa("No se pudo establecer conexión"
                                 " con el servidor.")
        except ConnectionError:
            self.cerrar_programa("No se pudo establecer conexión"
                                 " con el servidor.")

    def cerrar_programa(self, mensaje=None):
        if mensaje is not None:
            self.signal_enviar_alerta.emit(mensaje)
        QTimer.singleShot(6000, lambda: self.signal_cerrar_ventana.emit())

    def desconectar_servidor(self, socket_servidor: socket.socket) -> None:
        """Cierra el socket"""
        socket_servidor.close()

    def revisar_texto(self, texto):
        if texto.isalnum() and texto.lower() != texto:
            for elemento in texto:
                if elemento in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    self.puede = True
        self.signal_empezar.emit(self.puede)

    def guardar_datos(self, lista):
        self.nombre = lista[0]  # nombre usuario
        self.nivel = lista[1]  # nombre archivo
        dificultad = self.nivel.split("_")[0]
        self.tamano = p.TAMANO[dificultad]
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

    def calcular_puntaje(self, tiempo_restante):
        if tiempo_restante == "infinito":
            puntaje_final = p.PUNTAJE_INF
        else:
            puntaje_final = tiempo_restante * self.tamano * self.tamano / self.tiempo
        self.puntaje = puntaje_final
        self.signal_pedir_tablero.emit()

    def comprobar(self, tablero):
        self.enviar_informacion([self.nivel, tablero, self.nombre, self.puntaje])


class Tablero(QObject):
    signal_inicial = pyqtSignal(list)
    signal_crear_pepa = pyqtSignal()
    signal_agregar_pepa = pyqtSignal()
    signal_mover = pyqtSignal(list)
    signal_pedir_coordenadas = pyqtSignal(list)
    signal_enviar_accion = pyqtSignal(list)
    signal_perdiste = pyqtSignal()
    signal_tiempo_final = pyqtSignal(int)
    signal_sandia = pyqtSignal(list)
    signal_tablero = pyqtSignal(list)

    def __init__(self):
        super().__init__()
        self.thread = thread_modificado()
        self.thread.fin.connect(self.thread_fin)
        self.tamano = None
        self.tiempo = None
        self.x = 0  # posiciones pixeles
        self.y = 0
        self.m_x = 1  # posiciones cuadricula
        self.m_y = 1
        self.tiempo_restante = None
        self.puntaje = None
        self.lechugas = None

        self.mutex = QMutex()
        self.posiciones = None

        self.timer_sandia = QTimer(self)
        self.timer_sandia.timeout.connect(self.producir_sandia)
        self.intervalo = p.TIEMPO_APARICION * 1000

        self.signal_inicial.connect(self.posiciones_pepa)

    def posiciones_pepa(self, lista):
        self.x = lista[0]
        self.y = lista[1]
        self.tamano = lista[2]
        self.lechugas = [[1 for x in range(self.tamano)] for i in range(self.tamano)]
        self.signal_agregar_pepa.emit()
        self.timer_sandia.start(self.intervalo)   # revisar

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
        if self.lechugas[self.m_x - 1][self.m_y - 1] == 1:
            self.signal_enviar_accion.emit(["vaciar", [self.m_x, self.m_y]])
            self.lechugas[self.m_x - 1][self.m_y - 1] = 0
        else:
            self.signal_enviar_accion.emit(["rellenar", [self.m_x, self.m_y]])
            self.lechugas[self.m_x - 1][self.m_y - 1] = 1

    def actualizar_restante(self, dato):
        if dato.split(" ")[2].isnumeric():
            self.tiempo_restante = int(dato.split(" ")[2])
            if self.tiempo_restante <= 0:
                self.signal_perdiste.emit()
        else:
            self.tiempo_restante = "infinito"

    def producir_sandia(self):
        x = random.randint(50, p.ANCHO_PANTALLA[p.TAMANO_INV[self.tamano]] - 20)
        y = random.randint(50, p.LARGO_PANTALLA[p.TAMANO_INV[self.tamano]] - 20)
        self.signal_sandia.emit([x, y])

    def enviar_tablero(self):
        self.signal_tablero.emit(self.lechugas)
