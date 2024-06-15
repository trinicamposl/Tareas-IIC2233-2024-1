from PyQt6.QtCore import QObject, pyqtSignal
import frontend.Tablero as tablero


class Usuario(QObject):
    signal_intentar_empezar = pyqtSignal(str)
    signal_empezar = pyqtSignal(bool)
    signal_datos = pyqtSignal(list)

    def __init__(self):
        super().__init__()
        self.puede = False

    def revisar_texto(self, texto):
        if texto.isalnum() and texto.lower() != texto:
            for elemento in texto:
                if elemento in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    self.puede = True
        self.signal_empezar.emit(self.puede)

    def guardar_datos(self, lista):
        self.nombre = lista[0]
        self.nivel = lista[1]
        self.crear_tablero(self.nivel)

    def crear_tablero(self, parametro):
        crear_tablero = tablero.Tablero(parametro)
        crear_tablero.show()



# backend.signal_intentar_empezar.connect(revisar_texto)
# frontend.signal_empezar.connect(recibir_info):
