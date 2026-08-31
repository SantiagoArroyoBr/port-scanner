import socket
import threading
import ipaddress

def Escaneo(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    resultado = s.connect_ex((direccion, port))
    if resultado == 0:
        print(port, "puerto abierto")
    s.close()

Validacion = False

#Checar ip valida
while not Validacion:
    try:
        direccion = input("Ingrese una direccion IP valida: ")
        ipaddress.ip_address(direccion)
        Validacion = True
    except ValueError:
        print("Ip invalida")

#Checar PORTS
for port in range(1, 65536):
    hilo = threading.Thread(target=Escaneo, args=(port,))
    hilo.start()