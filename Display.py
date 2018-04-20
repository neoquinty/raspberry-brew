# (0,0)  line1		S:	<Step>			fase of homebrew 
# (0,8)  line2		T:	<temp>/<temp>		current / target temperature
# (0,16) line3	   	H:	<ON or OFF>		heating element on or off
# (0,24) line4		t:	<elapsed>/<estimated>	time elapsed/estimated
# (0,32) line5		tot:	<total elapsed time>	total elasped time

import time

class Display:
	disp=0
	line=0	##il display da 128 gestisce 7 linee
	font=0
	draw=0

	def __init__(self):
		# Raspberry Pi pin configuration:
		RST = None     # on the PiOLED this pin isnt used
		DC = 23
		SPI_PORT = 0
		SPI_DEVICE = 0
		# Initialize library.
		try:
			self.disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)
			self.disp.begin()
			self.font = ImageFont.load_default()
			# Clear display.
			self.clear()
		except:
			print "Display __init__: Display not initialized.."
			print ""
	
	def write(self,text,x=0,y=0,w=None,h=None):
		if w==None:
			w=self.disp.width
		if h==None:
			h=self.disp.height		
		image = Image.new('1', (w, h))
		draw = ImageDraw.Draw(image)
		draw.rectangle((x,y,w,h), outline=0, fill=0)
		draw.text((x, y), text,  font=self.font, fill=255)
		self.disp.image(image)
    		self.disp.display()

	def fill(self,line_one,line_two,line_three,line_four,line_five):
		image = Image.new('1', (self.disp.width, self.disp.height))
		draw = ImageDraw.Draw(image)
		draw.rectangle((0,0,self.disp.width,self.disp.height), outline=0, fill=0)
		draw.text((0, 0),  line_one,   font=self.font, fill=255)
		draw.text((0, 8),  line_two,   font=self.font, fill=255)
		draw.text((0, 16), line_three, font=self.font, fill=255)
		draw.text((0, 24), line_four,  font=self.font, fill=255)
		draw.text((0, 32), line_five,  font=self.font, fill=255)
		self.disp.image(image)
    		self.disp.display()
		
	def clear(self):
		self.disp.clear()
		self.disp.display()
	
