import requests
import json

option = True



print("Welcome to the app")

while option:
    IdSensor = input("Please enter the id sensor: ")

    SensorValue = input("Please insert the value of the sensor: ")

    REQUEST_URL = f"https://app-api-iot.herokuapp.com/option/?IdSensor={IdSensor}&SensorValue={SensorValue}"
    _request = requests.get(REQUEST_URL)

    print("Do you like to continue? [Y/N]")

    _option = input()
    _option = _option.lower()

    if _option == 'y':
        option = True
    else:
        option = False