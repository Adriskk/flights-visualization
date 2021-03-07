import requests
import configparser
import json
import functions as func

config = configparser.ConfigParser()
config.read(func.CONFIG_FILE)

CALLS = int(config['API']['calls'])
DEBUG = int(config['API']['debug'])
DEBUG = True if int(DEBUG) == 1 else False
COLUMNS = ['long', 'lat', 'position-source']


# => API DATA
# LAT = str(40)
# LON = str(-85)
# => DISTANCE WILL ALWAYS BE 25 CUZ IN THIS API
# => THE DISTANCE FROM GIVEN POINT CANNOT CHANGE ;<
DIST = str(25)

URL = config['API']['url']
API_KEY = config['API']['api_key']
HOST = config['API']['host']

print('CURRENT CALLS: ', CALLS + 1)


def get_flights():
    if CALLS < 360 and DEBUG is False:

        for destination in func.DESTINATIONS:
            LAT, LON = func.DESTINATIONS[destination]
            print(destination)

            # => CREATE URL
            url = URL + "lat/" + str(int(LAT)) + "/lon/" + str(int(LON)) + "/dist/" + DIST + "/"

            headers = {
                'x-rapidapi-key': API_KEY,
                'x-rapidapi-host': HOST
            }

            response = requests.request("GET", url, headers=headers).json()

            # => INCREMENT THE CALLS VALUE IN CONFIG
            func.increment_calls(config, func.CONFIG_FILE)

            # => SAVE TO FILENAME
            result = func.change_json(response, func.JSON_FILE)

            if result is False:
                print("[ ERROR ] Json hasn't been saved! ")

            # return response

    # => LOAD FROM JSON FILE
    elif DEBUG:
        print('[  DEBUG MODE  ] [ LOAD FROM JSON FILE ]')

        content = func.load_from_json(func.JSON_FILE)
        return content

    # => NO DEBUG NO API CALLS
    else:
        raise Exception('Cannot do more api calls! ')
