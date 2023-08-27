import numpy as np

def f(x):
    return np.sin(x)

def integral(f,A,x):
    n=x.size
    I=0
    for i in range(n):
        I=I+A[i]*f(x[i])
    return I

def calculaA(x):
    n=x.size
    A=np.zeros((n,n))
    B=np.zeros((n,1))
    for i in range(n):
        A[i,:]=x**i
        if(i%2==0):
            B[i]=2/(i+1)
    x=np.linalg.solve(A,B)            
    return x

def integral_generica(f,x,a,b):
    A=calculaA(x)
    t=(b+a)/2+(b-a)/2*x
    I=(b-a)/2*f(t)@A
    return I      
      
x = np.array([-np.sqrt(3/5), 0, np.sqrt(3/5)])
[x,A] = np.polynomial.legendre.leggauss(5)
I = integral_generica(f,x,0,2*np.pi)
print(I)