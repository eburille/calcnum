# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 16:21:47 2023

@author: 00325133
"""
import numpy as np
import area2 as a2

def f(x):
    y=np.array([[np.sin(x[0,0])+np.cos(x[1,0])-np.sqrt(2)],
                [np.sin(x[0,0])-np.cos(x[1,0])]])
    return y

def J(x):
    y=np.array([[np.cos(x[0,0]), -np.sin(x[1,0])],
                [np.cos(x[0,0]),  np.sin(x[1,0])]])
    return y

z=np.array([[1], [1]])


x=a2.newton(J,f,z,10)

