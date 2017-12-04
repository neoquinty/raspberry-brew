import sys
import datetime

import temperature.temperature as temperature
import display.display as display

num_data=0
cur_t=0;
avg_t=0;
max_t=0;
sum_t=0;


try:
	print( "%10s %6s %7s %7s %7s" % ("Clock","Number","Cur","Avg","Max" ))
	while True:
		cur_t=temperature.read_temp()	
		num_data=num_data+1
		sum_t=sum_t+cur_t
		avg_t=sum_t/num_data
		max_t=max(max_t,cur_t)
			
		print( "[%10s] %6d %7.2f %7.2f %7.2f" % (datetime.datetime.now().strftime('%H:%M:%S'),num_data,cur_t,avg_t,max_t ))
		time.sleep(1)
	
except KeyboardInterrupt:
	print( "EXIT\n" )


