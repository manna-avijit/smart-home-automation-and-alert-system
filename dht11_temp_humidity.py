from machine import Pin
import time
from dht import DHT11

# Initialize DHT11 sensor (Pin 10)
sensor_pin = Pin(10, Pin.OUT)
sensor = DHT11(sensor_pin)

# Function to read temperature and humidity
def read_dht11():
    sensor.measure()  # Trigger a new measurement
    temperature = sensor.temperature()  # Get temperature
    humidity = sensor.humidity()  # Get humidity
    print("Temperature: {}°C".format(temperature))
    print("Humidity: {}%".format(humidity))

while True:
    read_dht11()  # Continuously monitor temperature and humidity
    time.sleep(2)