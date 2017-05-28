'''
Irrigation
'''
import pifacedigitalio
import time 
pfd = pifacedigitalio.PiFaceDigital() 

pfd.relays[1].value = 1 # pump on
time.sleep(15) # keep this setting for () seconds
print("irrigating for 15 seconds...")
pfd.relays[1].value = 0 # pump off
time.sleep(30) # keep this setting for () seconds
print("waiting 30 seconds...")
pfd.relays[1].value = 1 # pump on
time.sleep(15) # keep this setting for () seconds
print("irrigating for 15 seconds...")
pfd.relays[1].value = 0 # pump off