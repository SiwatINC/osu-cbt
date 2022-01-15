from pymata4 import pymata4
from time import sleep
from threading import Thread
class cbt:

    PRESSUREIZE_TIME = 1.5 #Inlet Valve Duration
    SUSTAIN_TIME = 1 #Retain Pressure Duration
    mcu = None
    def activateInternal(self):
        self.extend()
        sleep(self.PRESSUREIZE_TIME+self.SUSTAIN_TIME)
        self.retract()
        print("your balls are crushed")
    
    def __init__(self):
        self.mcu = pymata4.Pymata4()
        self.mcu.set_pin_mode_digital_output(pin_number=50)
    def extend(self):
        mcu=self.mcu
        mcu.digital_write(50,1) #Open Inlet Valve
    def retract(self):
        mcu=self.mcu
        mcu.digital_write(50,0) #Close Inlet Valve
    def activate(self):
        routineThread = Thread(target=self.activateInternal)
        routineThread.start()