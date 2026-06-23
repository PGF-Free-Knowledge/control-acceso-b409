import serial
import time

baud_rates = [9600, 19200, 38400, 57600]

uart_port = "/dev/ttyAMA5"

test_command = bytes([
    0xF5, 0x09, 0x00, 0x00,
    0x00, 0x00, 0x09, 0xF5
])

for baud in baud_rates:

    print()
    print("========================")
    print("Probando:", baud, "bps")
    print("========================")

    try:

        ser = serial.Serial(
            uart_port,
            baudrate=baud,
            timeout=1
        )

        ser.reset_input_buffer()

        ser.write(test_command)

        time.sleep(0.2)

        response = ser.read(32)

        if response:

            print("RESPUESTA:")
            print(response.hex())

        else:

            print("Sin respuesta")

        ser.close()

    except Exception as e:

        print("ERROR:")
        print(e)
