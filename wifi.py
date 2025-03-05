import network
import ubinascii


def connect_wifi(ssid: str, password: str):
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to wi-fi ...')
        sta_if.active(True)
        sta_if.connect(ssid, password)
        while not sta_if.isconnected():
            pass
    print(f'network: {sta_if.ifconfig()}')
    mac = ubinascii.hexlify(sta_if.config('mac'))
    print(f'mac: {mac}')
    return sta_if

def create_ap(essid: str, password: str):
    ap_if = network.WLAN(network.AP_IF)
    ap_if.config(essid=essid, password=password)
    ap_if.active(True)
    return ap_if
