import numpy as np
import matplotlib.pyplot as plt
import area2 as a2

x = np.array([1,2,3,4,5])
y = np.array([7,4,3,1,0])
plt.plot(x,y,'o')

# Ajuste de uma reta
def F(x):
    y = np.array([np.exp(x/2)])
    return y

k = a2.ajuste(F, x, y)
xx = np.linspace(x[0], x[-1], 1000)
yy = k@F(xx)
plt.plot(xx, yy)

# Ajuste de uma cúbica
def F(x):
    y = np.array([x**4,x**3,x**2, x**1, x**0])
    
    return y

k = a2.ajuste(F,x,y)
xx = np.linspace(x[0], x[-1], 1000)
yy = k@F(xx)
plt.plot(xx,yy)

# Polinômio Interpolador
a = a2.interpola(x, y)
print("a",a)
xx = np.linspace(0, 7, 100)
yy = a2.polinomio(a, xx)
plt.plot(xx, yy)

# Spline Cúbico
[a0,b0,c0,d0] = a2.spline(x, y)
a2.plot_sline(x, y)


