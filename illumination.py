'''
Illumination
'''
import pifacedigitalio
import time 
pfd = pifacedigitalio.PiFaceDigital() 

pfd.relays[0].value = 1 # lights on