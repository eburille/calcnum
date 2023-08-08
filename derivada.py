import numpy as np

def dif_progressiva(f, x, h):
    df = (f(x+h) - f(x))/h
    return df

def dif_regressiva(f, x, h):
    df = (f(x+h) - f(x))/h
    return df

def dif_central(f, x, h):
    df = (f(x+h) - f(x-h))/(2*h)
    return df

def dif_seg(f, x, h):
    df = (dif_central(f, (x+h), h) - dif_central(f, x-h, h))/(2*h)
    return df

def f(x):
    y = np.sin(np.cos(np.exp(x)+1))
    return y

h = 0.000001
x = 1
dfp = dif_progressiva(f, x, h)
dfr = dif_regressiva(f, x, h)
dfc = dif_central(f, x, h)
dfs = dif_seg(f, x, h)

print('f=cos(1)= ', f(x))
print('df/dx prog = ', dfp)

print('df/dx reg = ', dfr)

print('df/dx cen = ', dfc)

print('df/dx seg = ', dfs)