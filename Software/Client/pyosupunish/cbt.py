from pymata4 import pymata4
from time import sleep
from threading import Thread
import config, logging
from time import perf_counter

class cbt:
    logger = logging.getLogger('cbt')
    mcu = None
    debounce_timer = 0
    def blinkPCLED(self):
        while(True):
            self.logger.debug("LEDLoop")
            self.mcu.digital_pin_write(pin=config.LED_PIN,value=1)
            sleep(0.5)
            self.mcu.digital_pin_write(pin=config.LED_PIN,value=0)
            sleep(0.5)
    def activateInternal(self):
        self.logger.warn("your balls are crushed")
        self.debounce_timer = perf_counter()+config.SUSTAIN_TIME+config.EXTEND_TIME
        self.extend()
        sleep(config.SUSTAIN_TIME)
        self.retract()
    def __init__(self):
        self.mcu = pymata4.Pymata4()
        self.mcu.set_pin_mode_digital_output(pin_number=config.FRONT_VALVE_PIN)
        self.mcu.set_pin_mode_digital_output(pin_number=config.REAR_VALVE_PIN)
        self.mcu.set_pin_mode_digital_output(pin_number=config.LED_PIN)
        LEDThread = Thread(target=self.blinkPCLED)
        LEDThread.start()
        self.mcu.set_pin_mode_digital_input_pullup(pin_number=config.RETRACT_BUTTON_PIN,callback=self.handle_retract_button)
        self.mcu.set_pin_mode_digital_input_pullup(pin_number=config.EXTEND_BUTTON_PIN,callback=self.handle_extend_button)
        self.mcu.set_pin_mode_digital_input_pullup(pin_number=config.TEST_BUTTON_PIN,callback=self.handle_test_button)
        self.logger.setLevel(config.CBT_LOGGING_LEVEL)
        self.retract()
    def handle_retract_button(self, data):
        
        if (perf_counter()-self.debounce_timer >= config.DEBOUNCE_TIME) and data[2] == 0: #data at index 2 is the pin value.
            self.logger.info("RetractButtonPressed")
            self.retract()
            self.debounce_timer = perf_counter()
    def handle_extend_button(self, data):
        
        if (perf_counter()-self.debounce_timer >= config.DEBOUNCE_TIME) and data[2] == 0: #data at index 2 is the pin value.
            self.logger.info("ExtendButtonPressed")
            self.extend()
            self.debounce_timer = perf_counter()
    def handle_test_button(self, data):
        
        if (perf_counter()-self.debounce_timer >= config.DEBOUNCE_TIME) and data[2] == 0: #data at index 2 is the pin value.
            self.logger.info("TestButtonPressed")
            self.activate()
            self.debounce_timer = perf_counter()
    def extend(self):
        self.logger.debug("Extending")
        mcu=self.mcu
        mcu.digital_write(config.FRONT_VALVE_PIN,0) # Drain Front Chamber
        mcu.digital_write(config.REAR_VALVE_PIN,1) # Pressureize Rear Chamber
        sleep(config.EXTEND_TIME)
        mcu.digital_write(config.REAR_VALVE_PIN,0) # Drain Rear Chamber 
    def retract(self):
        mcu=self.mcu
        self.logger.debug("Retracting")
        mcu.digital_write(config.REAR_VALVE_PIN,0) # Drain Rear Chamber
        mcu.digital_write(config.FRONT_VALVE_PIN,1) # Pressureize Front Chamber
        
    def activate(self):
        self.logger.debug("Activating cbt routine.")
        routineThread = Thread(target=self.activateInternal)
        routineThread.start()

        