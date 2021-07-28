import requests
import random
import time
from datetime import date, datetime

temperature = 30.0
lastTemperature = 30.0
humidity = 20.0
lastHumidity = 20.0

actualTime = datetime.now()
date = actualTime.strftime("%d/%m/%Y %H:%M:%S")

print("Welcome to the greenhouse sensor terminal")

IdArduino = "IdArduino_1"

REQUEST_URL = f"https://app-api-iot.herokuapp.com/createGreenhouse/?IdArduino={IdArduino}&date={date}"
_request = requests.get(REQUEST_URL)
print(_request.text)

def sensorStatus(temperature, lastTemperature, humidity, lastHumidity):
    
    if((lastTemperature-temperature)>=1 or (temperature-lastTemperature)>=1):
        return True
    elif((lastHumidity-humidity)>=1 or (humidity-lastHumidity)>=1):
        return True
    else:
        return False

while True:
    
    temperature = round(random.uniform(temperature-2, temperature+2),2)
    if temperature > 40:
        temperature = 40
    elif temperature < 0:
        temperature = 0
    
    humidity = round(random.uniform(humidity-10, humidity+10),2)
    if humidity > 50:
        humidity = 50
    elif humidity < 3:
        humidity = 3

    
    actualTime = datetime.now()
    date = actualTime.strftime("%d/%m/%Y %H:%M:%S")

    
    if(sensorStatus(temperature, lastTemperature, humidity, lastHumidity)):
        """ The request for the data """
        REQUEST_URL = f"https://app-api-iot.herokuapp.com/insertData/?IdArduino={IdArduino}&temperature={temperature}&humidity={humidity}&date={date}"
        _request = requests.get(REQUEST_URL)
        print(_request.text)

    # The variables for the last measurement are updated
    lastTemperature = temperature
    lastHumidity = humidity

    # Three seconds to start the next measurement
    time.sleep(15)