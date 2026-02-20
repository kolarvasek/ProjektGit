import network
import time
import secrets  # Tvůj secrets.py s WIFI_SSID a WIFI_PASSWORD

# Aktivace WiFi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

print("Connecting to WiFi:", secrets.WIFI_SSID)

# Připojení k síti
wlan.connect(secrets.WIFI_SSID)

# Čekej až bude připojeno (max 15 sekund)
for i in range(15):
    if wlan.isconnected():
        break
    print("Waiting... {}s".format(i+1))
    time.sleep(1)

# Výsledek
if wlan.isconnected():
    print("✅ Connected!")
    print("IP address:", wlan.ifconfig()[0])
else:
    print("❌ Failed to connect WiFi")
