# -*- coding: utf-8 -*-


__author__ = 'Adison'
__date__ = '13.03.2021'
__description__ = 'Trying to find area with the most planes on its coords using K-Means ML algorithm'


import sklearn
from sklearn.cluster import KMeans
from collections import Counter

import matplotlib.pyplot as plt
import pickle
import os

from data import *
from lib import exceptions


def find_aggregate(data):
    samples = [[row[0], row[1]] for row in data if row is not None]

    # => CHECK IF FILE EXISTS
    if os.path.isfile(MODEL_PATH): model = load_model()
    else:
        # => USING K-MEANS MACHINE LEARNING ALGORITHM
        model = KMeans(n_clusters=CLUSTERS)

        if save_model(model) is False: raise exceptions.ModelCannotSaveException

    try:
        model.fit(samples)

    except ValueError:
        return False

    # => GET THE CENTERS OF CLUSTERS
    centers = model.cluster_centers_.tolist()

    # => GET THE AMOUNT OF POINTS ASSOCIATED TO THE GIVEN CLUSTER
    points = dict(Counter(model.labels_))
    aggregate = 0

    for key in points:
        aggregate = centers[key]
        break

    x, y = [float(row[0]) for row in centers], [float(row[1]) for row in centers]

    # plt.scatter(x, y)
    # plt.xlabel('longitude')
    # plt.ylabel('latitude')
    # plt.title('K-Means cluster ml alg')
    # plt.show()

    return aggregate


def save_model(model, exists: bool = False) -> bool:
    if exists is False: open(MODEL_PATH, 'x').close()

    with open(MODEL_PATH, 'wb') as model_file:
        try:
            pickle.dump(model, model_file)
            return True

        except FileNotFoundError or pickle.PicklingError or pickle.UnpicklingError:
            return False


def load_model():
    with open(MODEL_PATH, 'rb') as model_file:
        model = pickle.load(model_file)
    return model


# =>  REPAIR THE COMMON ERROR
