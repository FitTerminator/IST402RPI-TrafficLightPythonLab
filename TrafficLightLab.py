from gpiozero import Button
from gpiozero import LED
from gpiozero import Buzzer
from time import sleep

button = Button(2)
buzzer = Buzzer(3)
redled = LED(13)
yellowled = LED(19)
greenled = LED(26)

redled.on()

while True:
    if button.is_pressed:
        redled.off()
        greenled.on()
        buzzer.on()
        sleep(0.25)
        buzzer.off()
        sleep(0.25)
        buzzer.on()
        sleep(0.25)
        buzzer.off()
        sleep(0.25)
        buzzer.on()
        sleep(0.25)
        buzzer.off()
        sleep(0.25)
        buzzer.on()
        sleep(0.25)
        buzzer.off()
        sleep(0.25)
        greenled.off()
        buzzer.off()
        yellowled.on()
        sleep(1)
        yellowled.off()
        redled.on()
        