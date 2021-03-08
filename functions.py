# -*- coding: utf-8 -*-

""" Description: project functions """

# => 3-RD PARTY IMPORTS
import json
import pandas as pd
import configparser
from datetime import datetime
import random


CONFIG_FILE = 'config/config.ini'

config = configparser.ConfigParser()
config.read(CONFIG_FILE)

JSON_FILE = 'json/data.json'
AIRPORTS_CSV_FILE = 'csv/list-of-airports-in-usa.csv'

MARKER_PATH = 'res/plane.png'
AIRPORTS_LIMIT = int(config['DATA']['airport_nrows'])
SAVE_PATH = 'res/basemap.png'

now = datetime.now()
HOUR = now.hour

THEME = {
    'water': '#' + config['THEME']['day_water'] if HOUR < 19 else '#' + config['THEME']['night_water'],
    'ground': '#' + config['THEME']['day_ground'] if HOUR < 19 else '#' + config['THEME']['night_ground'],
    'font': '#' + config['THEME']['day_color'] if HOUR < 19 else '#' + config['THEME']['night_color'],
    'states': bool(int(config['THEME']['day_states'])) if HOUR < 19 else bool(int(config['THEME']['night_states'])),
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
    # [0, 360 // 4, 'north'],
    # [360 // 4, (360 // 4) * 2, 'east'],
    # [(360 // 4) * 2, (360 // 4) * 3, 'south'],
    # [(360 // 4) * 3, 360, 'west']

    [0, 90, 'north'],
    [91, 180, 'east'],
    [181, 270, 'south'],
    [271, 360, 'west'],
]


def change_json(content: dict, filename: str) -> bool:
    current = load_from_json(filename)

    current["ctime"] = content["ctime"]

    if len(current) > 0:
        if content["ac"] is not None:
            ac = current["ac"]

            if ac is not None:
                for flight in content["ac"]:
                    ac.append(flight)
            else: ac = content["ac"]
            current["ac"] = ac

    else:
        current = content

    return write_to_json(content, filename, current)


def write_to_json(content: dict, filename: str, current=None):
    to_write = current if current is not None else content

    try:
        with open(filename, 'w') as file:
            json.dump(to_write, file, indent=4)

            return True

    except FileNotFoundError:
        print(f'[ FILE ERROR ] FILE NOT FOUND! - {filename}')
        return False


def load_from_json(filename: str) -> dict:
    try:
        with open(filename) as file:
            json_content = json.load(file)

            return json_content

    except FileNotFoundError:
        print(f'[ FILE ERROR ] FILE NOT FOUND! - {filename}')
        return {}


def increment_calls(config, filename: str):
    curr = int(config['API']['calls'])
    config.set('API', 'calls', str(curr+1))

    with open(filename, 'w') as file:
        config.write(file)

    return config


def angle(heading):
    if heading is None or heading == '' or heading == ' ': return random.choice(MARKERS)

    heading = int(heading)

    if ANGLES[0][0] <= heading <= ANGLES[0][1]: return MARKERS[ANGLES[0][2]]  # NORTH
    if ANGLES[1][0] <= heading <= ANGLES[1][1]: return MARKERS[ANGLES[1][2]]  # EAST
    if ANGLES[2][0] <= heading <= ANGLES[2][1]: return MARKERS[ANGLES[2][2]]  # SOUTH
    if ANGLES[3][0] <= heading <= ANGLES[3][1]: return MARKERS[ANGLES[3][2]]  # WEST

