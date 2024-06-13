from Tablero import Tablero
from TiempoBotones import Tiempo
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtGui import QFont, QPixmap, QMouseEvent, QKeyEvent
from PyQt6.QtCore import Qt, pyqtSignal, QUrl, QTimer
from PyQt6.QtWidgets import QHBoxLayout, QWidget, QComboBox, QFormLayout, QLineEdit, QGridLayout
from PyQt6.QtWidgets import QLabel, QPushButton, QScrollArea, QVBoxLayout, QApplication
import sys

ventana = Tablero("experto_1.txt")   # Construimos un QWidget que será nuestra ventana.
tiempo = Tiempo("experto_1.txt")

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

