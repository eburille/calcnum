import matplotlib.pyplot as plt
import numpy as np
from math import factorial

def f1(x):
    y = 1 -x**2/2 + x**4/24
    return y

def f2(x):
    y = 1 -x**2/2 + x**6/720
    return y

def R(x):
    y = x**5/factorial(5)
    return y

def erro(x):
    y = np.cos(x) - f1(x)
    return y

x = np.linspace(-5, 5, 1000)

plt.plot(x, np.cos(x))
plt.plot(x, f1(x))
plt.plot(x, f2(x))

plt.show()