'''
stop Illumination
'''

import pifacedigitalio
import time 
pfd = pifacedigitalio.PiFaceDigital() 

pfd.relays[0].value = 0 # lights off