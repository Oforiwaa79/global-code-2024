from machine import Pin
import time


led=Pin(2,Pin.OUT)
btn=Pin(0,Pin.IN)

ledState=0
btnState=0



while True:
    print(btn.value())
    if btn.value()== 0: #when btn is pressed
        led.value(ledState)#turn on led based on current state
        btnState +=1 #store in memory current state
        if btnState == 2:#check in memory if there is a stored value if value is appended and is equal to two
            btnState=0 #change the data to zero
            ledState= not ledState  #toggle led on or off based on current button state
            led.value(ledState) #turn on base on state
            
        time.sleep(0.1)