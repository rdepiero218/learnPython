#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 18:29:08 2018

@author: mindup610
Code for Lab 03: Section 9.1.3
A Student's Guide to Physical Modeling with Python
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as sim
from mpl_toolkits.mplot3d import Axes3D

plt.close('all')

# Create a grid of points for the Gaussian filter.
v = np.arange(-25, 26)
X, Y = np.meshgrid(v, v)

impulse = np.zeros( (51, 51) )

impulse[25, 25] = 1.0

# define filters to be used
gauss = np.loadtxt("gauss_filter.csv", delimiter=',')
smSquare_filter = np.ones( (3,3) ) / 9

# import image
catPic = plt.imread('bwCat.tif')



response1 = sim.convolve(catPic, smSquare_filter)
response2 = sim.convolve(catPic, gauss)

#plt.figure()
#plt.subplot(1, 3, 1)
#plt.imshow(catPic)
#plt.set_cmap('gray')
#plt.title('Original Image')
#plt.subplot(1,3,2)
#plt.imshow(response1)
#plt.title('Small Square Filter')
#plt.subplot(1,3,3)
#plt.imshow(response2)
#plt.title('Gauss Filter')


sDot = sim.convolve(impulse, smSquare_filter)
gDot = sim.convolve(impulse, gauss)

plt.figure()
plt.subplot(1,3,1)
plt.imshow(impulse)
plt.title('Impulse')

plt.subplot(1,3,2)
plt.imshow(sDot)
plt.title('Small Square')

plt.subplot(1,3,3)
plt.imshow(gDot)
plt.title('Gauss')

ax = Axes3D(plt.figure())
ax.surface_plot(X,Y,impulse, rstride=1, cstride=1)






#ax = Axes3D(plt.figure())
#ax.plot_surface(sDot)