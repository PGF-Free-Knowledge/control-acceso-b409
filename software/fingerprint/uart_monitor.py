import serial

puerto = serial.Serial(
    '/dev/serial0',
    baudrate=19200,
    timeout=2
)

print("Escuchando UART...")

while True:
    datos = puerto.read(64)

    if len(datos) > 0:
        print(datos.hex())
