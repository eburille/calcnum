import area2 as a2

def gradiente(z):
    x=z[0][0]
    y=z[1][0]
    
    g=np.array([[4*x**3],
                [4*y**3]])
    
    return g

def jacobiano(z):
    x=z[0][0]
    y=z[1][0]
    
    g=np.array([[12*x**2,0],
                [0,12*y**2]])
    
    return g


x0=np.array([[2],
            [2]])

minimo=a2.alg_grad1(gradiente,64,x0)
print(minimo)

minimo2=a2.newton(jacobiano,gradiente,x0,64)
print(minimo2)
