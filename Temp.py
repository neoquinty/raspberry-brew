import glob
import math
import time
import Relay
import os

class Temp:
	t=0
	target=0
	device_file=0
	start_time=0
	tot_time=0
	history_temp=[]
	history_time=[]
	history_heat=[]
		
	def __init__(self):
		print "Temp  __init__: temp initializing"
		try:
			os.system('modprobe w1-gpio')
			os.system('modprobe w1-therm')
			self.base_dir='/sys/bus/w1/devices/'
		except:
			print "ERROR: Module 'w1-gpio' or 'w1-therm' not found"
			exit()
			
		try:
			self.device_folder=glob.glob(self.base_dir + '28*')[0]
			self.device_file=self.device_folder + '/w1_slave'
		except:
			print "ERROR: Temperature probe not found!!"
			exit()
		self.start_time()	
	
	def start_time(self):
		self.start_time=time.time()
	
	def get_current_time(self):
		return time.time()-self.start_time

	def save(self,heat):
		self.history_temp.append(self.get_temp())
		self.history_time.append(self.get_current_time())
		self.history_heat.append(heat.get_status())
	
	def get_temp(self):
		return self.t
	
	def read_temp_raw(self):
		f = open(self.device_file,'r')
		lines = f.readlines()
		f.close()
		return lines

	def read_temp(self):
		lines = self.read_temp_raw()
		while lines[0].strip()[-3:] != 'YES':
			time.sleep(0.2)
			lines = read_temp_raw()
		equals_pos = lines[1].find('t=')
		if equals_pos != -1:
			temp_string = lines[1][equals_pos+2:]
			self.t = float(temp_string)/1000

	def increase_to(self,target,heat):
		self.read_temp()
		self.target=target
		start_t=self.t
		elapsed=0.1
		while float(self.t)<float(target):
			## apri resistenza
			if(heat.get_status()==0):
				heat.on()
			## cycle every 7.5sec
			time.sleep(7.5)
			elapsed+=0.125
			self.read_temp()
			##print "Temp: "+str(float(self.t))
			##print "Targ: "+str(float(target))
			self.tot_time=self.tot_time+0.125
			self.save(heat)
		## target reached
		ramp=(self.t-start_t)/elapsed
		heat.off()
		##print str(ramp)+" deg per min"
		return elapsed

	def decrease_to(self,target,heat):
		self.read_temp()
		self.target=target
		start_t=self.t
		elapsed=0.1
		while math.ceil(self.t)>target:
			## spegni resistenza
			if(heat.get_status()==1):
				heat.off()		
			##print "HEAT OFF"		
			## cycle every 30sec
			time.sleep(30)
			elapsed+=0.5
			self.tot_time=self.tot_time+0.5
			self.read_temp()
			self.save(heat)
			##print "Temperature"+str(self.t)+"/"++str(target)
		## target reached
		return elapsed

	
	def keep_constant(self,target,fortime,heat,timers,warning):
		self.read_temp()
		self.target=target
		elapsed = 0.1
		while elapsed<fortime:
			if math.ceil(self.t)<target:
				e=self.increase_to(target,heat)
				elapsed+=e	
			else:
				e=self.decrease_to(target,heat)
				elapsed+=e
			if timers != 0:
				for minute in timers:
					if minute == math.ceil(fortime-elapsed):
						if int(minute) > 35:
							## amaro
							warning.play("/root/project_brew/audio/hopbitter.wav")						
						elif int(minute) <= 10:
							## odore
							warning.play("/root/project_brew/audio/hoptaste.wav")
						else: ## >11 e < 35
							## gusto
							warning.play("/root/project_brew/audio/hoptaste.wav")
			time.sleep(15)
			elapsed+=0.25
			self.tot_time=self.tot_time+0.25
		heat.off()
		return elapsed	
		


if __name__=='__main__':
	temperature=Temp()
	heat=Relay.Relay(21)
	
	##print "Testing increasing temperature..."
	##elapsed_time = temperature.increase_to(55,heat)
	
	##print "Testing decreasing temperature..."
	##elapsed_time = temperature.decrease_to(52,heat)
	
	print "Testing constant temperature..."
	elapsed_time = temperature.keep_constant(55,5,heat,0,0)
	
	
		
	
		
