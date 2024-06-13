from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QWidget
from PyQt6.QtWidgets import QLabel
import parametros as p


class Tiempo(QWidget):
    def __init__(self, nivel: str):
        super().__init__()
        self.duration = p.TIEMPO_JUEGO[nivel.split("_")[0]]
        self.label2 = QLabel()
        self.label2.setStyleSheet('border: 1px solid black')
        self.label2.setText(f'Te quedan {self.duration} segundos.')
        self.label2.show()
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(1000)

    def update(self):
        self.label2.setText(f'Te quedan {self.duration} segundos.')
        self.duration -= 1

        if self.duration < 0:
            self.timer.stop()
            exit()  # perdiste!

    def aumento(self, cuanto):
        pass

