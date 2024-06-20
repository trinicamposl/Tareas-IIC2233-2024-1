# no sé
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QFont
import frontend.VentanaDeInicio as frontend_inicio
import backend.backend as backend
import frontend.Tablero as tablero
import sys
from funciones import leer_json


class Empezar:
    def __init__(self, puerto: str) -> None:

        self.puerto = puerto
        parametros = leer_json("parametros.json")
        self.host = parametros["host"]
        self.frontend_inicio = frontend_inicio.VentanaInicio()
        self.backend = backend.Usuario(self.host, self.puerto)
        self.backend_tablero = None
        self.tablero_juego = None
        self.pepa = None
        self.nivel = None
        self.modo = "inicio"
        self.conectado = False
        self.popup = None
        self.en_silencio = False

        self.backend.signal_cerrar_ventana.connect(self.cerrar)
        self.backend.signal_actualizar_conectado.connect(self.actualizar_conectado)
        self.backend.signal_enviar_alerta.connect(self.crear_popup)
        self.frontend_inicio.signal_intentar_empezar.connect(self.backend.revisar_texto)
        self.backend.signal_empezar.connect(self.frontend_inicio.recibir_info)
        self.frontend_inicio.signal_empezo_juego.connect(self.iniciar_juego)
        self.frontend_inicio.signal_datos.connect(self.backend.guardar_datos)
        self.backend.signal_crear_tablero.connect(self.crear_tablero)
        self.backend.signal_estaba_mal.connect(self.perdiste)

    def iniciar(self) -> None:
        if self.conectado:
            self.frontend_inicio.show()

    def iniciar_juego(self, mensaje, texto):
        if mensaje:
            self.frontend_inicio.hide()
            self.modo = "juego"
        else:
            self.frontend_inicio.signal_popup.emit(texto)

    def crear_tablero(self, nivel, mute):
        self.nivel = nivel
        self.tablero_juego = tablero.Tablero(nivel)
        self.tablero_juego.mute = mute
        self.tablero_juego.show()
        self.conectar_juego()

    def conectar_juego(self):
        self.backend_tablero = backend.Tablero()
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
        self.backend_tablero.signal_sandia.connect(self.tablero_juego.aparecer_sandia)
        self.tablero_juego.signal_comprobar.connect(self.backend.calcular_puntaje)
        self.backend.signal_pedir_tablero.connect(self.backend_tablero.enviar_tablero)
        self.backend_tablero.signal_tablero.connect(self.backend.comprobar)
        self.backend.signal_ganaste.connect(self.ganaste)
        self.tablero_juego.signal_pausa.connect(self.hacer_pausa)

    def mandar_info(self, datos):
        self.backend_tablero.signal_inicial.emit(datos)

    def actualizar_conectado(self) -> None:
        self.conectado = True
        self.iniciar()

    def cerrar(self):
        if self.modo == "inicio":
            if self.frontend_inicio is not None:
                self.frontend_inicio.close()
        else:
            self.tablero_juego.close()
        if not self.conectado:
            sys.exit()

    def crear_popup(self, mensaje):
        if self.frontend_inicio is not None:
            self.frontend_inicio.hide()
        elif self.tablero_juego is not None:
            self.tablero_juego.hide()
        self.popup = frontend_inicio.Popup(mensaje)
        self.popup.show()
        QTimer.singleShot(5000, lambda: self.popup.hide())

    def perdiste(self):
        mensaje = "Tu solución no era la correcta :(\n      Perdiste."
        self.tablero_juego.signal_perdiste.emit()
        self.tablero_juego.hide()
        self.popup = frontend_inicio.Popup(mensaje)
        self.popup.show()
        QTimer.singleShot(6000, lambda: self.popup.hide())
        QTimer.singleShot(1000, lambda: self.frontend_inicio.show())

    def ganaste(self, puntaje):
        self.tablero_juego.tiempo_infinito()
        self.tablero_juego.hide()
        self.frontend_inicio.actualizar_salon()
        self.frontend_inicio.show()
        mensaje = f"Ganaste!!!! Felicitacionesssss. Tuviste {puntaje} puntos"
        self.popup = frontend_inicio.Popup(mensaje)
        self.popup.show()
        self.tablero_juego.signal_ganaste.emit()

    def hacer_pausa(self):
        self.tablero_juego.hide()
        mensaje = "Tu juego está pausado"
        self.popup = frontend_inicio.Popup(mensaje)
        self.popup.show()
        self.popup.accepted.connect(self.despausar)
        self.popup.rejected.connect(self.despausar)

    def despausar(self):
        self.tablero_juego.show()
        self.tablero_juego.despausa()


if __name__ == "__main__":

    def hook(type_, value, traceback):
        print(type_)
        print(traceback)

    sys.__excepthook__ = hook


if __name__ == '__main__':
    def hook(type_, value, traceback):
        print(type_)
        print(traceback)

    sys.__excepthook__ = hook
    if len(sys.argv) < 2:
        print("Recuerda especificar un puerto")
    elif not sys.argv[1].isnumeric():
        print("Recuerda especificar un puerto que sea un número.")
    else:
        puerto = int(sys.argv[1])
        app = QApplication([])
        font = QFont("Cascadia Mono SemiBold", 14)
        app.setFont(font)
        juego = Empezar(puerto)
        sys.exit(app.exec())
