from time import sleep
import network
from machine import Pin
import BlynkLib

# Initialize LED on Pin 11
led1 = Pin(11, Pin.OUT)

# User should enter their Wi-Fi credentials here
ssid = 'ENTER_YOUR_SSID_HERE'
password = 'ENTER_YOUR_PASSWORD_HERE'

# User should enter their Blynk Auth Token here
BLYNK_AUTH = 'ENTER_YOUR_BLYNK_AUTH_TOKEN_HERE'

# Connect to Wi-Fi
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)

if not sta_if.isconnected():
    print('Connecting to Wi-Fi...')
    sta_if.connect(ssid, password)
    while not sta_if.isconnected():
        pass
print('Connected! Network config:', sta_if.ifconfig())

# Initialize Blynk with the provided authentication token
blynk = BlynkLib.Blynk(BLYNK_AUTH)

# Register virtual pin handler for V0 (Blynk virtual pin)
@blynk.on("V0")
def v0_write_handler(value):
    # Check the value sent by Blynk (either "1" or "0")
    if int(value[0]) == 1:
        led1.value(1)  # Turn LED on
        print("LED ON")
    else:
        led1.value(0)  # Turn LED off
        print("LED OFF")

# Run Blynk continuously to listen for commands
while True:
    blynk.run()