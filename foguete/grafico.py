import matplotlib.pyplot as plt
import numpy as np

def f(x):
    y=np.log(x)+5*np.exp(-x/5)-np.sqrt(x)/10-3
    return y

x = np.linspace(-20,20,1000)

plt.plot(x,f(x))
plt.plot([0,100],[0,0])



