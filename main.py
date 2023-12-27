# time-dependant-voltages
# 8 bit DAC range 0-255 output 0-3.3V

import machine
from time import sleep_us

#define Analogue 25
dac0 = machine.DAC(machine.Pin(25))

while (True) :
    for DACValue_0 in range (255):
        print(DACValue_0)
        dac0.write(DACValue_0)
        sleep_us(1)