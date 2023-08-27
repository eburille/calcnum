# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 13:43:16 2023

@author: Mariana
"""
#a=6,2, b=1,65, c=4, d=5
import numpy as np
import matplotlib.pyplot as plt


#def angulosaida(x):
   
    
 #  y=180-((np.arccos(((41,1625-(2*1.65*6.2*np.cos(x)))+25-16)/(2*(np.sqrt(41,1625-(2*1.65*6.2*np.cos(x))))*5)))+(np.arccos(((41,1625-(2*1.65*6.2*np.cos(x)))+38.44-2.7225)/(2*(np.sqrt(41,1625-(2*1.65*6.2*np.cos(x))))*6.2))))
  # return y     
   

          


def z(x):
    e=41.1625-(2*1.65*6.2*np.cos(x))
    e1=np.sqrt(e)
    return e1
    
def alfa(x):
    a=np.arccos((z(x)**2+25-16)/(2*z(x)*5))
    return a
   
def beta(x):
    b=np.arccos((z(x)**2+38.44-2.7225)/(2*z(x)*6.2))
    return b

def angulo_saida(x):
    a4=180-(alfa(x)+beta(x))
    return a4


x=0    
for i in range(37):
      
      y=angulo_saida(x)
      x=x+(10*(np.pi/180))
      print("angulo_de_saida",y)
      
      
      
x = np.linspace(0,6,1000)
plt.plot(x,angulo_saida(x))