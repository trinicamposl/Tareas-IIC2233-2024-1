import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QStackedLayout
from PyQt6.QtGui import QFont
from Tablero import Tablero

if __name__ == '__main__':
    def hook(type, value, traceback) -> None:
        print(type)
        print(value)
        print(traceback)
    sys.excepthook = hook

    app = QApplication([])

    # Configuramos la fuente
    font = QFont("Cascadia Mono SemiBold", 12)
    app.setFont(font)

    tablero = Tablero("novato_1.txt")
    tablero.show()

    sys.exit(app.exec())
