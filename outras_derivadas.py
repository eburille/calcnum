import numpy as np

def newton(J,f,z,N):
    for i in range(N):
        h=np.linalg.solve(J(z),-f(z))
        x=z+h
        z=x
    return x

def alg_grad1(gradiente,N,x):
    gamma=0.1
    for i in range(N):
        x=x-gamma*gradiente(x)/np.linalg.norm(gradiente(x),2)
    return x

def dif_progressiva3(f, x, h):
    df = (-3*f(x)+4*f(x+h)-f(x+2*h))/(2*h)
    return df

def dif2(f, x, h):
    df = (f(x-h)-2*f(x)+f(x+h))/(h**2) [:, 0]
    return df

def jacobiano(F, x, h):
    n = x.size
    m=F(x).size
    J = np.zeros((m,n))
    for i in range(2):
        H = np.zeros((n,1))

        J[:, i] = (F(x+H)-F(x-H)) / (2*h)
        a = i
    return J

def F(x):
    x1 = x[0][0]
    x2 = x[1][0]
    y = np.array([
        [np.sin(x1) + np.cos(x2) - 1],
        [np.sin(x1) - np.cos(x2) - 1]
    ])
    return y

def f(x):
    x1 = x[0,0]
    x2 = x[1,0]
    e = np.e
    y = np.exp(x1) * np.exp(x2)
    return np.array([[y]])

h = 0.000001
x = np.array([[1], [2]])
y = F(x)

jacobsen = jacobiano(f, x, h)
print(jacobsen)

min = newton(jacobsen, f, x, 100)

print(min)