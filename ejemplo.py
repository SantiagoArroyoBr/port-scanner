import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(0.5)

inicio = time.time()
resultado = s.connect_ex(('127.0.0.1', 9999))  # un puerto que sabes que está cerrado
fin = time.time()

print("resultado:", resultado)
print("tiempo que tardó:", fin - inicio, "segundos")
s.close()


    