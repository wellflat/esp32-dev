import time
from machine import Pin, PWM
import sensor
import wifi
import ambient


led = PWM(Pin(13, Pin.OUT))
led.freq(100)

def fire_led():
    for i in range(1024):
        #led.on()
        led.duty(i)
        time.sleep_ms(10)
        #led.off()
    for i in range(1023, -1, -1):
        led.duty(i)
        time.sleep_ms(10)

sta_if = wifi.connect_wifi(WIFI_SSID, WIFI_PASS)
am = ambient.Ambient(channelId=CHANNEL_ID, writeKey=WRITE_KEY)

scl, sda = Pin(22), Pin(21)
i2c = sensor.connect_i2c(scl, sda)

SEND_AMBIENT = False
def observe_temp():
    while True:
        try:
            #led.on()
            temp, pres, alti = sensor.read_bmp180(i2c)
            if SEND_AMBIENT:
                r = am.send({'d1': temp}, timeout=10)
                print(f'status: {r.status_code}')
                r.close()
            print(f'temp: {temp}')
            #led.off()
            time.sleep(60)
        except OSError as e:
            print(f'error: {str(e)}, {type(e)}')
            time.sleep(5)
            continue


