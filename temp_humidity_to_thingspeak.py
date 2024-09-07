import machine
import urequests
import network
import time
from machine import Pin
from DHT11 import DHT11, InvalidChecksum

# Constants for the HTTP request
HTTP_HEADERS = {'Content-Type': 'application/json'}

# User should enter their ThingSpeak Write API Key here
THINGSPEAK_WRITE_API_KEY = 'ENTER_YOUR_API_KEY_HERE'

# User should enter their Wi-Fi credentials here
ssid = 'ENTER_YOUR_SSID_HERE'
password = 'ENTER_YOUR_PASSWORD_HERE'

# Function to connect to Wi-Fi
def connect_to_wifi(ssid, password):
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)

    if not sta_if.isconnected():
        print('Connecting to Wi-Fi...')
        sta_if.connect(ssid, password)
        while not sta_if.isconnected():
            pass
    print('Connected! Network config:', sta_if.ifconfig())

# Main loop to read DHT11 sensor data and send to ThingSpeak
def send_data_to_thingspeak():
    # Pin configuration for DHT11 sensor (Pin 10 is used in this example)
    pin = Pin(10, Pin.OUT, Pin.PULL_DOWN)
    sensor = DHT11(pin)

    while True:
        try:
            # Read temperature and humidity from sensor
            temperature = sensor.temperature
            humidity = sensor.humidity
            print(f"Temperature: {temperature}°C, Humidity: {humidity}%")

            # Prepare data to send to ThingSpeak
            dht_readings = {'field1': temperature, 'field2': humidity}

            # Send data to ThingSpeak
            url = f"http://api.thingspeak.com/update?api_key={THINGSPEAK_WRITE_API_KEY}"
            request = urequests.post(url, json=dht_readings, headers=HTTP_HEADERS)
            request.close()

            print("Data sent to ThingSpeak:", dht_readings)

        except InvalidChecksum:
            print("Checksum error reading from DHT11 sensor. Retrying...")

        # Wait 15 seconds before the next reading (ThingSpeak allows updates every 15 seconds)
        time.sleep(15)

# Connect to Wi-Fi
connect_to_wifi(ssid, password)

# Start sending sensor data to ThingSpeak
send_data_to_thingspeak()