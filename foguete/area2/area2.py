import numpy as np

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
    return max(np.sum(A, axis=0))

def Norm_inf(A):
    return max(np.sum(A, axis=1))

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
    for i in range(10):
        h=np.linalg.solve(J(z),-f(z))   
        x=z+h
        z=x
    
    return x


def alg_grad(gradiente,N,x):
    gamma=0.00001
    for i in range(N):
        x=x-gamma*gradiente(x)
    return x

def ajuste(funcao,x,y):
    PHI=funcao(x)
    return np.linalg.solve(PHI@PHI.T,PHI@y)