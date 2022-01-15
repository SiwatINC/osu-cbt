from distutils.log import debug
import logging, config, subprocess, multiprocessing, os
from multiprocessing.spawn import freeze_support
from time import sleep
from osuapi import osuapi
from cbt import cbt

def spawnForegroundProc(path: str):
    print("Spawning "+path)
    subprocess.Popen(path,close_fds=True)
if __name__ == '__main__':
    freeze_support()
    logging.basicConfig()
    logger = logging.getLogger('osucbt')
    logger.setLevel(logging.DEBUG)
    charge = 0
    oldmiss = 0
    run = 0


    logger.info("osu!cbt client software by Siwat Sirichai")
    logger.info("Attempting to connect to the device")
    device = cbt()
    logger.info("Device Detected and connected!")

    if config.MANAGE_SYNC_INSTANCE:
        logger.info("This script is set to manage Sync.exe Instance.")
        logger.info("Attempting to start Sync.exe")
        curdir = os.path.dirname(__file__)
        multiprocessing.Process(target=spawnForegroundProc,args=(os.path.join(curdir,"dataserver/Sync.exe"),)).start()
        while True:
            try:
                miss = osuapi().miss
                break
            except:
                logger.info("API is still not alive.")

    logger.info("Attempting to Poll osu! API")
    logger.info("API is available, Continuing to Poll.")

    while True:
        logger.debug("Polling API...")
        run+=1
        if charge>0 and run%(config.DECAY_INTERVAL/config.SLEEP_INTERVAL) == 0:
            charge -= 1
        miss = osuapi().miss
        if miss == 0:
            charge = 0
            oldmiss = 0
        deltamiss = miss-oldmiss
        charge += deltamiss
        if(charge>=config.TRIGGER_VALUE):
            charge = 0
            device.activate()
        logger.info("Charge: "+str(charge)+"/"+str(config.TRIGGER_VALUE))
        sleep(config.SLEEP_INTERVAL)
        oldmiss = miss

