# -*- coding: utf-8 -*-
"""
Created on Sun May 28 22:04:09 2017

@author: Jenny
"""

import numpy as np
from matplotlib import pyplot as plt

T = 201
int_grid = np.zeros(T)
mid = T//2
int_grid[mid] = 1.0

grid = np.zeros((T,T))

curr_grid = int_grid

grid[0] = int_grid

myobj = plt.matshow(grid, cmap=plt.cm.gray)

for i in np.arange(0,T-1):
    for j in np.arange(0,T-2):
        curr_grid = grid[i]
        if curr_grid[j] == 0.0 and curr_grid[j+2] == 0.0:
            grid[i+1][j+1] = 0.0
        elif curr_grid[j] == 1.0 and curr_grid[j+2] == 0.0:
            grid[i+1][j+1] = 1.0
        elif curr_grid[j] == 0.0 and curr_grid[j+2] == 1.0:
            grid[i+1][j+1] = 1.0
        else:
            grid[i+1][j+1] = 0.0

myobj.set_data(grid)
plt.draw()
