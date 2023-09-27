import BlynkLib
import network

BLYNK_AUTH = 'TaRC7gFhnUOew9xF7cYaKaiX2TIaapOm'


wifi = network.WLAN(network.STA_IF)
wifi.active(True)


while not wifi.isconnected():
    pass

print('IP:', wifi.ifconfig()[0])

blynk = BlynkLib.Blynk(BLYNK_AUTH)

@blynk.on("connected")
def blynk_connected(ping):
    print("Connecting.............")
    print('Blynk ready. Ping:', ping, 'ms')
    print("Connected!")

while True:
    blynk.run()