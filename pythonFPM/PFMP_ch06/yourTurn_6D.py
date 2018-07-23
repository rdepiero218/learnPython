#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 18:31:52 2018

@author: mindup610

Your Turn 6D
A Student's Guide to Physical Modeling with Python

Make a surface plot of the function z = x^2 + y^2
over a grid for x, y from -1 to 1
"""
import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D

points = np.linspace(-1,1,101)
X, Y = np.meshgrid(points, points)

Z = X**2 + Y**2

ax = Axes3D(plt.figure())
ax.plot_surface(X,Y,Z)
# ax.plot_surface(X,Y,Z, rstride=1, cstride=1f)
