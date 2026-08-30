# Port Scanner

Proyecto de portafolio: escáner de puertos TCP en Python, usando sockets y concurrencia con threading.

## Qué hace

Escanea un rango de puertos (por default 1-65535) sobre una IP objetivo (por default `localhost`) e imprime los puertos que encuentra abiertos.

Usa múltiples hilos (threading) para escanear en paralelo en vez de uno por uno, reduciendo drásticamente el tiempo total de escaneo.

## Requisitos

Solo necesitas tener Python instalado (usa únicamente librerías estándar: `socket` y `threading`).

## Cómo correrlo

Desde la terminal:

python main.py

O ábrelo y corre `main.py` directamente desde tu editor de código.

## Aviso ético

Esta herramienta está pensada únicamente para usarse sobre redes y equipos propios, o con autorización explícita del dueño de la red/equipo. Escanear puertos de sistemas de terceros sin permiso puede ser ilegal dependiendo de la jurisdicción. Este proyecto es solo con fines educativos y de portafolio.

## Qué aprendí

- Uso de sockets TCP (`socket.AF_INET`, `socket.SOCK_STREAM`) y `.connect_ex()` para probar conexiones sin manejar excepciones
- Configuración de timeouts para evitar esperas innecesarias
- Por qué reutilizar un mismo socket para múltiples conexiones causa errores, y cómo evitarlo
- Concurrencia básica con `threading.Thread` para acelerar tareas de espera (I/O bound)