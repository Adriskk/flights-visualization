import requests
import configparser
import functions as func
from opensky_api import OpenSkyApi
import extract
import folium

config = configparser.ConfigParser()
config.read(func.CONFIG_FILE)

DEBUG = int(config['API']['debug'])
DEBUG = True if int(DEBUG) == 1 else False

USERNAME = config['API']['username']
PASSWORD = config['API']['password']

# => OPEN SKY API
OS_API = OpenSkyApi(USERNAME, PASSWORD)


def get_air_crafts_pos():
    try:
        return OS_API.get_states(bbox=(25.0001, 49.1000, -130.0000, -60.0000))

    except requests.exceptions.ReadTimeout:
        pass


def create_markers(MAP):

    AIR_CRAFTS = []

    for pack in extract.get_from_opensky(get_air_crafts_pos()):
        AIR_CRAFTS.append(pack)

    for scatter in AIR_CRAFTS:

        # => UNPACK
        lon, lat, vel, heading = scatter

        folium.Marker(location=[int(lat), int(lon)], popup=f'plane').add_to(MAP)

    return MAP
