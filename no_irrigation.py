'''
stop irrigation

'''
import pifacedigitalio
import time 
pfd = pifacedigitalio.PiFaceDigital() 

pfd.relays[1].value = 0 # pump off