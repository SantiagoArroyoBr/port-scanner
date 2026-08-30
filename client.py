import socket
import threading

def Escaneo(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    resultado = s.connect_ex(('127.0.0.1', port))
    if resultado == 0:
        print(port, "puerto abierto")
    s.close()

for port in range(1, 65536):
    hilo = threading.Thread(target=Escaneo, args=(port,))
    hilo.start()