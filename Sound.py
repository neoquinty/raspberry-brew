import os

class Sound:
	
	def __init__(self):
		print "Sound __init__: sound initialized"
		
	def play(self,filepath):
		## using omxplayer
		command="omxplayer -o local "+filepath
		os.system(command)

if __name__=='__main__':
	warning=Sound()
	print "playing..."
	warning.play("/root/project_brew/audio/insertgrain.wav")	
	print "...done"
	print ""	
	
