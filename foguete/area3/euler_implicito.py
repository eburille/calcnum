# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 16:04:09 2023

@author: 00325133
"""
import numpy as np
import matplotlib.pyplot as plt





def euler_explicito(f,t0,y0,h,N):
    y=np.zeros(N+1)
    t=np.zeros(N+1)
    y[0]=y0
    t[0]=t0
    for i in range(N):
        y[i+1]=y[i]+h*f(y[i],t[i])
        t[i+1]=t[i]+h
    return [t,y]

def euler_2grau(f,t0,y0,h,N):
    n=y0.size
    y=np.zeros((n,N+1))
    t=np.zeros(N+1)
    y[:,0]=y0
    t[0]=t0
    for i in range(N):
        y[:,i+1]=y[:,i]+h*f(y[:,i],t[i])
        t[i+1]=t[i]+h
    return [t,y]

def secante(fff,x1,x2,N):
    for i in range(N):
        x3=(x1*fff(x2)-fff(x1)*x2)/(fff(x2)-fff(x1))
        x1=x2
        x2=x3
        if(x1==x2): break
    return x3

def euler_implicito(f,t0,y0,h,N):
    y=np.zeros(N+1)
    t=np.zeros(N+1)
    y[0]=y0
    t[0]=t0
    for i in range(N):
        t[i+1]=t[i]+h
        ff = lambda x: x-y[i]-h*f(x,t[i+1])
        z=secante(ff,y[i],y[i]+0.1,100)
        y[i+1]=z
    return [t,y]
    

#def f(y,t):
 #   f=np.array([0.1*(y[0])**2-9.8,
   #             y[0]])
    #return f   

t0=0
y0=np.array([0,100])
h=0.01
N=1000     

#[T,Y]=euler_implicito(f,0,1,0.01,100)
#plt.plot(T,Y)

#[T,Y1]=euler_2grau(f,t0,y0,h,N)
#plt.plot(T,Y1[0,:])