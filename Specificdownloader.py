#!/usr/bin/python
import urllib.request
import time
import datetime
import os
import subprocess
import PicCombiner
import threading

from pyvirtualdisplay import Display
from selenium import webdriver

#rammb-slider.cira.colostate.edu/?sat=goes-16&sec=full_disk&x=10848&y=10848&z=0&im=1&map=0

def downloader(image_url, Name):
	try:
		urllib.request.urlretrieve(image_url,"./TempTileImg/" + Name)
	except:
		print("Cant update")
		
		

threads = []
	

TimeText="2018-03-04 16:00:38 UTC"
TimeStampCode="20180304160038"

print ("Cut Time: " + TimeStampCode[:8])

	
for x in range(16):
	for y in range(16):
		RX = "{:03d}".format(x)
		RY = "{:03d}".format(y)
		IDTHING = RX + "_" + RY + ".png"
		#print("ID: " + str(IDTHING) + " TIME: " + str(TimeStamp))
		
			
		#Natural Color
		#downloader("http://rammb-slider.cira.colostate.edu/data/imagery/" + TimeStampCode[:8] + "/himawari---full_disk/natural_color/" + str(TimeStampCode) + "/04/" + IDTHING, IDTHING)
		
		#GeoColor
		#downloader("http://rammb-slider.cira.colostate.edu/data/imagery/" + TimeStampCode[:8] + "/himawari---full_disk/geocolor/" + str(TimeStampCode) + "/04/" + IDTHING, IDTHING)
			
		#Goes-16 GeoColor
		t = threading.Thread(target=downloader, args=("http://rammb-slider.cira.colostate.edu/data/imagery/" + TimeStampCode[:8] + "/goes-16---full_disk/geocolor/" + str(TimeStampCode) + "/04/" + IDTHING, IDTHING))
		threads.append(t)
		t.start()
		
print(str("Waiting 60sec for download finish"))
	
for SleepTime in range(61):
	print("Time to Wait: "+ str(60 - SleepTime))
	print(str(threads))
	time.sleep(1)
		
print(TimeText)
PicCombiner.main(TimeText)
	
print("Done")
