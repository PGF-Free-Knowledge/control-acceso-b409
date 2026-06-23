from gpiozero import DigitalInputDevice
from time import sleep

pin12 = DigitalInputDevice(12)
pin13 = DigitalInputDevice(13)

print("Monitoreando GPIO12 y GPIO13")

while True:
    print(
        f"GPIO12={pin12.value}  GPIO13={pin13.value}"
    )
    sleep(1)