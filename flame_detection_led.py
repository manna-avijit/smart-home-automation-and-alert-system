from machine import Pin
import time

# Initialize flame sensor (Pin 16) and LED (Pin 3)
flame_sensor = Pin(16, Pin.IN)
led3 = Pin(3, Pin.OUT)

# Function to check for flame detection
def check_flame():
    if flame_sensor.value() == 0:
        led3.on()  # Turn on LED if flame is detected
        print("** Fire detected!!! **")
    else:
        led3.off()  # Turn off LED if no flame
        print("No Fire detected")

while True:
    check_flame()  # Continuously monitor flame sensor
    time.sleep(2)