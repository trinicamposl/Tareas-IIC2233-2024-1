# no sé
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QFont
import frontend.VentanaDeInicio as frontend_inicio
import backend.backend as backend
import sys


class Empezar:
    def __init__(self) -> None:
        """
        Instanciamos todas las ventanas y clases necesarias
        """
        self.frontend_inicio = frontend_inicio.VentanaInicio()
        self.backend = backend.Usuario()
        self.conectar()

    def conectar(self) -> None:
        # # Backend le avisa al frontend del juego que empieza el juego
        # self.backend.senal_empezar_juego(self.frontend_juego.empezar_juego)
        # Backend notifica al frontend_juego cuando se empieza
        self.frontend_inicio.signal_intentar_empezar.connect(self.backend.revisar_texto)
        self.backend.signal_empezar.connect(self.frontend_inicio.recibir_info)
        self.frontend_inicio.signal_empezo_juego.connect(self.iniciar_juego)
        self.frontend_inicio.signal_datos.connect(self.backend.guardar_datos)

    def iniciar(self) -> None:
        self.frontend_inicio.show()

    def iniciar_juego(self, mensaje):
        if mensaje:
            self.frontend_inicio.hide()
        else:
            self.frontend_inicio.signal_popup.emit()


if __name__ == "__main__":

    def hook(type_, value, traceback):
        print(type_)
        print(traceback)

    sys.__excepthook__ = hook

    app = QApplication([])
    font = QFont("Cascadia Mono SemiBold", 10)
    app.setFont(font)
    juego = Empezar()
    juego.conectar()
    juego.iniciar()

    sys.exit(app.exec())
    