import pickle
import sys
import matplotlib.pyplot as plt

print(sys.argv)

time="null"
heat="null"
temp="null"

for filename in sys.argv:
	if filename.find(".py") == -1:
		with open(filename,'rb') as handle:
			if filename.find("time") != -1:
				time=pickle.load(handle)
			if filename.find("temp") != -1:
				temp=pickle.load(handle)
			if filename.find("heat") != -1:
				heat=pickle.load(handle)

print time
print temp
print heat		

plt.plot(time,temp,'b')
plt.plot(time,heat,'r')
plt.show()

