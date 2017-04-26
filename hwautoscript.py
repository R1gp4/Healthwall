import pifacedigitalio
import time 
pfd = pifacedigitalio.PiFaceDigital() 

while True:
	print("The relays are now ON" 
	pfd.relays[0].value = 1 # lights on
	pfd.relays[1].value = 1 # pump on
	time.sleep(60) # keep this setting for one minute (60 seconds)
	
	print("now the relays will turn off")
	pfd.relays[0].value = 0 # lights off
	pfd.relays[1].value = 0 # pump off
	time.sleep(86400) # keep this setting for one minute (60 seconds)








