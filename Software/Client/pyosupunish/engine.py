import config
from time import sleep
from cbt import cbt

device = cbt()
while(True):
    device.activate()
    sleep(0.9)
