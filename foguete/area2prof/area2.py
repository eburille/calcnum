import numpy as np
import matplotlib.pyplot as plt

def gauss(A,y):
    X=np.concatenate((A,y),axis=1)
    linhas = X.shape[0]
    colunas = X.shape[1]

    for i in range(1,linhas):
        for j in range(i):
            X[i,:]=X[i,:]-X[j,:]*X[i,j]/X[j,j]
                
    Z = triangular(X[:,0:colunas-1],X[:,-1])
    return Z
    
def triangular(A,y):
    print(A)
    linhas = A.shape[0]
    x=np.zeros((linhas,1))
    for i in range(linhas-1,-1,-1):
        x[i]=(y[i]-A[i,:]@x)/A[i,i]
    return x


def norm_p(x,p):
    return (sum(abs(x)**p))**(1/p)

def norm_inf(x):
    return max(abs(x))

def Norm_1(A):
    return max(np.sum(np.abs(A), axis=0))

def Norm_inf(A):
    return max(np.sum(np.abs(A), axis=1))

def Norm_2(A):
    a,b=np.linalg.eig(A@np.transpose(A))
    return np.sqrt(max(a))

def gauss_jacobi(A,B,N):
    m=A.shape[0]
    U = np.triu(A,1)
    L = np.tril(A,-1)
    D = np.tril(np.triu(A))
    C = -np.linalg.inv(D)@(L+U)
    print("a norma de C é",np.linalg.norm(C))
    E = np.linalg.inv(D)@B
    x = np.zeros((m,1))
    for i in range(N):
        xa=x
        x=C@x+E
    
    nc=np.linalg.norm(C)
    erro=nc/(1-nc)*np.linalg.norm(x-xa)
    print("O erro é menor que",erro)
    return x
    
def gauss_seidel(A,B,N):
    m=A.shape[0]
    U = np.triu(A,1)
    L = np.tril(A,-1)
    D = np.tril(np.triu(A))
    Cs = -np.linalg.inv(D+L)@(U)
    print("a norma de Cs é",np.linalg.norm(Cs))
    Es = np.linalg.inv(D+L)@B
    x = np.zeros((m,1))
    for i in range(N):
        xa=x
        x=Cs@x+Es
    
    
    nc=np.linalg.norm(Cs)
    erro=nc/(1-nc)*np.linalg.norm(x-xa)
    print("O erro é menor que",erro)
    return x    
    
def potencia(A,N):
    x= np.random.rand(A.shape[0])
    for i in range(N):
        v=A@x
        x=v/np.linalg.norm(v)
    l=np.transpose(x)@A@x
    return l,x
    
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
    
def alg_grad2(gradiente,N,x):
    gamma=0.1
    for i in range(N):
        x=x-gamma*gradiente(x)
    return x
 
def ajuste(funcao,x,y):
    PHI=funcao(x)
    return np.linalg.solve(PHI@PHI.T,PHI@y)

def polinomio(a,x):
    n=a.size
    m=x.size
    y=np.zeros(m)
    for i in range(n):
        y=y+a[i]*x**(n-i-1)
    return y

def polinomio2(a,x0,x):
    n=a.size
    m=x.size
    y=np.zeros(m)
    for i in range(n):
        y=y+a[i]*(x-x0)**(i)
    return y


def interpola(x,y):
    m=x.size
    A=np.zeros((m,m))
    for i in range(m):
        A[:,m-1-i]=x**i
    return np.linalg.solve(A,y)

def spline(x,y):

    h=x[1:]-x[0:-1]
    n=x.size
    A=np.zeros((n,n))
    B=np.zeros((n,1))
    A[0,0]=1
    A[-1,-1]=1
    for i in range(1,n-1):
        A[i,i-1]=h[i-1]
        A[i,i]=2*h[i-1]+2*h[i]
        A[i,i+1]=h[i]
        B[i]=3*(y[i+1]-y[i])/h[i]-3*(y[i]-y[i-1])/h[i]
    
    c=np.linalg.solve(A,B)
    a=y

    a0 = np.zeros(n-1)
    b0 = np.zeros(n-1)
    c0 = np.zeros(n-1)
    d0 = np.zeros(n-1)
    
    for j in range(n-1):
        a0[j]=a[j]  
        b0[j]=(3*y[j+1]-3*y[j]-2*c[j]*h[j]**2-c[j+1]*h[j]**2)/(3*h[j])
        c0[j]=c[j]
        d0[j]=(c[j+1]-c[j])/(3*h[j])

    return [a0,b0,c0,d0]

def plot_sline(x,y):
    [a0,b0,c0,d0] = spline(x,y)
    for j in range(x.size-1):
        xx=np.linspace(x[j],x[j+1],100)
        yy=polinomio2(np.array([a0[j],b0[j],c0[j],d0[j]]),x[j],xx)
        plt.plot(xx,yy)

