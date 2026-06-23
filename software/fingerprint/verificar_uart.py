import serial

puerto = serial.Serial(
    "/dev/serial0",
    baudrate=9600,
    timeout=1
)

print("Puerto abierto:", puerto.name)

while True:
    datos = puerto.read(32)

    if datos:
        print(datos.hex())
