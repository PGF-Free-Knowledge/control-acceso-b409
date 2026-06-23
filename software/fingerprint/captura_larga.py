import serial
import time

puerto = serial.Serial(
    "/dev/ttyAMA5",
    baudrate=19200,
    timeout=0.2
)

print("Puerto abierto")

comando = bytes([
    0xF5, 0x01, 0x00, 0x00,
    0x00, 0x00, 0x01, 0xF5
])

puerto.write(comando)

print("Esperando actividad durante 30 segundos...")

for i in range(300):

    datos = puerto.read(64)

    if len(datos) > 0:
        print("RECIBIDO:", datos.hex())

    time.sleep(0.1)

puerto.close()

print("Fin")