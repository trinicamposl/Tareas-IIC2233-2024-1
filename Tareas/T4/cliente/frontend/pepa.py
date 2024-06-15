from PyQt6.QtCore import QTimer, QPropertyAnimation, QPoint, Qt
from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import QPixmap
import parametros as p


class Pepa(QLabel):
    def __init__(self, parent: object, posicion: list) -> None:
        super().__init__(parent)
        self.posicion_inicial = posicion
        self.direccion = None
        self.crear_dibujos()
        self.crear_timers()
        self.setScaledContents(True)

    def crear_dibujos(self):
        self.dibujo_principal = QPixmap(p.RUTAS["abajo"][0])
        self.setPixmap(self.dibujo_principal)
        self.setGeometry(*self.posicion_inicial, p.ANCHO_LECHUGA, p.ALTURA_LECHUGA)
        self.setWindowFlags(self.windowFlags() | Qt.WindowType.WindowStaysOnTopHint)

    def crear_timers(self):
        self.paso = 0
        self.timer_animacion = QTimer()
        self.timer_animacion.setInterval(p.TIEMPO_PASOS * 3)
        self.timer_animacion.timeout.connect(self.caminar)
        self.timer_fin_animacion = QTimer()
        self.timer_fin_animacion.setInterval(p.TIEMPO_PASOS * 3)
        self.timer_fin_animacion.timeout.connect(self.detener)

    def detectar_tipo_movimiento(self, posicion_mapa: list) -> str:
        """Retorna el tipo de movimiento (up, down, left, right)
        dependiendo de las nuevas posiciones dentro del mapa"""
        posicion_x, posicion_y = self.x(), self.y()
        nueva_x, nueva_y = posicion_mapa[0], posicion_mapa[1]
        if nueva_y > posicion_y:
            return "abajo"
        elif nueva_y < posicion_y:
            return "arriba"
        elif nueva_x > posicion_x:
            return "derecha"
        elif nueva_x < posicion_x:
            return "izquierda"
        else:
            return "fin"  # no hay movimiento

    def caminar(self):
        if self.direccion == "fin":
            self.setPixmap(self.dibujo_principal)
        else:
            if self.direccion == "abajo":
                lista = p.RUTAS["abajo"]
            elif self.direccion == "arroba":
                lista = p.RUTAS["arriba"]
            elif self.direccion == "derecha":
                lista = p.RUTAS["derecha"]
            elif self.direccion == "izquierda":
                lista = p.RUTAS["izquierda"]
            indice = self.paso % 3
            self.setPixmap(QPixmap(lista[indice]))
            self.paso += 1

    def comenzar_animacion(self) -> None:
        """Inicializa el timer de la animación"""
        self.timer_animacion.start()
        self.timer_fin_animacion.start()

    def detener(self) -> None:
        """Detiene la animación del personaje"""
        self.timer_animacion.stop()
        self.timer_fin_animacion.stop()
        self.setPixmap(self.pixmap_principal)
        self.pasos = 0

    def mover(self, posicion_mapa) -> None:
        self.tipo_movimiento = self.detectar_tipo_movimiento(posicion_mapa)
        if self.tipo_movimiento == "fin":
            self.setPixmap(self.pixmap_principal)
        else:
            self.comenzar_animacion()
            self.movimiento_casilla = QPropertyAnimation(self, b"pos")
            self.movimiento_casilla.setEndValue(QPoint(*posicion_mapa))
            self.movimiento_casilla.setDuration(p.TIEMPO_PASOS * 3)
            self.movimiento_casilla.start()
