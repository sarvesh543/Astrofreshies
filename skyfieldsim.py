from skyfield.api import EarthSatellite, load, wgs84
from vpython.vpython import print_to_string
import getData
import numpy as np
from vpython import *

def inf_loop():
    ts = load.timescale()
    line1 ,line2,name = getData.get_sat_data()
    satellite = EarthSatellite(line1, line2, name, ts)

    R =  6.563e+6 
    scale = 3.3270e+4

    cns = canvas(width = 1300,height = 700,background= color.black)
    newCns =canvas(width = 500,height = 500,background= color.white)
    sphere(canvas=cns,pos=vector(0,0,0),radius=R/scale,texture=textures.earth)
    textOption = ''

    box = 0
    index = 0
    simstarttime = ts.now()
    tnow = simstarttime
    passedOnce = False
    while True:
        t= ts.now()
        #print(t,tnow)
        if t - tnow > 0.00005:
            
            tnow = t
            geocentric = satellite.at(t)
            current_coord = np.array(geocentric.position.km)*1000
            temp = current_coord/scale
            lat, lon = wgs84.latlon_of(geocentric)
            if passedOnce:
                box.visible = False
                textOption.visible = False
            box = sphere(canvas=cns,pos=vector(temp[0],temp[1],temp[2]),radius=10,color=color.white)            
            
            textOption = text(canvas=newCns,text=f'Latitude: {lat}   Longitude: {lon}',pos=vector(0,0,0), depth=0,align='center',color=color.black)
            passedOnce = True

            
        if t - simstarttime > 24*60*60:
            break

while True:
    inf_loop()

