import requests
import random
import time
from datetime import date, datetime

temperature = 30
lastTemperature = 30
humidity = 20
lastHumidity = 20

print("Esta es la id de su sistema arduino")

IdArduino = "6519150005"

print(IdArduino)

 
def sensorStatus(temperature, lastTemperature, humidity, lastHumidity):
    
    if(temperature != lastTemperature):
        return True
    elif(humidity != lastHumidity):
        return True
    else:
        return False

while True:
    
    temperature = round(random.uniform(temperature-5, temperature+5),2)
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
        REQUEST_URL = f"https://greenhouse-iot-api.herokuapp.com/insertData/?IdArduino={IdArduino}&temperature={temperature}&humidity={humidity}&date={date}"
        _request = requests.get(REQUEST_URL)
        print(_request.text)

    lastTemperature = temperature
    lastHumidity = humidity

    time.sleep(3)