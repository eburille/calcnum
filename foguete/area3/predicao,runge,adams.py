# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np




def predicao_correcao(f,t0,y0,h,N):
    y=np.zeros(N+1)
    t=np.zeros(N+1)
    y[0]=y0
    t[0]=t0
    for i in range(N):
        k1=f(y[i],t[i])
        k2=f(y[i]+h*k1,t[i]+h)
        y[i+1]=y[i]+h*(k1+k2)/2
        t[i+1]=t[i]+h
    return [t,y]

def runge4(f,t0,y0,h,N):
    y=np.zeros(N+1)
    t=np.zeros(N+1)
    y[0]=y0
    t[0]=t0
    for i in range(N):
        k1=f(y[i],t[i])
        k2=f(y[i]+h/2*k1,t[i]+h/2)
        k3=f(y[i]+h/2*k2,t[i]+h/2)
        k4=f(y[i]+h*k3,t[i]+h)
        y[i+1]=y[i]+h*(k1+2*k2+2*k3+k4)/6
        t[i+1]=t[i]+h
    return [t,y]

def adams4(f,t0,y0,h,N):
    y=np.zeros(N+1)
    t=np.zeros(N+1)
    y[0]=y0
    t[0]=t0
    for i in range(N):
        k1=f(y[i],t[i])
        k2=f(y[i-1],t[i-1])
        k3=f(y[i-2],t[i-2])
        k4=f(y[i-3],t[i-3])
        y[i+1]=y[i]+h*(55*k1-59*k2+37*k3-9*k4)/24
        t[i+1]=t[i]+h
    return[t,y]
    

def euler_melhorado(f,t0,y0,h,N):
    y=np.zeros(N+1)
    t=np.zeros(N+1)
    y[0]=y0
    t[0]=t0
    for i in range(N):
        k1=f(y[i],t[i])
        k2=f(y[i]+h/2*k1,t[i]+h/2)
        y[i+1]=y[i]+h*k2
        t[i+1]=t[i]+h
    return [t,y]