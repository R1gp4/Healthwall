#setup
import pifacedigitalio
import time
pfd = pifacedigitalio.PiFaceDigital()


#main
<<<<<<< HEAD
# def irrigation(sleepTime):
''' Irrigation script '''
try:
    pfd.relays[0].value = 1 # lights on
    pfd.relays[1].value = 1 # pump on
    print("irrigating for " + str(sleepTime) + " seconds... press ctrl+c to interrupt")
    time.sleep(sleepTime) # keep this setting for () seconds
    pfd.relays[1].value = 0 # pump off

except (KeyboardInterrupt, SystemExit):
    pfd.relays[1].value = 0 # if something goes wrong, turn off the pump
    print("Interrupted by user")

# irrigation(200)
=======
def irrigation(sleepTime):
    ''' Irrigation script '''
    try:
        pfd.relays[0].value = 1 # lights on
        pfd.relays[1].value = 1 # pump on
        print("irrigating for " + str(sleepTime) + " seconds... press ctrl+c to interrupt")
        time.sleep(sleepTime) # keep this setting for () seconds
        pfd.relays[1].value = 0 # pump off

    except (KeyboardInterrupt, SystemExit):
        pfd.relays[1].value = 0 #if something goes wrong, turn off the pump
        print("Interrupted by user")

irrigation(200)
>>>>>>> fc5ab115b9d21afd0ec94adb5b65f867d72c0274
