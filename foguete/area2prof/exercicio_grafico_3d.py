import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d, Axes3D 

fig = plt.figure(figsize = (12,10))
ax = Axes3D(fig) 

x = np.arange(-10, 10, 0.05)
y = np.arange(-10, 10, 0.05)

X, Y = np.meshgrid(x, y)
Z = (X**2+Y**2+X*Y)/100+np.sin(X)+np.sin(Y)
cset = ax.plot_surface(X, Y, Z)
plt.show()