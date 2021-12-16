import astropy.coordinates
import numpy as np
from satellite import satellite
import math

# with dt = 0.01; 24 hrs of simulation takes 44 min
# with dt = 0.001; 24 hrs of simulation takes 2.4 hrs
# we need to decide value of dt with respect to how much
# accuracy we need and how often we can update from the api

# time parameters
t = 0
#small time step
dt = 0.1

# constants
G = 6.674e-11
M = 5.97219e+24
R =  6.563e+6

#test sat setup
sat_height = (((86400/(2*math.pi)) ** 2) * G * M) ** (1/3)
v = math.sqrt(G*M/sat_height)

pos = np.array([sat_height,0,0])
test_sat = satellite('test',pos,np.array([0,v,0]))





#maybe include this in satellite class

def updateValues(sat):
    global t

    a_mag = G*M/(np.linalg.norm(sat.pos)**2)
    a = -1 * a_mag * sat.pos / np.linalg.norm(sat.pos)    
    sat.vel += a*dt
    sat.pos += sat.vel * dt    
 
    t += dt
    


# testing to see if geostationary satellite returns to initial pos and velocity after 24 hrs
print('Test Start')
index = 0

#change t to change time of simulation
while t < 86164:
    updateValues(test_sat)
    #print(index,'  ', t,'  ',test_sat.pos, '  ',test_sat.vel)
    #index += 1

print()
print('Results  ', t)
print()
print("initial height: ",sat_height ,'  ' ,"final height: ", np.linalg.norm(test_sat.pos))
print(test_sat.pos)
print()
print()
print("initial vel: ", v, '  ',"final vel: ",np.linalg.norm(test_sat.vel))
print(test_sat.vel)
print()
print('Test End')

# end of test


