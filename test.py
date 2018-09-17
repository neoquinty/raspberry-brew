## schema connessioni
## alimentazione 3.3v --> 1 (primo in verticale, colonna sx)
## ground --> 39 (ultimo in verticale, colonna sx)
## PIN temperatura --> 7 (quarto in verticale, colonna sx) --> GPIO4
## PIN relay resis --> 40 (ultimo in verticale, colonna dx) --> GPIO21
import thread
import Brew
import Timer


app=Brew.Brew("recipe.txt",1,1,1)
app.read_recipe()
print "Recipe:"
print "\tMASH TIME: "+str(app.mash_time)+" min"
print "\tMASH TEMP: "+str(app.mash_temp)+" C"
print "\tBOIL TIME: "+str(app.boil_time)+" min"
print "\tBOIL TEMP: "+str(app.boil_temp)+" C"
print "\tHOP AMARO: "+str(app.hop_bitter_time)+" min"
print "\tHOP AROMA: "+str(app.hop_taste_time)+" min"
print "\tHOP  PROF: "+str(int(app.hop_flav_time))+" min"

try:
	thread.start_new_thread( app.show, ())
	## if timers==0 -> no acustic warnigs for hop (i.e. for mashing process)
	## if timers!=0 -> acustic warning for hops (bitter,taste,flav) i.e. for boiling process
	#timers=0
	## MASH
	## increase to mash temperature
	app.probe_T.increase_to(app.mash_temp,app.heat)
	## keep mash target for tot minutes
	app.warning.play("/root/project_brew/audio/insertgrain.wav")
	app.probe_T.keep_constant(app.mash_temp,app.mash_time,app.heat,timers,app.warning)	
	app.warning.play("/root/project_brew/audio/removegrain.wav")
	## BOIL
	## increase to boil temperature
	app.probe_T.increase_to(app.boil_temp,app.heat)
	## avviso acustico startboil
	app.warning.play("/root/project_brew/audio/startboil.wav")
	## setting timers for hop, cooling element and brew end
	timer_bitter=Timer.Timer((int(app.boil_time)-int(app.hop_bitter_time))*60,"/root/project_brew/audio/hopbitter.wav")
	timer_taste=Timer.Timer((int(app.boil_time)-int(app.hop_taste_time))*60,"/root/project_brew/audio/hoptaste.wav")
	timer_aroma=Timer.Timer((int(app.boil_time)-int(app.hop_flav_time))*60,"/root/project_brew/audio/hoptaste.wav")
	timer_cool_insert=Timer.Timer((int(app.boil_time)-15)*60,"/root/project_brew/audio/insert_serp.wav")
	timer_end=Timer.Timer(int(app.boil_time)*60,"/root/project_brew/audio/brew_end.wav")
	#start the timer as thread each
	timer_bitter.start()
	timer_taste.start()
	timer_aroma.start()
	timer_cool_insert.start()
	timer_end.start()

	#keep temperature costant during boiling
	app.probe_T.keep_constant(app.boil_temp,app.boil_time,app.heat,timers,app.warning)

	#saving data structure for analisys before exit
	app.save()
	app.end=1	
	app.heat.off()
	app.heat.reset()
except Exception as e:
	print "Error..."
	print "Saving data..."
	app.save()
	app.end=1	
	print "Exiting..."
	print ""

	app.heat.off()
	app.heat.reset()
