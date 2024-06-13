import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QFont
from Tablero import Tablero


if __name__ == '__main__':
    def hook(type, value, traceback) -> None:
        print(type)
        print(traceback)
    sys.__excepthook__ = hook

    app = QApplication([])
    # a = QFontDatabase.addApplicationFont(p.PATH_LETRA)
    font = QFont("Cascadia Mono SemiBold", 10)
    app.setFont(font)  # Creamos las base de la app: QApplication.
    ventana = Tablero("experto_1.txt")
    ventana2 = Tablero("novato_1.txt")   # Construimos un QWidget que será nuestra ventana.
    ventana3 = Tablero("intermedio_1.txt")
    ventana.show()
    ventana3.show()  # Mostramos la ventana.
    ventana2.show()
    sys.exit(app.exec())
    