'''
Irrigation
'''
import pifacedigitalio
import time 
pfd = pifacedigitalio.PiFaceDigital() 

pfd.relays[1].value = 1 # pump on