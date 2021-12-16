
#import vpython could be used for graphics
import time
import numpy as np
import math
import requests
from satellite import satellite
from datetime import datetime
import getData
import display


# with dt = 0.1; 24hrs of simulation takes 5 sec
# with dt = 0.01; 24 hrs of simulation takes 44 min
# with dt = 0.001; 24 hrs of simulation takes 2.4 hrs
# we need to decide value of dt with respect to how much
# accuracy we need and how often we can update from the api

# sim time parameters
t = 0
#small time step
dt = 0.1

# constants
G = 6.674e-11
M = 5.97219e+24
R =  6.563e+6

#test sat setup


temp_time = int(time.time())

sat_name = 'placeholder'
test_sat = getData.get_sat_data(temp_time,sat_name)





#maybe include this in satellite class

def updateValues(sat):
    global t

    a_mag = G*M/(np.linalg.norm(sat.pos)**2)
    a = -1 * a_mag * sat.pos / np.linalg.norm(sat.pos)    
    sat.vel += a*dt
    sat.pos += sat.vel * dt

    # compare with data with api
  
 
    t += dt
    


# testing to see if geostationary satellite returns to initial pos and velocity after 24 hrs
print('Test Start')
index = 0
time.sleep(10)

#change t to change time of simulation
while t < 8*60*60:
    updateValues(test_sat)
    if int(time.time())- temp_time > 2*60*60*1000:
        temp_time = int(time.time())
        sat_name = 'placeholder'
        test_sat = getData.get_sat_data(temp_time,sat_name)
        temp_time = int(time.time())
    display.updateDisplay()

    

print()
print('Results  ', t)
print()
print("final height: ", np.linalg.norm(test_sat.pos))
print(test_sat.pos)
print()
print()
print("final vel: ",np.linalg.norm(test_sat.vel))
print(test_sat.vel)
print()
print('Test End')

# end of test


