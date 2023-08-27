# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 21:37:00 2023

@author: Mariana
"""

import numpy as np
import matplotlib.pyplot as plt
import math


#def angulo(x):
#z=np.sqrt(41,1625-(2*1.65*6.2*np.cos(x)))    
#a=math.acos((z**2+25-16)/2*z*5)
#b=math.acos((z**2+38.44-2.7225)/2*z*6.2)
#a4=180-(a+b)

x=0    
for i in range(37):
      
     
      y=angulo_saida(x)
      x=x+(10*(np.pi/180))
      print("angulo_de_saida",y)
   
    
    
   
    
    
x = np.linspace(0,6,1000)
plt.plot(x,angulo(x))