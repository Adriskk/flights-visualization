# -*- coding: utf-8 -*-

""" Description: visualize file - shows the map with current flights up the US """

# => 3-RD PARTY IMPORTS
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import time

# => IMPORTS
import functions as func
import request as req
import extract


def create_basemap(airports: dict):
    figure = plt.figure(figsize=(16, 10))

    MAP = Basemap(
        projection='mill',
        llcrnrlat=10,
        urcrnrlat=60,
        llcrnrlon=-170,
        urcrnrlon=-20,
        resolution='c'
    )

    MAP.drawcoastlines()

    # MAP.drawparallels(np.arange(-90, 90, 10), labels=[True, False, False, False])
    # MAP.drawparallels(np.arange(-180, 180, 30), labels=[True, False, False, False])

    for iata, lat, lon in zip(airports['iata_code'][1:], airports['latitude_deg'][1:], airports['longitude_deg'][1:]):

        MAP.scatter(
            int(float(lon)), int(float(lat)),
            latlon=True, s=50, c="w", marker="o", zorder=8, alpha=.5
        )

        # => SHOW AIRPORT NAME
        x, y = MAP(int(float(lon))+1, int(float(lat))-1)
        plt.text(x, y, iata, fontsize=8, zorder=6, color=func.THEME['font'], weight='bold')

    for scatter in AIRCRAFTS:
        lon, lat, vel, heading = scatter

        MAP.scatter(
            int(lon), int(lat),
            latlon=True, s=100, marker=func.angle(heading), c=func.THEME['marker-color'], zorder=4, alpha=.9
        )

        # => SHOW icao CODE OF EVERY PLANE THAT HAS THIS DATA
        # x, y = MAP(int(float(scatter['lon'])), int(float(scatter['lat'])))
        # plt.text(x+10, y, label, fontsize=9, zorder=9, color='yellow')

    # MAP.scatter(-100, 60, latlon=True, s=2000, marker='^')
    # MAP.scatter(-50, 65, latlon=True, s=2000, marker='^')

    # MAP.bluemarble()
    MAP.drawmapboundary(fill_color=func.THEME['water'])
    MAP.drawcountries()
    MAP.fillcontinents(color=func.THEME['ground'], lake_color=func.THEME['water'])

    if func.THEME['states']:
        MAP.drawstates()

    plt.savefig(func.SAVE_PATH)
    plt.show(color='#fbc531')


# => GET JSON DATA
# response = req.get_flights()
# data = func.load_from_json(func.JSON_FILE)

while True:
    AIRCRAFTS = []

    for pack in extract.get_from_opensky(req.get_air_crafts_pos()):
        if pack is False:
            time.sleep(10)
            continue

        AIRCRAFTS.append(pack)

    # new = extract.get_values(data, ["lat", "lon", "from", "to", "icao"])
    # labels = extract.get_labels(new, "icao")
    create_basemap(func.US_AIRPORTS)

    # -> TRUNCATE THE JSON FILE FOR NEW DATA
    if not req.DEBUG:
        func.write_to_json({ "ac": [] }, func.JSON_FILE)

    time.sleep(5)
