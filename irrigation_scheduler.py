# Irrigation Scheduler

import sched, time
s = sched.scheduler(time.time, time.sleep)
def print_time(): print "From print_time", time.time()
def pump_on(): pfd.relays[1].value = 1 # pump on
def pump_off(): pfd.relays[1].value = 0 # pump off

def print_some_times():
     print time.time()
     s.enter(5, 1, print_time, ())
     s.enter(10, 1, print_time, ())
     s.run()
     print time.time()

print_some_times()



