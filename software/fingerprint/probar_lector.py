import serial
import time

try:

    puerto = serial.Serial(
        "/dev/ttyAMA5",
        baudrate=19200,
        timeout=2
    )

    print("Puerto abierto correctamente")

    comando = bytes([
        0xF5, 0x09, 0x00, 0x00,
        0x00, 0x00, 0x09, 0xF5
    ])

    print("Enviando comando...")

    puerto.write(comando)

    time.sleep(0.5)

    respuesta = puerto.read(32)

    if respuesta:

        print("Respuesta recibida:")
        print(respuesta.hex())

    else:

        print("No hubo respuesta")

    puerto.close()

except Exception as e:

    print("ERROR:")
    print(e)