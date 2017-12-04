## sudo modprobe w1-gpio 
## sudo modprobe w1-therm 
## cd /sys/bus/w1/devices
## ls
## cd 28-xxxx (change this to match what serial number pops up)
## cat w1_slave

import os
import glob
import time

class Temperature:
	base_dir='/sys/bus/w1/devices/'
	device_folder=glob.glob(base_dir + '28*')[0]
	device_file=device_folder + '/w1_slave'
	device_folder=0
	device_file=0

	time_start=0
	time_end=0

	temp_c=0
	max_t=0
	avg_t=0
	sum_t=0

	measures=0
	
	def __init__(self):
		os.system('modprobe w1-gpio')
		os.system('modprobe w1-therm')

	def read_temp_raw():
		f = open(self.device_file,'r')
		lines = f.readlines()
		f.close()
		return lines

	def get_temp():
		self.time_start=time()
		lines = read_temp_raw()
		while lines[0].strip()[-3:] != 'YES':
			time.sleep(0.2)
			lines = read_temp_raw()
		equals_pos = lines[1].find('t=')
		if equals_pos != -1:
			temp_string = lines[1][equals_pos+2:]
			self.temp_c = float(temp_string)/1000
			self.measures=self.measures+1
			return self.temp_c

	def stats():
		self.time_end=time()
		self.sum_t=self.sum_t+self.temp_c
		self.avg_t=self.sum_t/self.measures
		self.max_t=max(self.max_t,self.cur_t)
		t_sec=self.time_end-self.time_start
		return (t_sec, temp_c, avg_t, max_t)

