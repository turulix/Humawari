#!/usr/bin/python
import os
import random
import sys
import threading
import time
import urllib.request
from datetime import datetime

import win32api
import win32con
import win32process
from selenium import webdriver

import PicCombiner


# rammb-slider.cira.colostate.edu/?sat=goes-16&sec=full_disk&x=10848&y=10848&z=0&im=1&map=0

def downloader(image_url, Name):
    try:
        time.sleep(random.randrange(0, 20, 1))
        urllib.request.urlretrieve(image_url, "./TempTileImg/" + Name)
    except:
        print("Cant update")


while True:
    pid = win32api.GetCurrentProcessId()
    handle = win32api.OpenProcess(win32con.PROCESS_ALL_ACCESS, True, pid)
    win32process.SetPriorityClass(handle, win32process.BELOW_NORMAL_PRIORITY_CLASS)

    log = open("./Log.txt", "a")
    threads = []
    options = webdriver.ChromeOptions()
    options.binary_location = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
    options.add_argument('headless')
    options.add_argument('verbose')

    driver = webdriver.Chrome(chrome_options=options)
    driver.set_window_position(-10000, 0)
    driver.get('http://rammb-slider.cira.colostate.edu/?sat=goes-16&sec=full_disk&x=10848&y=10848&z=0&im=1&map=0')
    TimeStamp = driver.find_element_by_id(id_='imageryTime')

    print(TimeStamp.text)
    TimeStampCode = TimeStamp.text.replace(":", "").replace("-", "").replace(" ", "").replace("UTC", "")
    TimeText = TimeStamp.text
    driver.quit()
    print(TimeStampCode)
    print("Cut Time: " + TimeStampCode[:8])

    for x in range(16):
        for y in range(16):
            RX = "{:03d}".format(x)
            RY = "{:03d}".format(y)
            IDTHING = RX + "_" + RY + ".png"
            # print("ID: " + str(IDTHING) + " TIME: " + str(TimeStamp))

            # Natural Color
            # downloader("http://rammb-slider.cira.colostate.edu/data/imagery/" + TimeStampCode[:8] + "/himawari---full_disk/natural_color/" + str(TimeStampCode) + "/04/" + IDTHING, IDTHING)

            # GeoColor
            # downloader("http://rammb-slider.cira.colostate.edu/data/imagery/" + TimeStampCode[:8] + "/himawari---full_disk/geocolor/" + str(TimeStampCode) + "/04/" + IDTHING, IDTHING)

            # Goes-16 GeoColor
            t = threading.Thread(target=downloader, args=("http://rammb-slider.cira.colostate.edu/data/imagery/" + TimeStampCode[:8] + "/goes-16---full_disk/geocolor/" + str(TimeStampCode) + "/04/" + IDTHING, IDTHING))
            threads.append(t)
            t.start()
    WaitTime = 0
    log.write("[" + str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + "] " + "Startet Waiting for " + str(TimeText) + "\n")
    log.close()
    while threading.active_count() > 1:
        print("Waiting: " + str(threading.active_count()) + " Threads to go")
        WaitTime = WaitTime + 1

        if WaitTime > 60:
            log = open("./Log.txt", "a")
            log.write("[" + str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + "] " + "Download took longer than 60sec restarting.")
            os.execv(sys.executable, ['python'] + sys.argv)

        time.sleep(1)
    log = open("./Log.txt", "a")
    log.write("[" + str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + "] " + "Waited for: " + str(WaitTime) + "Seconds\n\n")
    log.close()
    print(TimeText)
    PicCombiner.main(TimeText)

    print("Standby")
    time.sleep(10 * 60)
