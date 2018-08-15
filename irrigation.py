
''' Irrigation '''
#setup
import pifacedigitalio
import time
pfd = pifacedigitalio.PiFaceDigital()

#main
try:
    pfd.relays[1].value = 1 # pump on
    print("irrigating for 40 seconds... press ctrl+c to interrupt")
    time.sleep(40) # keep this setting for () seconds
    pfd.relays[1].value = 0 # pump off
except (KeyboardInterrupt, SystemExit):
    pfd.relays[1].value = 0 #if something goes wrong, turn off the pump
