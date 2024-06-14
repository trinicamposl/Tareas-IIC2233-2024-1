# no sé
from PyQt6.QtWidgets import QApplication
from frontend import VentanaDeInicio
from backend import Usuario
import sys


class Empezar:
    def __init__(self) -> None:
        """
        Instanciamos todas las ventanas y clases necesarias
        """
        self.frontend_inicio = VentanaDeInicio()
        self.backend = Usuario()

    def conectar(self) -> None:
        # # Backend le avisa al frontend del juego que empieza el juego
        # self.backend.senal_empezar_juego(self.frontend_juego.empezar_juego)
        # Backend notifica al frontend_juego cuando se empieza
        self.backend.signal_intentar_empezar.connect(self.frontend_juego.revisar_texto)
        self.frontend.signal_empezar.connect(self.backend.recibir_info)

    def iniciar(self) -> None:
        self.frontend_inicio.show()


if __name__ == "__main__":

    def hook(type_, value, traceback):
        print(type_)
        print(traceback)

    sys.__excepthook__ = hook

    app = QApplication([])
    juego = Empezar()
    juego.conectar()
    juego.iniciar()

    sys.exit(app.exec())
