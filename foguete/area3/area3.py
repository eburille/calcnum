import numpy as np

def dif_progressiva(f,x,h):
    df = (f(x+h)-f(x))/h
    return df

def dif_regressiva(f,x,h):
    df = (f(x)-f(x-h))/h
    return df

def dif_central(f,x,h):
    df = (f(x+h)-f(x-h))/(2*h)
    return df

def dif_progressiva3(f,x,h):
    df = (-3*f(x)+4*f(x+h)-f(x+2*h))/(2*h)
    return df

def dif2(f,x,h):
    df = (f(x-h)-2*f(x)+f(x+h))/(h**2)
    return df

def jacobiano(F,x,h):
    n=x.size
    m=F(x).size
    J=np.zeros((m,n))
    for i in range(n):
        H=np.zeros((n,1))
        H[i][0]=h
        J[:,i]=((F(x+H)-F(x-H))/(2*h))[:,0]
    return J

def gradiente(F,x,h):
    y=jacobiano(F,x,h)
    return y.transpose()

def ponto_medio(f,a,b,N):
    I=0
    h=(b-a)/N
    for i in range(N):
        I=I+f(a+h/2*(2*i+1))
    I=I*h
    return I

def trapezio(f,a,b,N):
    I=(f(a)+f(b))/2
    h=(b-a)/N
    for i in range(N-1):
        I=I+f(a+h*(i+1))
    I=I*h
    return I

def simpson(f,a,b,N):
    I=f(a)+f(b)
    h=(b-a)/N
    for i in range(N):
        I=I+4*f(a+h*(i+1/2))
    for i in range(N-1):
        I=I+2*f(a+h*(i+1))
    I=I*h/6
    return I    