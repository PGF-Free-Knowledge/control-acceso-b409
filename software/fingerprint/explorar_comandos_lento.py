import serial
import time

for cmd in range(6, 17):

    print()
    print("========================================")
    print(f"COMANDO 0x{cmd:02X}")
    print("========================================")

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

        print("Enviando comando...")

        puerto.write(paquete)

        respuesta = puerto.read(64)

        if respuesta:

            print("RESPUESTA:")
            print(respuesta.hex())

        else:

            print("SIN RESPUESTA")

        puerto.close()

    except Exception as e:

        print("ERROR:", e)

    print()
    print(">>> OBSERVE EL LECTOR AHORA <<<")
    print("Esperando 5 segundos...")
    print()

    time.sleep(5)

print()
print("FIN DE LA PRUEBA")