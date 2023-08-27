# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 22:22:23 2023

@author: Mariana
"""

import numpy as np

x=0
e= lambda x:41.1625-(2*1.65*6.2*np.cos(x))

for x in range(37):
    y=e(x)
    x=x+(10*(np.pi/180))
    print("angentrada",y)