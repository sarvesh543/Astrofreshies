from vpython import *
import time

G = 6.674e-11
M = 5.97219e+24
R =  6.563e+6 

scale = 3.3270e+4

def updateDisplay(dict,cns):
    curr_time = int(time.time())
    if curr_time in dict.keys():
        sphere(canvas=cns,pos=dict[curr_time].pos,radius =1)
        
    sphere(canvas=cns,pos=vector(0,0,0),radius=R/scale,texture=textures.earth)
    return 0