# -*- coding: utf-8 -*-
"""
Created on Sun May 18 17:36:14 2014

@author: joshua
"""

import numpy
from random import shuffle
from matplotlib.pyplot import hist

def hat_check_simulation(n):
    """
    Each of n customers gives a hat to a hat check person who gives them
    back randomly. How many people get back their hats.
    """
    trials = []
    for x in range(10000):
        hats = [x for x in range(n)]
        random_hats = hats[:]
        shuffle(hats)
        same_hats = 0
        for i in range(n):
            if hats[i] == random_hats[i]:
                same_hats += 1
        trials.append(same_hats)
    hist(trials, bins=100, range=(0, 5), histtype='bar')
    return numpy.mean(trials)   