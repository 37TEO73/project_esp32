# Escribe tu código aquí :-)
try:
    import urequests as requests
except ImportError:
    import requests

import network
import time

import esp
esp.osdebug(None)

import gc
gc.collect()

# Your network credentials
ssid = "ARRIS-EE79"
password = "23060129M"

# Your phone number in international format
phone_number = "+573216391561"
# Your callmebot API key
api_key = "1366787"

def connect_wifi(ssid, password):
    # Connect to your network
    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.connect(ssid, password)

    while not station.isconnected():
        time.sleep(1)  # Sleep for a second to avoid spamming

    print('Connection successful')
    print(station.ifconfig())

def send_message(phone_number, api_key, message):
    # Set your host URL
    url = f'https://api.callmebot.com/whatsapp.php?phone={phone_number}&text={message}&apikey={api_key}'

    # Make the request
    response = requests.get(url)

    # Check if it was successful
    if response.status_code == 200:
        print('Success!')
    else:
        print('Error')
        print(response.text)

# Connect to WiFi
connect_wifi(ssid, password)

# Send message to WhatsApp "Hello"
message = 'MOVIMIENTO%20DETECTADO!!!!!'  # YOUR MESSAGE HERE (URL ENCODED) https://www.urlencoder.io/



from machine import Pin
import time

# Pin numbers for LED and sensor
led_pin = 2
sensor_pin = 12

# Set the LED pin as an output and the sensor pin as an input
led = Pin(led_pin, Pin.OUT)
sensor = Pin(sensor_pin, Pin.IN)

# Initialize state variables
state = 0
val = 0

while True:
    val = sensor.value()  # read sensor value

    if val == 1:  # check if the sensor is HIGH
        led.on()  # turn LED ON

        if state == 0:
            send_message(phone_number, api_key, message)
            state = 1  # update variable state to HIGH

    # Add a small delay to avoid constant checking of the sensor
    time.sleep(0.1)