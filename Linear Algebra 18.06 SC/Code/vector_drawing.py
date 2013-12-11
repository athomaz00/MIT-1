# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 09:46:27 2013

@author: joshua
"""

import matplotlib.pyplot as plt
import numpy as np

vectors = [np.array([1, 0]), np.array([0, 1])]
xmin = 0
xmax = 10
ymin = 0
ymax = 10

plt.ylim((ymin, ymax))
plt.xlim((xmin, xmax))
ax = plt.axes()
plt.grid(ax)
              

def visual_addition(vectors):
    x = 0
    y = 0
    for v in vectors:
        plt.arrow(x, y, v[0], v[1], head_width=0.1, head_length=0.1)
        x += v[0]
        y += v[1]

    
# visual_addition(vectors)
# plt.show()
    
def visual_scaling(vectors, scalars):
    assert(len(vectors)==len(scalars))
    visual_addition(map(np.multiply, vectors, scalars))


# for i in range(1, 100):
#     visual_scaling(vectors, [i/10., i/10.])
# plt.show()