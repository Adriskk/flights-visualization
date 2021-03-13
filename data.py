# -*- coding: utf-8 -*-

# => 3-RD PARTY IMPORTS
import pandas as pd
import configparser
from datetime import datetime
import folium


CONFIG_FILE = 'config/config.ini'

config = configparser.ConfigParser()
config.read(CONFIG_FILE)

AIRPORTS_CSV_FILE = config['DATA']['airports_csv_file']
AIRPORTS_LIMIT = int(config['DATA']['airport_nrows'])
MAX_AIRCRAFTS = int(config['DATA']['air_crafts_amount'])

MODEL_PATH = config['ML']['kmeans_model_path']
OLD_MODEL_PATH = config['ML']['knr_model_path']
CLUSTERS = int(config['ML']['clusters'])

LOCATION = [37.870206, -99.687162]
MAP_SAVE_PATH = config['MAP']['map_save_path']

now = datetime.now()
HOUR = now.hour
SUNSET_H = int(config['DATA']['sunset'])

WINDOW_WIDTH, WIND0W_HEIGHT = int(config['WINDOW']['width']), int(config['WINDOW']['height'])
MAP_WIDTH, MAP_HEIGHT = int(config['MAP']['width']), int(config['MAP']['height'])


THEME = {
    'map-theme': config['THEME']['day_map_theme'] if HOUR < SUNSET_H else config['THEME']['night_map_theme'],
    'font': '#' + config['THEME']['day_color'] if HOUR < SUNSET_H else '#' + config['THEME']['night_color'],
    'states': bool(int(config['THEME']['day_states'])) if HOUR < SUNSET_H else bool(int(config['THEME']['night_states'])),
    'marker-color': '#' + config['THEME']['marker_color']
}

# => ALL USA AIRPORTS
US_AIRPORTS = pd.read_csv(AIRPORTS_CSV_FILE, usecols=[
    'longitude_deg', 'latitude_deg', 'iata_code', 'name'], nrows=AIRPORTS_LIMIT+1)


directions = ['N', 'E', 'S', 'W']

# => MARKERS
MARKERS = {
    key: str(i + 1) for i, key in enumerate(directions)
}

ANGLES = [
    [0, 90, 'N'],
    [91, 180, 'E'],
    [181, 270, 'S'],
    [271, 360, 'W'],
]

