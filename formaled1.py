from machine import Pin as pin
from utime import sleep, sleep_ms

led1 =pin(2,pin.OUT)
led2 =pin(4,pin.OUT)
led3 =pin(16,pin.OUT)
led4 =pin(17,pin.OUT)
led5 =pin(5,pin.OUT)
led6 =pin(18,pin.OUT)
led7 =pin(19,pin.OUT)
led8 =pin(21,pin.OUT)
led9 =pin(3,pin.OUT)
pausa=0.05

while True:
    led1.value(1)
    sleep(pausa)
    led1.value(0)
    sleep(pausa)
    led2.value(1)
    sleep(pausa)
    led2.value(0)
    sleep(pausa)
    led3.value(1)
    sleep(pausa)
    led3.value(0)
    sleep(pausa)
    led4.value(1)
    sleep(pausa)
    led4.value(0)
    sleep(pausa)
    led5.value(1)
    sleep(pausa)
    led5.value(0)
    sleep(pausa)
    led6.value(1)
    sleep(pausa)
    led6.value(0)
    sleep(pausa)
    led7.value(1)
    sleep(pausa)
    led7.value(0)
    sleep(pausa)
    led8.value(1)
    sleep(pausa)
    led8.value(0)
    sleep(pausa)
    led9.value(1)
    sleep(pausa)
    led9.value(0)
    sleep(pausa)
   