import numpy as np
from matplotlib import pyplot as plt
'''
vantagens:
    Não precisa comecar com intervalos entre raizes
    mais rapido que o metodo dos pontos falsos
    
desvantagens:
    Pode não encontrar raiz

    m = f(x(n)) - f(x(n-1))
        -------------------
           x(n) - x(n-1)
    
           
    x(n+1) = x(n) - f(x(n))   =  x(n) f(x(n-1))  -  x(n-1) f(x(1))
                    -------      ---------------------------------
                       m                 f(x(n)) - f(x(n-1))
'''

def newtinho(f, df, a, N, e1, e2, e3):
    pa = a

    for i in range(N):
        if df(a) == 0:
            return(p)

        p = a - f(a) / df(a)

        a = p

        if abs(f(p)) <= e1:
            print(f'parei aqui 1 - i = {i}')
            break

        if abs(p - pa) <= e2:
            print(f'parei aqui 2 - i = {i}')
            break

        if abs((p-pa) / p) <= e3:
            print(f'parei aqui 3 - i = {i}')
            break
    return p    

def secante(f, a, b, N, e1, e2, e3):
    pa = a
    for i in range(N):
        if (f(b) - f(a)) == 0:
            return p
        p = (a*f(b) - b*f(a)) / (f(b) - f(a))

        b = a
        a = p

        if abs(f(p)) <= e1:
            print(f'parei aqui 1 - i = {i}')
            break

        if abs(p - pa) <= e2:
            print(f'parei aqui 2 - i = {i}')
            break

        if abs((p-pa) / p) <= e3:
            print(f'parei aqui 3 - i = {i}')
            break

    return p

def f(x):
    y = np.log(x) + x
    return y

def df(x):
    y = 1/x + 1
    return y

if __name__ == '__main__':
    print(f(0.5074741254118916))

    a = 0.49
    b = 0.52
    x = np.linspace(a, b, 100000)
    plt.plot([a,b], [0, 0])
    plt.plot(x, f(x))

    '''          f, a, b,   N,   e1, e2, e3'''
    z3 = secante(f, a, b, 100, 0,  0, 0)
    '''          f,  df  a,   N,   e1, e2, e3'''
    z4 = newtinho(f, df, a, 100, 0,  0,  0)
    print(f'''Método secante = {z3},
Método do noewtinho = {z4}''')

    plt.show()