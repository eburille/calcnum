# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 16:30:35 2023

@author: 00325133
"""

import numpy as np
import area2 as a2

def gradiente(z):
    x=z[0][0]
    y=z[1][0]
    
    
    g=np.array([[np.exp(x)*np.exp(y)+2*x],
                [np.exp(x)*np.exp(y)+2*y]])
    return g


x0=np.array([[1],
             [-1]])

minimo=a2.alg_grad(gradiente,50000,x0)