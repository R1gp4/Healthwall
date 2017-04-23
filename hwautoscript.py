import pifacedigitalio
import time 

pfd = pifacedigitalio.PiFaceDigital() 

while True:
    print("This prints once a minute.")
	time.sleep(60)  # Delay for 1 minute (60 seconds)
	pfd.relays[0].value = 1
	pfd.relays[1].value = 1
	time.sleep(60) 
	print("now the relays will turn off")
	pfd.relays[0].value = 0
	pfd.relays[1].value = 0


