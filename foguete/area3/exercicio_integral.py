# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 19:37:04 2023

@author: LABF11501
"""
import area3 as a3

def y(x):
    return np.sin(x)
N=1000
I1 = a3.ponto_medio(y,0,np.pi,N) 
I2 = a3.trapezio(y,0,np.pi,N) 
I3 = a3.simpson(y,0,np.pi,N) 
print("Ponto Médio =",I1)
print("Erro Ponto Médio =",2-I1)
print("Trapézio =",I2)
print("Erro Trapezio =",2-I2)
print("Simpson =",I3)
print("Erro Simpson =",2-I3)
