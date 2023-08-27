# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 13:12:48 2023

@author: Mariana
"""


#a=6,2, b=1,65, c=4, d=5

import numpy as np
import matplotlib.pyplot as plt




def angulo(x):
    e=(41.1625-(2*1.65*6.2*np.cos(x)))
    z=np.sqrt(e)    
    a=(z**2+25-16)/(2*z*5)
    alfa=np.arccos(a)
    b=(z**2+38.44-2.7225)/(2*z*6.2)
    beta=np.arccos(b)
    a4=180-(alfa+beta)
    return a4
x=0    
#for x in range(37):
      
 #     x=x*(np.pi/180)
  #    y=angulo(x)
   #   x=x+(10*(np.pi/180))
    #  print("angulo_de_saida",y)
      
x = np.linspace(0,6,1000)
plt.plot(x,angulo(x))
