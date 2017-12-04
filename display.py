import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import subprocess

class Display:
	RST = None     # on the PiOLED this pin isnt used
	DC = 23
	SPI_PORT = 0
	SPI_DEVICE = 0
	
	display=0
	image=0
	draw=0
	
	num_lines=0	

	def __init__(self):
		self.display = Adafruit_SSD1306.SSD1306_128_64(rst=RST)
		self.display.begin()
		
	def destroy():
		self.display.clear()
		self.display.display()

	def refresh():
		# write black image before writing again
		self.image=Image.new('1',(self.display.width,self.display.height))
		self.draw=ImageDraw.Draw(self.image)
		self.draw.rectangle((0,0,width,height), outline=0, fill=0)
	
	def write(str,i=10):
		top=-2
		x=0
		if self.num_lines > 6:
			refresh()	
			self.num_lines=0
		if i > 7:
			i = self.num_lines

		self.draw.text((x,top+i*8), str, font=ImageFont.load_default(),fill=255 ) 
 		# Display image.
   		self.display.image(self.image)
    		self.display.display()
		self.num_lines = self.num_lines+1
 
