import numpy as np
import matplotlib.pyplot as plt
from equacoes import achar_intervalos

def achar_raizes(lista_intervalos: list, f, N: int, e1: float, e2: float, e3: float) -> list:
    lista_raizes = []
    for intervalo in lista_intervalos:
        a = intervalo[0]
        pa = a
        b = intervalo[1]
        p = (a*f(b) - b*f(a)) / (f(b) - f(a))
        i=0
        #print(f(p))
        x = np.linspace(a, b, 100)
        while i < N:
            #print(f'p = {p}, f(p) = {f(p)}')
            if f(p)*f(a) > 0:
                a = p
                p = (a*f(b) - b*f(a)) / (f(b) - f(a))
            else:
                b = p
                p = (a*f(b) - b*f(a)) / (f(b) - f(a))

            plt.plot([a, b], [f(a), f(b)])
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
    y = (x-4)**2 - e**(x/10)
    return y


if __name__ == '__main__':
    a = -100
    b = 100
    x = np.linspace(a, b, 100000)

    intervalos = achar_intervalos(a, b, f, x)
    print(intervalos)
    raizes = achar_raizes(intervalos, f, 100, 0, 0, 0)
    print(raizes)

    plt.plot([a,b], [0, 0])

    for raiz in raizes:
        plt.plot([raiz, raiz], [f(a), f(b)])

    plt.plot(x, f(x))
    plt.show()
