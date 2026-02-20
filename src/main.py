import urequests
import network
import time
from machine import I2C, Pin
from lcd import Lcd_i2c
import secrets

ssid = 'SPS-PROSEK HOST'
password = 'vyuka3ITmqtt'
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid)

i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)
lcd = Lcd_i2c(i2c)

url = "http://ip-api.com/json/78.102.17.227"
x = urequests.get(url)
print(x.json())
x.close()


url_weather = secrets.API
data = urequests.get(url_weather)
raw=data.json()
print("raw data:\n",raw)    
data.close()

temp = raw["main"]["temp"]
humidity = raw["main"]["humidity"]
desc = raw["weather"][0]["description"]

print("Temp:", temp)
print("Humidity:", humidity)
print("Desc:", desc)