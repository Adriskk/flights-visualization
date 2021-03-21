# -*- coding: utf-8 -*-

""" Description: project functions """

# => 3-RD PARTY IMPORTS
import json
import random
from PyQt5 import QtWebEngineWidgets
import folium
import io
from data import *


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

    if CONNECTED_ANGLES[0][0] <= heading <= CONNECTED_ANGLES[0][1]: return CONNECTED_ANGLES[0][2]  # NE
    if CONNECTED_ANGLES[1][0] <= heading <= CONNECTED_ANGLES[1][1]: return CONNECTED_ANGLES[1][2]  # SE
    if CONNECTED_ANGLES[2][0] <= heading <= CONNECTED_ANGLES[2][1]: return CONNECTED_ANGLES[2][2]  # SW
    if CONNECTED_ANGLES[3][0] <= heading <= CONNECTED_ANGLES[3][1]: return CONNECTED_ANGLES[3][2]  # NW

    if ANGLES[0][0] <= heading <= ANGLES[0][1]: return ANGLES[0][2]  # NORTH
    if ANGLES[1][0] <= heading <= ANGLES[1][1]: return ANGLES[1][2]  # EAST
    if ANGLES[2][0] <= heading <= ANGLES[2][1]: return ANGLES[2][2]  # SOUTH
    if ANGLES[3][0] <= heading <= ANGLES[3][1]: return ANGLES[3][2]  # WEST


def folium_map():
    MAP = folium.Map(location=LOCATION, zoom_start=5)
    data = io.BytesIO()
    MAP.save(data, close_file=False)
    WebWidget = QtWebEngineWidgets.QWebEngineView()
    WebWidget.setHtml(data.getvalue().decode())
    return WebWidget


def change_the_current_map_colors():
    conf = configparser.ConfigParser()
    conf.read('config/config.ini')

    current = THEME['map-theme']

    NIGHT = conf['THEME']['night_map_theme']
    DAY = conf['THEME']['day_map_theme']
    MODE = ''

    if current == NIGHT:
        NEXT = DAY
        MODE = 'light'

    else:
        NEXT = NIGHT
        MODE = 'dark'

    THEME['map-theme'] = NEXT

    return MODE

