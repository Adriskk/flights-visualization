import pandas as pd
import configparser
from datetime import datetime
import folium


CONFIG_FILE = 'config/config.ini'

config = configparser.ConfigParser()
config.read(CONFIG_FILE)

JSON_FILE = 'json/data.json'
AIRPORTS_CSV_FILE = 'csv/list-of-airports-in-usa.csv'

MARKER_PATH = 'res/plane.png'
AIRPORTS_LIMIT = int(config['DATA']['airport_nrows'])
MAX_AIRCRAFTS = 600
SAVE_PATH = 'res/basemap.png'

LOCATION = [37.870206, -99.687162]
MAP_SAVE_PATH = 'maps/map.html'

now = datetime.now()
HOUR = now.hour
SUNSET_H = 19

WINDOW_WIDTH, WIND0W_HEIGHT = 1280, 720
MAP_WIDTH, MAP_HEIGHT = 751, 441


THEME = {
    'map-theme': config['THEME']['day_map_theme'] if HOUR < SUNSET_H else config['THEME']['night_map_theme'],
    'font': '#' + config['THEME']['day_color'] if HOUR < SUNSET_H else '#' + config['THEME']['night_color'],
    'states': bool(int(config['THEME']['day_states'])) if HOUR < SUNSET_H else bool(int(config['THEME']['night_states'])),
    'marker-color': '#' + config['THEME']['marker_color']
}

# => DESTINATIONS OF THE BIGGER CITIES (Those are lat and lon in range - not the city coords)
DESTINATIONS = {    # 24 requests / per use
    'BERM': [38.779623, -68.006869],
    'NJ': [40.035871, -74.203157],
    'MIAMI': [25.469607, -78.400208],
    'DALLAS': [32.645431, -94.703918],
    'LV-LA': [35.794721, -117.198012],
    'LA': [33.572598, -115.418228],
    'SAN-F': [33.572598, -115.418228],
    'SEATTLE': [47.443120, -120.984437],
    'CHIC': [41.369192, -87.895747],
    'DET': [41.926463, -83.094810],
    'WAS': [38.785344, -76.742474],
    'NY': [40.879288, -73.636243],
    'BOST': [42.186268, -70.901687],
    'HNL': [19.758981, -153.780139],
    'CAL': [38.862311, -120.054232],
    'DEN': [38.832486, -107.468542],
    'GEOR': [31.168608, -82.635840],
    'OHIO': [38.528513, -84.997466],
    'PENS': [40.652992, -78.822506],
    'NY-STATE': [43.827342, -74.523746],
    'ATL-ISL': [18.786300, -66.121798],
    'ALT': [32.003044, -71.439180],
    'NEW-MEX': [35.866438, -104.398163],
    'OKH': [35.294592, -95.169648]
}

# => ALL USA AIRPORTS
US_AIRPORTS = pd.read_csv(AIRPORTS_CSV_FILE, usecols=[
    'longitude_deg', 'latitude_deg', 'iata_code', 'name'], nrows=AIRPORTS_LIMIT+1)


directions = ['north', 'east', 'south', 'west']

# => MARKERS
MARKERS = {
    key: str(i + 1) for i, key in enumerate(directions)
}

ANGLES = [
    [0, 90, 'north'],
    [91, 180, 'east'],
    [181, 270, 'south'],
    [271, 360, 'west'],
]

ICON_SIZE = (10, 10)
ICON_URL = r'https://banner2.cleanpng.com/20181129/' \
           r'xbw/kisspng-computer-icons-airplane-clip' \
           r'-art-portable-network-orange-airplane-2-icon' \
           r'-free-orange-airplane-icon-5bff7a8b9ae4d1.8655483315434697076345.jpg'
