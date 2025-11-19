from machine import Pin, ADC, deepsleep
import time

# Soil moisture sensor on ADC0 (GPIO26)
soil_adc = ADC(Pin(26))

# Potentiometer threshold on ADC1 (GPIO27)
pot_adc = ADC(Pin(27))

# LED on GPIO15
led = Pin(15, Pin.OUT)

while True:
    # Read soil sensor voltage
    soil = soil_adc.read_u16()

    # Read potentiometer voltage (threshold)
    pot = pot_adc.read_u16()

    # Compare and control LED
    if soil <= pot:
        led.value(1)  # LED ON
    else:
        led.value(0)  # LED OFF

    print("Soil:", soil, "V  Threshold:", pot, "V")
    # Sleep for 5 minutes (300,000 ms)
    #deepsleep(300000)
    time.sleep(1)
