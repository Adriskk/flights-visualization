# -*- coding: utf-8 -*-

""" Description: visualize file - shows the map with current flights up the US """

# => 3-RD PARTY IMPORTS
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

# => IMPORTS
import functions as func
import request as req
import extract


def create_basemap(scatters: list, airports: dict):
    figure = plt.figure(figsize=(16, 10))

    MAP = Basemap(
        projection='mill',
        llcrnrlat=0,
        urcrnrlat=80,
        llcrnrlon=-170,
        urcrnrlon=-20,
        resolution='c'
    )

    MAP.drawcoastlines()

    MAP.drawparallels(np.arange(-90, 90, 10), labels=[True, False, False, False])
    MAP.drawparallels(np.arange(-180, 180, 30), labels=[True, False, False, False])

    for iata, lat, lon in zip(airports['iata_code'][1:], airports['latitude_deg'][1:], airports['longitude_deg'][1:]):

        MAP.scatter(
            int(float(lon)), int(float(lat)),
            latlon=True, s=15, c="w", marker=",", zorder=3,
        )

        # => SHOW opicao CODE OF EVERY PLANE THAT HAS THIS DATA
        x, y = MAP(int(float(lon))+1, int(float(lat))-1)
        plt.text(x, y, iata, fontsize=8, zorder=6, color=func.THEME['font'])

    for scatter, label in zip(scatters, labels):
        print(scatter)

        MAP.scatter(
            int(float(scatter['lon'])), int(float(scatter['lat'])),
            latlon=True, s=100, marker="2", c=func.THEME['marker-color'], zorder=8,
        )

        # => SHOW opicao CODE OF EVERY PLANE THAT HAS THIS DATA
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

    # plt.savefig(func.SAVE_PATH)
    plt.show(color='#fbc531')


# => GET JSON DATA
response = req.get_flights()
data = func.load_from_json(func.JSON_FILE)

new = extract.get_values(data, ["lat", "lon", "from", "to", "opicao"])
labels = extract.get_labels(new, "opicao")
create_basemap(new, func.US_AIRPORTS)

# -> TRUNCATE THE JSON FILE FOR NEW DATA
if not req.DEBUG:
    func.write_to_json({ "ac": [] }, func.JSON_FILE)
