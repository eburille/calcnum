import numpy as np

def gauss_jacobi(A, B, N):
    m = A.shape[0]
    U = np.triu(A,1)
    L = np.tril(A, -1)
    D = np.tril(np.triu(A))
    C = -np.linalg.inv(D)@(L+U)

    print('Norma de C: ', np.linalg.norm(C))
    E = np.linalg.inv(D)@B
    x = np.zeros((m, 1))
    for i in range(N) :
        x = C@x+E
    return x

def gauss_seidel(A, B, N):
    m = A.shape[0]
    U = np.triu(A,1)
    L = np.tril(A, -1)
    D = np.tril(np.triu(A))
    Cs = -np.linalg.inv(D+L)@(U)

    print('Norma de C: ', np.linalg.norm(Cs))
    Es = np.linalg.inv(D)@B
    x = np.zeros((m, 1))
    for i in range(N) :
        xa=x
        x = Cs@x+Es

    nc = np.linalg.norm(Cs)
    erro = nc/(1-nc)*np.linalg.norm(x-xa)

    return x

matriz = np.matrix([[1, 1, 1], [2, 1, -1], [2, 2, 1]])
Outra_coisa = [1, 0, 1]

xs = np.linalg.solve(matriz, Outra_coisa)
x1 = gauss_jacobi(matriz, Outra_coisa, 100)

print(x1)

erro = np.linalg.norm(xs-x1)