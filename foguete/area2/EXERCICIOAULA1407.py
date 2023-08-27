# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 16:20:16 2023

@author: 00325133
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig=plt.figure(figsize=(12,10))
ax = Axes3D(fig)

x=np.arange(-5, 5.1, 0.2)
y=np.arange(-5, 5.1, 0.2)

X, Y = np.meshgrid(x,y)
Z=X**4*Y**4
#Z = (X**2+Y**2)*np.exp(Y)*np.exp(X)
#Z=(X**2+Y**2+X*Y)/100+np.sin(X)+np.sin(Y)


cset=ax.scatter(X, Y, Z)