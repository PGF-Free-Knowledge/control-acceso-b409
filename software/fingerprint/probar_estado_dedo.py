import serial
import time

puerto = serial.Serial(
    "/dev/ttyAMA5",
    baudrate=19200,
    timeout=1
)

comando = bytes([
    0xF5,
    0x05,
    0x00,
    0x00,
    0x00,
    0x00,
    0x05,
    0xF5
])

for i in range(10):

    puerto.write(comando)

    respuesta = puerto.read(64)

    if respuesta:
        print(respuesta.hex())

    time.sleep(1)

puerto.close()