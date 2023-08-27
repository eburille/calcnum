import numpy as np
import area2 as a2

def f(z):
    x = z[0,0]
    y = z[1,0]
    a = np.array([[ 4*x**3+np.exp(x)*np.exp(-y)],
                  [ 4*y**3-np.exp(x)*np.exp(-y)]])
    return a


def J(z):
    x=z[0,0]
    y=z[1,0]

    a=np.array([[12*x**2+np.exp(x)*np.exp(-y),-np.exp(x)*np.exp(-y)],
                [-np.exp(x)*np.exp(-y),12*y**2+np.exp(x)*np.exp(-y)]])
    return a

z=np.array([[1], [1]])

x=a2.newton(J,f,z,10)




    
    