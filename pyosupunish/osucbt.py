from distutils.log import debug
import logging
from time import sleep
from osuapi import osuapi
from cbt import cbt

logger = logging.getLogger('osucbt')
logger.setLevel(logging.DEBUG)

logger.info("connected")


TRIGGER_VALUE = 10  # How many accumulated misses until activation
DECAY_INTERVAL = 5  # How many seconds pass until the value drop by 1
SLEEP_INTERVAL = 0.5
charge = 0
oldmiss = 0
run = 0

device = cbt()

while True:
    run+=1
    if charge>0 and run%(DECAY_INTERVAL/SLEEP_INTERVAL) == 0:
        charge -= 1
    miss = osuapi().miss
    if miss == 0:
        charge = 0
        oldmiss = 0
    deltamiss = miss-oldmiss
    charge += deltamiss
    if(charge>=TRIGGER_VALUE):
        charge = 0
        device.activate()
    print("charge: "+str(charge))
    sleep(SLEEP_INTERVAL)
    oldmiss = miss
