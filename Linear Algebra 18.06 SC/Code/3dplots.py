# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 13:28:09 2013

@author: joshua
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plt.plot([0, 2], [0, 0], [0, 0])
plt.plot([0, 0], [0, 3], [0, 0])
plt.plot([0, 0], [0, 0], [0, 4])
plt.plot([0, 2], [0, 3], [0, 4])

plt.show()