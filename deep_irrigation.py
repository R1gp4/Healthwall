
''' Irrigation '''
#setup
import pifacedigitalio
import time
pfd = pifacedigitalio.PiFaceDigital()

#main
try:
    pfd.relays[1].value = 1 # pump on
    print("irrigating for 40 seconds... press ctrl+c to interrupt")
    time.sleep(240) # keep this setting for (240) seconds
    pfd.relays[1].value = 0 # pump off
except (KeyboardInterrupt, SystemExit):
    pfd.relays[1].value = 0 #if something goes wrong, turn off the pump
