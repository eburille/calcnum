# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

import numpy as np
import matplotlib.pyplot as plt
import euler_implicito as euler
from mpl_toolkits.mplot3d import Axes3D

def f(l,t):
    x=l[3]
    y=l[4]
    z=l[5]
    vx=l[0]
    vy=l[1]
    vz=l[2]
    a=-10/(x**2+y**2+z**2)
    f=np.array([a*x,a*y,a*z,vx,vy,vz])
    if (x**2+y**2+z**2)<1:
        f=np.zeros(6)
    return f


t0=0
y0=np.array([0.1,1,1,10,0,0])
h=0.001
N=100000
[t,s]=euler.euler_2grau(f,t0,y0,h,N)

#plt.plot(s[3,:])
#plt.plot(s[4,:])
#plt.plot(s[5,:])

ax = plt.figure().add_subplot(projection='3d')

ax.plot(s[3,:], s[4,:], s[5,:], label='parametric curve', color='r')

u, v = np.mgrid[0:2*np.pi:10j, 0:np.pi:10j]
x = np.cos(u)*np.sin(v)
y = np.sin(u)*np.sin(v)
z = np.cos(v)
ax.plot_wireframe(x, y, z, color="blue")

ax.legend()

plt.show()