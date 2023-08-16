import numpy as np
import matplotlib.pyplot as plt

def f(y, x):
    f = (x - y) / y
    return f

def euler(f, t0, y0, h, N):
    y = np.zeros(N+1)
    t = np.zeros(N+1)
    y[0] = y0
    t[0] = t0
    for i in range(N):
        t[i+1] = t[i] + h
        y[i+1] = y[i] + h*f(y[i], t[i])
        
    return [t, y]

def euler_melhorado(f, t0, y0, h, N):
    y = np.zeros(N+1)
    t = np.zeros(N+1)
    y[0] = y0
    t[0] = t0
    for i in range(N):
        k1 = f(y[i], t[i])
        k2 = f(y[i]+h/2*k1, t[1]+h/2)
        
        y[i+1] = y[i] + h*k2
        t[i+1] = t[i] + h
    return [t, y]

def predica_correcao(f, t0, y0, h, N):
    y = np.zeros(N+1)
    t = np.zeros(N+1)
    y[0] = y0
    t[0] = t0
    for i in range(N):
        k1 = f(y[i], t[i])
        k2 = f(y[i]+h*k1, t[1]+h)
        
        y[i+1] = y[i] + h*(k1+k2)/2
        t[i+1] = t[i] + h
    return [t, y]


if __name__ == '__main__':
    t0 = 2
    y0 = 3
    h = 0.01
    N = 500

    [T, Y1] = euler(f, t0, y0, h, N)
    [T, Y2] = euler_melhorado(f, t0, y0, h, N)

    ta = np.linspace(t0, t0 + h*N, 1000)
    ya = ta/2 + 4/ta
    

    plt.plot(ta, ya)
    plt.plot(T, Y1,  'o')
    plt.plot(T, Y2,  'o')
    plt.show()