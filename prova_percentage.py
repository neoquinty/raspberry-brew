import time
import math

start_time=time.time()
total_time=20
while 1:
	elapsed=time.time()-start_time
	percentage=int(math.ceil(round(elapsed*100/total_time)))
	print "Progress: %3d [%2d/%2d]" % (percentage,int(round(elapsed)),total_time)
	if percentage>=100:
		exit()
	time.sleep(1)
	
