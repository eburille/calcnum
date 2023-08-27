import matplotlib.pyplot as plt
import numpy as np

def f(x):
    y=x**2*np.exp(x)-np.exp(x)
    return y

x = np.linspace(-5,1.5,1000)

plt.plot(x,f(x))




