import serial
import time

for cmd in range(6, 17):

    print()
    print("======================")
    print(f"Probando comando: 0x{cmd:02X}")
    print("======================")

    try:

        puerto = serial.Serial(
            "/dev/ttyAMA5",
            baudrate=19200,
            timeout=1
        )

        paquete = bytes([
            0xF5,
            cmd,
            0x00,
            0x00,
            0x00,
            0x00,
            cmd,
            0xF5
        ])

        puerto.write(paquete)

        respuesta = puerto.read(64)

        if respuesta:
            print("RESPUESTA:")
            print(respuesta.hex())
        else:
            print("Sin respuesta")

        puerto.close()

    except Exception as e:

        print("ERROR:", e)

    time.sleep(1)