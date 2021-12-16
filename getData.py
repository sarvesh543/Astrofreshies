import numpy as np

import requests
from astropy import units as u
from astropy.coordinates import (ITRS, TEME, CartesianDifferential,
                                 CartesianRepresentation)
from astropy.time import Time
from sgp4.api import Satrec
from typing_extensions import runtime

from satellite import satellite

#api
def get_sat_data():
    #api_key = "jEz5UgM4wTgvpwsAbOCX1hxBU0BO0VRkCsLPpJd9"
    api_url = "http://tle.ivanstanojevic.me/api/"
    #temporary
    sat_id = "25544"
    # to add sat name search in place of sat id
    response = requests.get(f'{api_url}tle/{sat_id}')
    response = response.json()
    print(response)
    return [response['line1'], response['line2'], response['name']]
    

    

  