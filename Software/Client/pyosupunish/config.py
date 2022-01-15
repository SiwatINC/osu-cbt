# osu! sync client configurations
API_URL = "http://localhost:10800" #IP address and Port combination to access RestAPI
MANAGE_SYNC_INSTANCE = True #Should this script manage the Sync.exe Process?
SLEEP_INTERVAL = 0.5 # Delay between misses checks.

# rules configurations
TRIGGER_VALUE = 10  # How many accumulated charges until activation
DECAY_INTERVAL = 5  # How many seconds pass until charges drop by 1

# device configurations
PRESSUREIZE_TIME = 1.5 #Inlet Valve Duration
SUSTAIN_TIME = 1 #Retain Pressure Duration
INLET_VALVE_PIN = 50 #Arduino Pin for Inlet Valve