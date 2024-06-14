from PyQt6.QtCore import QObject, pyqtSignal


class Usuario(QObject):
    signal_intentar_empezar = pyqtSignal(list)
    signal_empezar = pyqtSignal(list)

    def __init__(self, nivel):
        super().__init__()
        self.nivel = nivel
        self.puede = False

    def revisar_texto(self, texto):
        if texto.isalnum() and texto.lower() != texto:
            for elemento in texto:
                if elemento in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    self.puede = True
        self.signal_empezar.emit(self.puede)

# backend.signal_intentar_empezar.connect(revisar_texto)
# frontend.signal_empezar.connect(recibir_info):
