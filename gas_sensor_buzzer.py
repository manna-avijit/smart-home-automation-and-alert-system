from machine import ADC, Pin
import time

# Initialize gas sensor (Pin 26) and buzzer (Pin 13)
gas_sensor = ADC(Pin(26))
buzzer = Pin(13, Pin.OUT)

def buzz(duration):
    buzzer.value(1)  # Turn on buzzer
    time.sleep(duration)  # Keep buzzer on for specified duration
    buzzer.value(0)  # Turn off buzzer
    time.sleep(duration)

# Function to read gas sensor and trigger buzzer if threshold is exceeded
def gas_sensor1():
    gas_value = gas_sensor.read_u16()  # Read the gas sensor value
    voltage = gas_value * 3.3 / 65535  # Convert the value to voltage
    print("Gas Sensor Value:", gas_value)
    print("Voltage:", voltage)

    if gas_value >= 15000:
        print("Danger!! Gas levels too high!")
        buzz(0.5)  # Activate buzzer for 0.5 seconds
    else:
        print("Gas levels normal")
    
    time.sleep(1)  # Delay before the next reading

while True:
    gas_sensor1()  # Continuously monitor gas levels