# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

import numpy as np
import area2 as a2
import matplotlib.pyplot as plt

x=np.array([1,2,3,4,5])
y=np.array([7,4,3,1,0])

def f1(x):
    y = np.array([35.0*np.exp(-x/2)])
    
    return y

#def f2(x):
 #   y=


k1=a2.ajuste(f1,x,y)
print("k1",k1)
plt.plot(x,y,'o')

xx=np.linspace(0,7,1000)
yy=k1@f1(xx)
print("xx",xx)
print("yy",yy)

plt.plot(xx,yy)