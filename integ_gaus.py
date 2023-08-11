import numpy as np

def t(b, a, x):
    t = (b+a)/2  + (b-a)/2  *  x
    return t


def integral(f,A,x):
    n = x.size
    I = 0
    for i in range(n):
        I = I + A[i]* f(x[i])
    return I

def integral_generica(f, x, a, b):
    A = calculaA(x)
    T = t(b, a, x)
    I =  ((b-a)/2) * f(T)@A
    return I

def f(x):
    f = np.e ** (-x) * np.cos(x)
    return f

def calculaA(x):
    n = x.size
    A = np.zeros((n,n))
    B = np.zeros((n,1))    
    for i in range(n):
        A[i,:] = x**i
        if(i%2 == 0):
            B[i] = 2/(i+1)
    
    x = np.linalg.solve(A, B)
    return x

x = np.array([(-3/5)**0.5,  0., (3/5)**0.5])
A = np.array([1, 1, 1])

x = np.polynomial.legendre.legroots((0,0,0,1))
print(x)
A = calculaA(x)

I = integral_generica(f, x, 0, np.inf)
print(I)