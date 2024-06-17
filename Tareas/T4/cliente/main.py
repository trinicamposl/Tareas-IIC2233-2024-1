# no sé
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QFont
import frontend.VentanaDeInicio as frontend_inicio
import backend.backend as backend
import frontend.Tablero as tablero
import sys


class Empezar:
    def __init__(self) -> None:
        """
        Instanciamos todas las ventanas y clases necesarias
        """
        self.frontend_inicio = frontend_inicio.VentanaInicio()
        self.backend = backend.Usuario()
        self.backend_tablero = None
        self.conectar()
        self.tablero_juego = None
        self.pepa = None
        self.nivel = None

    def conectar(self) -> None:
        # # Backend le avisa al frontend del juego que empieza el juego
        # self.backend.senal_empezar_juego(self.frontend_juego.empezar_juego)
        # Backend notifica al frontend_juego cuando se empieza
        self.frontend_inicio.signal_intentar_empezar.connect(self.backend.revisar_texto)
        self.backend.signal_empezar.connect(self.frontend_inicio.recibir_info)
        self.frontend_inicio.signal_empezo_juego.connect(self.iniciar_juego)
        self.frontend_inicio.signal_datos.connect(self.backend.guardar_datos)
        self.backend.signal_crear_tablero.connect(self.crear_tablero)
        self.iniciar()

    def iniciar(self) -> None:
        self.frontend_inicio.show()

    def iniciar_juego(self, mensaje):
        if mensaje:
            self.frontend_inicio.hide()
        else:
            self.frontend_inicio.signal_popup.emit()

    def crear_tablero(self, nivel):
        self.nivel = nivel
        self.tablero_juego = tablero.Tablero(nivel)
        self.tablero_juego.show()
        self.conectar_juego()

    def conectar_juego(self):
        self.backend_tablero = backend.Tablero()
        self.backend.signal_tiempo_final.connect(self.backend_tablero.signal_tiempo_final)
        self.backend_tablero.signal_perdiste.connect(self.frontend_inicio.volver_perdido)
        self.backend_tablero.signal_perdiste.connect(self.tablero_juego.retirada)
        self.tablero_juego.signal_salir.connect(self.frontend_inicio.volver)
        self.frontend_inicio.signal_parar_tiempo.connect(self.backend.reiniciar_tiempo)
        self.backend_tablero.signal_crear_pepa.connect(self.tablero_juego.definir_Pepa)
        self.backend_tablero.signal_crear_pepa.emit()
        self.tablero_juego.signal_posicion.connect(self.mandar_info)
        self.backend.signal_empezar_tiempo.emit()
        self.tablero_juego.signal_silenciar.connect(self.frontend_inicio.silenciar)
        self.tablero_juego.signal_mover.connect(self.backend_tablero.mover)
        self.backend_tablero.signal_mover.connect(self.tablero_juego.mover_pepa)
        self.backend_tablero.signal_pedir_coordenadas.connect(self.tablero_juego.dar_coordenadas)
        self.tablero_juego.signal_dar_coordenadas.connect(self.backend_tablero.mover_final)
        self.tablero_juego.signal_relleno.connect(self.backend_tablero.relleno)
        self.backend_tablero.signal_enviar_accion.connect(self.tablero_juego.rellenar)
        self.tablero_juego.signal_tiempo_restante.connect(self.backend_tablero.actualizar_restante)

    def mandar_info(self, datos):
        self.backend_tablero.signal_inicial.emit(datos)


if __name__ == "__main__":

    def hook(type_, value, traceback):
        print(type_)
        print(traceback)

    sys.__excepthook__ = hook

    app = QApplication([])
    font = QFont("Cascadia Mono SemiBold", 10)
    app.setFont(font)
    juego = Empezar()
    sys.exit(app.exec())
