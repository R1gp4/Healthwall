
''' Irrigation '''

import pifacedigitalio
import time 
pfd = pifacedigitalio.PiFaceDigital()

''' Lights '''
pfd.relays[0].value = 1 # lights on

''' Nothing '''
time.sleep(3600*1) # 1 hours of sleep

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



''' Nothing '''
time.sleep(3600*9.5) # hours of sleep


''' Lights '''
pfd.relays[0].value = 1 # lights on

''' Nothing '''
time.sleep(3600*2) # hours of sleep


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


''' Nothing '''
time.sleep(3600*2) # hours of sleep

pfd.relays[0].value = 0 # lights off

quit()