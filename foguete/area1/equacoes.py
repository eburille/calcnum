import numpy as np
import matplotlib.pyplot as plt

def achar_intervalos(a, b, f, linspace) -> list:
    lista_valores = linspace
    intervalos = []
    watch_dog = a
    for x in lista_valores:
        if f(watch_dog) * f(x) <= 0:
            intervalos.append((watch_dog, x))
        watch_dog = x
    return intervalos

def achar_ponto_mais_proximo(a, b, f, linspace) -> tuple:
    lista_valores = linspace
    watch_dog = float('inf')
    for x in lista_valores:
        d = (x**2 + f(x)**2)**0.5
        if d < watch_dog:
            watch_dog = d
    return (watch_dog, f(watch_dog))

def achar_raizes(lista_intervalos: list, f, N: int, e1: float, e2: float, e3: float) -> list:
    lista_raizes = []
    for intervalo in lista_intervalos:
        a = intervalo[0]
        pa = a 
        b = intervalo[1]
        p = (a+b) / 2
        i=0
        #print(f(p))
        while i < N:
            #print(f'p = {p}, f(p) = {f(p)}')
            if f(p)*f(a) > 0:
                a = p
                p = (a+b) / 2
            else:
                b = p
                p = (a+b) / 2
            i = i+1

            if abs(f(p)) <= e1:
                print(f'parei aqui 1 - i = {i}')
                break

            if abs(p - pa) <= e2:
                print(f'parei aqui 2 - i = {i}')
                break

            if abs((p-pa) / p) <= e3:
                print(f'parei aqui 3 - i = {i}')
                break
        lista_raizes.append(p)
    return lista_raizes

def f(x):
    e = np.e
    pi = np.pi
    y = x/15 - np.cos(x)
    return y

if __name__ == '__main__':
    a = -20
    b = 20
    x = np.linspace(a, b, 99999)
    
    plt.plot([a,b], [0, 0])
    plt.plot(x, f(x))
    
    p = achar_ponto_mais_proximo(a, b, f, x)
    print('ponto mais próximo (x, y) = ', p)

    intervalos = achar_intervalos(a, b, f, x)
    print(intervalos)
    print('numero de intervalos = ', len(intervalos))
    '''                     a, b,     f,   N,  e1, e2, e3'''
    raizes = achar_raizes(intervalos, f, 1000, 0,  0,  0)
    print('raízes = ', raizes)
    prod = 1
    for raiz in raizes:
        prod = prod * raiz
        print(f(raiz))
    
    print('prod: ', prod)
    
    plt.show()