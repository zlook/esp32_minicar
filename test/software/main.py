from machine import Pin
from time import sleep_ms

p25 = Pin(25, Pin.OUT)
p26 = Pin(26, Pin.OUT)
p27 = Pin(27, Pin.OUT)
p14 = Pin(14, Pin.OUT)


for _ in range(3):
    p25.value(1)
    p26.value(1)
    p27.value(0)
    p14.value(0)

    sleep_ms(1000)

    p25.value(0)
    p26.value(0)
    p27.value(0)
    p14.value(0)
    sleep_ms(1000)

    p25.value(0)
    p26.value(0)
    p27.value(1)
    p14.value(1)

    sleep_ms(1000)
    p25.value(0)
    p26.value(0)
    p27.value(0)
    p14.value(0)
    sleep_ms(1000)