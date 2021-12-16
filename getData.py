from typing_extensions import runtime
from astropy.coordinates import CartesianRepresentation, CartesianDifferential, TEME
from astropy import units as u
from astropy.time import Time
from sgp4.api import Satrec
from sgp4.api import SGP4_ERRORS
from satellite import satellite
import numpy as np

# api
# key is not connected to burner email so no worries
import requests

def get_sat_data(current_time,sat_name):
    #api_key = "jEz5UgM4wTgvpwsAbOCX1hxBU0BO0VRkCsLPpJd9"
    api_url = "http://tle.ivanstanojevic.me/api/"
    #temporary
    sat_id = "40075"
    # to add sat name search in place of sat id
    response = requests.get(f'{api_url}tle/{sat_id}')
    response = response.json()

    line1 = response['line1']
    line2 = response['line2']
    sat = Satrec.twoline2rv(line1, line2)

    t = Time(current_time, format='jd')
    error, teme_p, teme_v = sat.sgp4(t.jd1, t.jd2)
    
    temp_teme_p = teme_p
    temp_teme_v = teme_v
    

    teme_p = CartesianRepresentation(teme_p*u.km)
    teme_v = CartesianDifferential(teme_v*u.km/u.s)
    print(temp_teme_p,temp_teme_v)
    teme = TEME(teme_p.with_differentials(teme_v), obstime=t)
    
    return satellite(response['name'], np.array(temp_teme_p), np.array(temp_teme_v))