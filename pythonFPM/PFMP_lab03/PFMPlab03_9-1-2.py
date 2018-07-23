i#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 17:58:17 2018

@author: mindup610

Code for Lab 03: Section 9.1.2 
A Student's Guide to Physical Modeling with Python
"""
import numpy as np
import matplotlib.pyplot as plt

import scipy.ndimage as sim

#impulse = np.zeros( (51, 51))
#
#impulse[25, 25] = 1.0

# define filters to be used
smSquare_filter = np.ones( (3,3) ) / 9
lgSquare_filter = np.ones( (15,15) ) / 225

# import image
catPic = plt.imread('bwCat.tif')

response1 = sim.convolve(catPic, smSquare_filter, mode='constant')
response2 = sim.convolve(catPic, lgSquare_filter, mode='constant')

plt.figure()
plt.subplot(1, 3, 1)
plt.imshow(catPic)
plt.set_cmap('gray')
plt.title('Original Image')
plt.subplot(1,3,2)
plt.imshow(response1)
plt.title('Convolution w Small Square Filter')
plt.subplot(1,3,3)
plt.imshow(response2)
plt.title('Convolution w Large Square Filter')
