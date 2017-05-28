'''
Irrigation
'''
import pifacedigitalio
import time 
pfd = pifacedigitalio.PiFaceDigital() 

pfd.relays[1].value = 1 # pump on
time.sleep(30) # keep this setting for () seconds
pfd.relays[1].value = 0 # pump off