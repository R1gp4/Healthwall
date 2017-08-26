
''' Irrigation '''

import pifacedigitalio
import time 
pfd = pifacedigitalio.PiFaceDigital()

pfd.relays[1].value = 1 # pump on
time.sleep(40) # keep this setting for () seconds
print("irrigating for 30 seconds...")
pfd.relays[1].value = 0 # pump off


"""
''' Nothing '''
time.sleep(3600*12)


''' Irrigation '''

pfd.relays[1].value = 1 # pump on
time.sleep(30) # keep this setting for () seconds
print("irrigating for 30 seconds...")
pfd.relays[1].value = 0 # pump off
time.sleep(30) # keep this setting for () seconds
print("waiting 30 seconds...")
pfd.relays[1].value = 1 # pump on
time.sleep(30) # keep this setting for () seconds
print("irrigating for 30 seconds...")
pfd.relays[1].value = 0 # pump off

"""