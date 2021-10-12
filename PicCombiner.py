
# Combine multiple images into one.
#
# To install the Pillow module on Mac OS X:
#
# $ xcode-select --install
# $ brew install libtiff libjpeg webp little-cms2
# $ pip install Pillow
#

from __future__ import print_function

import os
import sys
import time

import win32api
import win32con
import win32process
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFile


# 2018 03 02 025000

def main(DrawTextThing):
	pid = win32api.GetCurrentProcessId()
	handle = win32api.OpenProcess(win32con.PROCESS_ALL_ACCESS, True, pid)
	win32process.SetPriorityClass(handle, win32process.BELOW_NORMAL_PRIORITY_CLASS)


	ImageFile.LOAD_TRUNCATED_IMAGES = True
	files = []
#	DrawTextThing = ""
#	for arg in argv[1:]:
#		DrawTextThing = DrawTextThing + arg + " "
	time.sleep(5)
	print(sys.argv[1:])
	for x in range(16):
		for y in range(16):
			RX = "{:03d}".format(x)
			RY = "{:03d}".format(y)
			files.append("./TempTileImg/" + str(RX) + "_" + str(RY) + ".png")
			#print("./IMG/" + str(RX) + "_" + str(RY) + ".png")
 


	result = Image.new("RGB", (678*16, 678*16))
	print(files)
	
	for index, file in enumerate(files):
		path = os.path.expanduser(file)
		img = Image.open(path)
		img.thumbnail((678, 678), Image.ANTIALIAS)
		x = index // 16 * 678
		y = index % 16 * 678
		w, h = img.size
		print('pos {0},{1} size {2},{3}'.format(x, y, w, h))
  
		result.paste(img, (y, x))

	draw = ImageDraw.Draw(result)
	#font = ImageFont.truetype("times.ttf", 150)
	#draw.text((0,0),str(DrawTextThing),(255,255,255),font=font)

	result.save("./FullEarthImg/" + str(DrawTextThing).replace(":", "-") + ".jpg")
	
	time.sleep(1)
	FullEarth = " \FullEarthImg\ ".replace(" ", "")
	
	#image_path = os.path.abspath(os.path.dirname(__file__)) + str(FullEarth) + str(DrawTextThing).replace(":","-") + ".jpg"
	#print(str(image_path))
	#SPI_SETDESKWALLPAPER  = 0x0014
	#SPIF_UPDATEINIFILE    = 0x0001
	#SPIF_SENDWININICHANGE = 0x0002

	#user32 = ctypes.WinDLL('user32')
	#SystemParametersInfo = user32.SystemParametersInfoW
	#SystemParametersInfo.argtypes = ctypes.c_uint,ctypes.c_uint,ctypes.c_void_p,ctypes.c_uint
	#SystemParametersInfo.restype = wintypes.BOOL
	#print(SystemParametersInfo(SPI_SETDESKWALLPAPER, 0, image_path, SPIF_UPDATEINIFILE | SPIF_SENDWININICHANGE))

	#print("Screen Set")
	
if __name__ == "__main__":
	main(sys.argv[1:])
 