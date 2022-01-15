from pymata4 import pymata4
from time import sleep
from threading import Thread
import config, logging

class cbt:
    logger = logging.getLogger('cbt')
    mcu = None
    def activateInternal(self):
        self.extend()
        sleep(config.PRESSUREIZE_TIME+config.SUSTAIN_TIME)
        self.retract()
        self.logger.warn("your balls are crushed")
        
    def __init__(self):
        self.mcu = pymata4.Pymata4()
        self.mcu.set_pin_mode_digital_output(pin_number=config.INLET_VALVE_PIN)
        self.logger.setLevel(logging.INFO)
    def extend(self):
        mcu=self.mcu
        mcu.digital_write(config.INLET_VALVE_PIN,1) #Open Inlet Valve
    def retract(self):
        mcu=self.mcu
        mcu.digital_write(config.INLET_VALVE_PIN,0) #Close Inlet Valve
    def activate(self):
        routineThread = Thread(target=self.activateInternal)
        routineThread.start()