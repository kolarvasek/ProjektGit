import urequests
import network
import time
from machine import I2C, Pin
from lcd import Lcd_i2c
import my_secrets as secrets

# Interval aktualizace počasí v sekundách
WEATHER_INTERVAL = 600  # 10 minut

# Inicializace LCD
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)
lcd = Lcd_i2c(i2c, 16, 2)

def lcd_print(line1="", line2=""):
    lcd.clear()
    lcd.set_cursor(0,0)
    lcd.write(line1[:16])
    lcd.set_cursor(0,1)
    lcd.write(line2[:16])

# Připojení k WiFi (jednoduše)
ssid = 'SPS-PROSEK HOST'
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
lcd_print("Connecting to", ssid[:16])
wlan.connect(ssid)

# čekání na připojení (max 15 sekund)
timeout = 15
while not wlan.isconnected() and timeout > 0:
    lcd_print("Connecting...", "Timeout: {}".format(timeout))
    print("Connecting... Timeout:", timeout)
    time.sleep(1)
    timeout -= 1

if wlan.isconnected():
    lcd_print("WiFi Connected", "")
    print("WiFi Connected", wlan.ifconfig())
    time.sleep(2)
else:
    lcd_print("WiFi Failed", "")
    print("WiFi Failed")
    time.sleep(2)

# Načtení lokace přes IP
lat, lon = None, None
try:
    r = urequests.get("http://ip-api.com/json/")
    data = r.json()
    r.close()
    if data.get("status") == "success":
        lat = data.get("lat")
        lon = data.get("lon")
except:
    pass

if lat is None or lon is None:
    lcd_print("Location Error", "")
    lat, lon = 50.0, 14.0  # fallback Praha
    time.sleep(2)

# krátké zobrazení souřadnic
lcd_print("Lat:{:.2f}".format(lat), "Lon:{:.2f}".format(lon))
time.sleep(3)

api_key = secrets.api_key
last_update = 0  # okamžitá aktualizace

while True:
    if time.time() - last_update > WEATHER_INTERVAL:
        # načtení počasí
        temp, humidity, desc = None, None, None
        try:
            url = "https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid={api_key}&units=metric".format(api_key=api_key)
            r = urequests.get(url)
            data = r.json()
            print(r.json())
            r.close()
            if "main" in data and "weather" in data:
                temp = data["main"]["temp"]
                humidity = data["main"]["humidity"]
                desc = data["weather"][0]["description"]
        except:
            pass

        if temp is not None and desc is not None:
            lcd_print("T:{:.1f}C H:{}%".format(temp, humidity), str(desc)[:16])
        else:
            lcd_print("API Error", "")

        last_update = time.time()

    time.sleep(1)