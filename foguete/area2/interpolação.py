# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 16:31:06 2023

@author: 00325133
"""
import numpy as np
import matplotlib.pyplot as plt

a=np.array([2,0,0])


x=np.array([1,2,3,4,5])
y=np.array([7,4,3,1,0])
plt.plot(x,y,'o')

xx=np.linspace(0,7,100)



def polinomio(a,x):
    n=a.size
    m=x.size
    y=np.zeros(m)
    for i in range(n):
        y=y+a[i]*x**(n-i-1)
    return y

def interpola(x,y):
    m=x.size
    A=np.zeros((m,m))
    for i in range(m):
        A[:,m-1-i]=x**i
    return np.linalg.solve(A,y)

a=interpola(x,y)    
print("a",a)
yy=polinomio(a,xx)
plt.plot(xx,yy)

h=x[1:]-x[0:-1]
n=x.size
A=np.zeros((n,n))
B=np.zeros((n,1))
A[0,0]=1
A[-1,-1]=1
for i in range(1,n-1):
     A[i,i-1]=h[i-1]
     A[i,i]=2*h[i-1]+2*h[i]
     A[i,i+1]=h[i]
     B[i]=3*(y[i+1]-y[i])/h[i]-3*(y[i+1]-y[i])/h[i]
     
c=np.linalg.solve(A,B)
a=y    