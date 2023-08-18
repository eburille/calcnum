import numpy as np  
import matplotlib.pyplot as plt


def secante(f, a, b, N, e1, e2, e3):
    pa = a
    for i in range(N):
        if (f(b) - f(a)) == 0:
            return p
        p = (a*f(b) - b*f(a)) / (f(b) - f(a))

        b = a
        a = p

        if abs(f(p)) <= e1:
            print(f'parei aqui 1 - i = {i}')
            break

        if abs(p - pa) <= e2:
            print(f'parei aqui 2 - i = {i}')
            break

        if abs((p-pa) / p) <= e3:
            print(f'parei aqui 3 - i = {i}')
            break

    return p

def f(x):
    y = np.log(x) + x
    return y

def df(x):
    y = 1/x + 1
    return y

def euler_explicito(f, t0, y0, h, N):
    y = np.zeros(N+1)
    t = np.zeros(N+1)
    y[0]=y0
    t[0]=t0
    for i in range(N):
        y[i+1]=y[i]+h*f(y[i],t[i])
        t[i+1]=t[i]+h

    return [t,y]

def euler_implicito(f, t0, y0, h, N):
    y = np.zeros(N+1)
    t = np.zeros(N+1)
    y[0]=y0
    t[0]=t0
    for i in range(N):
        def eq(x):
            e = x - y[i] - h*f(x, t[i])
            return e
        #                                solve( y[i] - y[i-1] - h*f(y[i], t[i]) , 0)
        y[i+1]= secante(eq, y[i], y[i]+0.1, N, 0.001, 0.001, 0.001 )
        t[i+1]=t[i]+h

    return [t,y]

def f(y,t):
    df = -2*y
    return df

tf = 100
N=500
h = tf/N

[t,y] = euler_explicito(f, 0,1, h, N)
[t1, y1] = euler_implicito(f, 0,1, h, N)

#plt.plot(t ,y)
plt.plot(t1 ,y1)
plt.show()