## schema connessioni

## alimentazione 3.3v --> 1 (primo in verticale, colonna sx)
## ground --> 39 (ultimo in verticale, colonna sx)

## PIN temperatura --> 7 (quarto in verticale, colonna sx) --> GPIO4
## PIN relay resis --> 40 (ultimo in verticale, colonna dx) --> GPIO21
import Brew
import time
import thread

app=Brew.Brew("recipe.txt",1,1,1)
app.read_recipe()
print "Recipe:"
print "MASH TIME: "+str(app.mash_time)+" min"
print "MASH TEMP: "+str(app.mash_temp)+" C"
print "BOIL TIME: "+str(app.boil_time)+" min"
print "BOIL TEMP: "+str(app.boil_temp)+" C"
print "HOP AMARO: "+str(app.hop_bitter_time)+" min"
print "HOP AROMA: "+str(app.hop_taste_time)+" min"
print "HOP  PROF: "+str(int(app.hop_flav_time))+" min"

thread.start_new_thread( app.show, ())
## serve per attivare gli avvisi sonori sulle gettate del luppolo (in fase di boiling solamente)
timers=0		
## MASH
## increase to mash temperature
app.probe_T.increase_to(app.mash_temp,app.heat)
## keep mash target for tot minutes
app.warning("/root/project_brew/audio/insertgrain.wav")
app.probe_T.keep_constant(app.mash_temp,app.mash_time,app.heat,timers,app.warning)	
app.warning("/root/project_brew/audio/removegrain.wav")
## BOIL
## increase to boil temperature
app.probe_T.increase_to(app.boil_temp,app.heat)	
## keep boil target for tot minute
timers=(app.hop_bitter_time,app.hop_taste_time,app.hop_flav_time)
app.probe.T.keep_constant(app.boil_temp,app.boil_time,app.heat,timers,app.warning)

app.save()

app.end=1	

app.heat.off()
app.heat.reset()
