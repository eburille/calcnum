import numpy as np

def met_p_med(f, a, b, N):
    h = (b-a)/N
    area_tot = 0
    for i in range(1, N):
        area = f(a + h/2 * (2*i - 1))
        area_tot += area
    integral = h * area_tot
    return integral

def met_trapezio(f, a, b, N):
    h = (b-a)/N
    area_tot = 0
    for i in range(N-1):
        area = f(a + h*i)
        area_tot += area
    integral = h * ( (f(a)+f(b))/ 2  + area_tot)
    return integral

def f(x):
    y = (np.exp(-(np.tan(x)**2)) * np.tan(x)**2)   /   2
    return y

if __name__ == '__main__':
    a = -np.pi / 2
    b = np.pi / 2
    N = 1000000

    integral_p_med = met_p_med(f, a, b, N)
    integral_met_trapezio = met_trapezio(f, a, b, N)
    print(integral_p_med)
    print(integral_met_trapezio)