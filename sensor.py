import ubinascii
from machine import Pin, I2C
from bmp180 import BMP180


def connect_i2c(scl: Pin, sda: Pin) -> I2C:
    i2c = I2C(0, scl=scl, sda=sda, freq=100000)
    addr = i2c.scan()
    print(f"address: {str(addr)}")
    return i2c

def read_bmp180(i2c: I2C) -> tuple:
    bmp180 = BMP180(i2c)
    bmp180.oversample_setting = 3
    bmp180.baseline = 101325.0
    chip_id = ubinascii.hexlify(bmp180.chip_id)
    #print(chip_id)
    temperature = bmp180.temperature
    pressure = bmp180.pressure
    altitude = bmp180.altitude
    return (temperature, pressure, altitude)
