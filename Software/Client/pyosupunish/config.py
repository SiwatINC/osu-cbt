import logging

# script configuration
ENABLE_GUI = True
OSU_CBT_LOGGING_LEVEL = logging.WARNING
CBT_LOGGING_LEVEL = logging.INFO
OSU_API_LOGGING_LEVEL = logging.INFO

# osu! sync client configurations
API_URL = "http://localhost:10800" #IP address and Port combination to access RestAPI
MANAGE_SYNC_INSTANCE = True #Should this script manage the Sync.exe Process?
SLEEP_INTERVAL = 0.05 # Delay between misses checks.

# rules configurations
TRIGGER_VALUE = 10  # How many accumulated charges until activation
DECAY_INTERVAL = 5  # How many seconds pass until charges drop by 1

# device configurations
SUSTAIN_TIME = 0.4 #Extension Duration
FRONT_VALVE_PIN = 50 #Arduino Pin for Front Valve
REAR_VALVE_PIN = 51 #Arduino Pin for Rear Valve
RETRACT_BUTTON_PIN = 49
EXTEND_BUTTON_PIN = 48
TEST_BUTTON_PIN = 47
LED_PIN = 46
DEBOUNCE_TIME = 0.1