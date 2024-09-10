from machine import Pin
import time

# Initialize LED and PIR sensor
led2 = Pin(4, Pin.OUT)
pir_sensor = Pin(15, Pin.IN)

# Function to detect motion and control the LED
def detect_motion(pin):
    if pin.value() == 1:
        led2.on()  # Turn LED on when motion is detected
        print("Motion detected!")
    else:
        led2.off()  # Turn LED off when no motion
        print("No motion")

while True:
    detect_motion(pir_sensor)
    time.sleep(2)