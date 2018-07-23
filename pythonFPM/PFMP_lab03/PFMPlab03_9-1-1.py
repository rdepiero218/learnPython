#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 17:54:11 2018

@author: mindup610
"""
import numpy as np
import matplotlib.pyplot as plt

import scipy.ndimage as sim

impulse = np.zeros( (51, 51))

impulse[25, 25] = 1.0

my_filter = np.ones( (3,3) ) / 9

response = sim.convolve(impulse, my_filter)

plt.figure()
plt.imshow(impulse)

plt.figure()
plt.imshow(response)