import thread
import Sound
import time
import math

class Timer:
	seconds=0
	sound_path=""
	exit=0
	def __init__(self, seconds, sound_path):	
		self.seconds=seconds
		self.sound_path=sound_path

	def start(self):
		thread.start_new_thread( self.action, ())

	def action(self):
		time.sleep(self.seconds)
		self.end()				
	
	def end(self):
		Sound.Sound().play(self.sound_path)			
		self.exit=1

if __name__== "__main__" :
	## imposto 2 timers
	t1=Timer( 2*60, "/root/project_brew/audio/hopbitter.wav")
	t2=Timer( 3*60, "/root/project_brew/audio/hopbitter.wav")
	
	cur_time=time.time()
	t1.start()
	t2.start()
	while 1:
		time.sleep(10)
		elapsed=time.time()-cur_time
		print "Elapsed time in sec: "+str(math.floor(elapsed))	
	
	
	
	
 
