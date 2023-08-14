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
        t_meio = t[i] + h/2
        y_meio = y[i]+ h/2 * f(y[i], t_meio)
        
        y[i+1] = y[i] + h*f(y_meio, t_meio)
        t[i+1] = t[i] + h
    return [t, y]


if __name__ == '__main__':
    t0 = 2
    y0 = 3
    h = 0.01
    N = 50

    [T, Y1] = euler(f, t0, y0, h, N)
    [T, Y2] = euler_melhorado(f, t0, y0, h, N)

    ta = np.linspace(t0, t0 + h*N, 1000)
    ya = ta/2 + 4/ta
    

    plt.plot(ta, ya)
    plt.plot(T, Y1,  'o')
    plt.plot(T, Y2,  'o')
    plt.show()