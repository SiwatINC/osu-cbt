from distutils.log import debug
import logging
from mimetypes import init
import config
import subprocess
import multiprocessing
import os
from multiprocessing.spawn import freeze_support
from time import sleep
from osuapi import osuapi
from cbt import cbt
from tkinter import *


def spawnForegroundProc(path: str):
    print("Spawning "+path)
    subprocess.Popen(path, close_fds=True)

def initializeDevice():
    global charge, oldmiss, run, charges, label_text, root, device, logger
    logger.info("osu!cbt client software by Siwat Sirichai")
    logger.info("Attempting to connect to the device")
    
    device = cbt()
    logger.info("Device Detected and connected!")
    if config.MANAGE_SYNC_INSTANCE:
        label_text.set("Trying to connect to osu! . . .")    
        root.after(500,initializeSync)
    else:
        root.after(1000, loop)
def initializeSync():
    global logger
    logger.info("This script is set to manage Sync.exe Instance.")
    logger.info("Attempting to start Sync.exe")
    curdir = os.path.dirname(__file__)
    multiprocessing.Process(target=spawnForegroundProc, args=(
        os.path.join(curdir, "dataserver/Sync.exe"),)).start()
    while True:
        try:
            miss = osuapi().miss
            break
        except:
            logger.info("API is still not alive.")
    logger.info("Attempting to Poll osu! API")
    logger.info("API is available, Continuing to Poll.")
    root.after(1000, loop)

def loop():
    global charge, oldmiss, run, charges, label_text, root, logger
    logger.debug("Polling API...")
    label_text.set("Ready")    
    run += 1
    if charge > 0 and run % (config.DECAY_INTERVAL/config.SLEEP_INTERVAL) == 0:
        charge -= 1
    miss = osuapi().miss
    if miss == 0:
        charge = 0
        oldmiss = 0
    deltamiss = miss-oldmiss
    charge += deltamiss
    if(charge >= config.TRIGGER_VALUE):
        charge = 0
        device.activate()
        label_text.set("Activating device!")
    charges.set(charge)
    logger.info("Charge: "+str(charge)+"/"+str(config.TRIGGER_VALUE))
    sleep(config.SLEEP_INTERVAL)
    oldmiss = miss
    root.after(int(config.SLEEP_INTERVAL*1000), loop)

if __name__ == '__main__':
    freeze_support()
    
    global charge, oldmiss, run, slider, charges, label_text, device, logger

    logging.basicConfig()
    logger = logging.getLogger('osucbt')
    logger.setLevel(config.OSU_CBT_LOGGING_LEVEL)

    charge = 0
    oldmiss = 0
    run = 0

    root = Tk()
    charges = IntVar()
    label_text = StringVar()
    root.geometry("300x100")
    frame = Frame(root)
    frame.pack()

    label_text.set("Initializing . . .")
    label = Label(frame, textvariable=label_text)
    label = label
    label.pack()

    slider = Scale(frame, from_=0, to=10, orient=HORIZONTAL,
                   label="Charges", variable=charges)
    slider.pack(padx=5, pady=5)

    root.title("osu!cbt client by Siwat Sirichai")
    label_text.set("Trying to connect to device . . .")
    root.after(500,initializeDevice)
    
    root.mainloop()

