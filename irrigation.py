
''' Irrigation '''
#setup
import pifacedigitalio
import time
pfd = pifacedigitalio.PiFaceDigital()
sleepTime = 240

#main
try:
    pfd.relays[0].value = 1 # lights on
    pfd.relays[1].value = 1 # pump on
    print("irrigating for " + str(sleepTime) + " seconds... press ctrl+c to interrupt")
    time.sleep(sleepTime) # keep this setting for () seconds
    pfd.relays[1].value = 0 # pump off

except (KeyboardInterrupt, SystemExit):
    pfd.relays[1].value = 0 #if something goes wrong, turn off the pump
    print("Interrupted by user")
    break
