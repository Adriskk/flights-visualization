# -*- coding: utf-8 -*-

""" Description: this script contains functions, which extract given data from json dict """


def get_values(data: dict, keys: list) -> list:
    ac = data['ac']

    values = []

    for plane in ac:
        to_add = {}

        for key in keys:

            if key in plane.keys(): to_add[key] = plane[key]
            else: break

        values.append(to_add)

    return values


def get_labels(data: list, key: str) -> list:
    labels = []

    for element in data:
        if key in element.keys():
            label = element[key]
            labels.append(label)
        else: labels.append('')

    return labels


def get_from_opensky(states):
    try:
        for state in states.states:

            if state is not None:
                yield [
                    state.longitude,
                    state.latitude,
                    state.velocity,
                    state.heading,
                    state.callsign,
                    state.last_contact
                ]

        # return [[state.longitude, state.latitude, state.velocity] for state in states.states]
    except AttributeError:
        return False
