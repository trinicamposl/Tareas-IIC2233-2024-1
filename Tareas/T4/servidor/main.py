import socket
import sys
from funciones_servidor import leer_json
from threading import Thread, Lock
import pickle
from funciones_servidor import decodificar, codificar, revisar
import parametros_servidor as p


def escuchar_cliente(jugador: object, lock: Lock, dato: str) -> None:
    """Se encarga de recibir los mensajes del cliente e interpretarlos"""
    socket_cliente = jugador
    while True:
        try:
            bytes_largo_datos = socket_cliente.recv(4)
            largo_datos = int.from_bytes(bytes_largo_datos,
                                         byteorder="big")
            respuesta = bytearray()
            respuesta += bytearray(bytes_largo_datos)
            bytes_totales = ((25 + 3) * ((largo_datos // 25))) + 3
            if largo_datos % 25 != 0:
                bytes_totales += (25 + 4)  # Chunk extra
            if len(bytes_largo_datos) == 0:
                # Desconexión.
                break
            # Lectura de los bytes
            while len(respuesta) < bytes_totales:
                bytes_lectura = min(4096, (bytes_totales) - len(respuesta))
                respuesta_bytes = socket_cliente.recv(bytes_lectura)
                respuesta += bytearray(respuesta_bytes)
            # Desencriptación y obtención del objeto
            with lock:
                mensaje = pickle.loads(decodificar(respuesta))
                veredicto = revisar(mensaje)
                if veredicto:
                    with open(p.PATH_PUNTAJES, "a", encoding="utf-8") as archivo:
                        archivo.write(f"{mensaje[2]}---{mensaje[3]}\n")
                    socket_cliente.sendall(codificar(pickle.dumps(True)))
                else:
                    socket_cliente.sendall(codificar(pickle.dumps(False)))
        except BrokenPipeError:
            print(f"Cliente {dato} fue desconectado.")
            break
        except ConnectionResetError:
            print(f"Cliente {dato} fue desconectado.")
            break
        except AttributeError:
            # Ya se ha des-asignado el cliente.
            break


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Recuerda especificar el puerto!")
    elif not sys.argv[1].isnumeric():
        print("Recuerda especificar un puerto numérico")
    else:
        path_parametros = "parametros.json"
        parametros = leer_json(path_parametros)
        host = parametros["host"]
        port = int(sys.argv[1])
        lock_escuchar = Lock()
        # Se crea el socket, hacemos bind y listen
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind((host, port))
            sock.listen()
        except PermissionError:
            print("Intenta con un puerto superior a 1024.")
            sys.exit()
        except OSError:
            print("El puerto ya se encuentra ocupado.")
            sys.exit()
        while True:
            try:
                print(f"Recibiendo conexiones en {port}.")
                # Aceptamos a un cliente
                socket_cliente, address = sock.accept()
                print(f"Nueva conexión: IP -> {address[0]}; " f"puerto -> {address[1]}")
                # Creamos un thread encargado de escuchar a ese cliente
                thread = Thread(target=escuchar_cliente,
                                args=(socket_cliente, lock_escuchar, address[1]),
                                daemon=True)
                thread.start()

            except ConnectionError:
                print("Ocurrió un error en la conexión.")
                sys.exit()
