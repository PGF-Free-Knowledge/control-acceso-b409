import serial
import time

try:

    puerto = serial.Serial(
        "/dev/ttyAMA5",
        baudrate=19200,
        timeout=2
    )

    print("Lector conectado")

    comando = bytes([
        0xF5, 0x01, 0x00, 0x00,
        0x00, 0x00, 0x01, 0xF5
    ])

    print("Solicitando captura...")

    puerto.write(comando)

    time.sleep(1)

    respuesta = puerto.read(32)

    if respuesta:

        print("Respuesta:")
        print(respuesta.hex())

    else:

        print("Sin respuesta")

    puerto.close()

except Exception as e:

    print("ERROR:")
    print(e)