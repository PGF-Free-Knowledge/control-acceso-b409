from gpiozero import Button
from time import sleep

rx = Button(13)

print("Esperando actividad en GPIO13...")

while True:

    if rx.is_pressed:
        print("Actividad detectada")

    sleep(0.1)