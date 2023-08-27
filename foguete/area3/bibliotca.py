import numpy as np

def bissecao(f,a,b,N,e1,e2,e3):
    print("Método da Bisseção:")
    pa=a
    for i in range(N):
        p=(a+b)/2
          
        print("i",i,"p",f"{p:.6}")

        if(f(a)*f(p)>0):
            a=p
        else:
            b=p
            
        if abs(f(p))<=e1: 
            print("Parou - |f(x)|<e1")
            break

        if abs(p-pa)<=e2: 
            print("Parou - |x(i)-x(i-1)|<e2")
            break

        if abs((p-pa)/p)<=e3:
            print("Parou - |x(i)-x(i-1)|/|x(i)|<e3")
            break
        
        pa=p
        
    return p
 
def posicao_falsa(f,a,b,N,e1,e2,e3):
    print("Método da Posição Falsa:")
    pa=a
    for i in range(N):
        p=(a*f(b)-b*f(a))/(f(b)-f(a))
        
        print("i",i,"p",f"{p:.6}")
        
        if(f(a)*f(p)>0):
            a=p
        else:
            b=p
            
        if abs(f(p))<=e1: 
            print("Parou - |f(x)|<e1")
            break

        if abs(p-pa)<=e2: 
            print("Parou - |x(i)-x(i-1)|<e2")
            break

        if abs((p-pa)/p)<=e3:
            print("Parou - |x(i)-x(i-1)|/|x(i)|<e3")
            break
        
        pa=p

    return p 

def secante(f,a,b,N,e1,e2,e3):
    print("Método da Secante:")
    pa=a
    for i in range(N):
        p=(a*f(b)-b*f(a))/(f(b)-f(a))
        
        print("i",i,"p",f"{p:.6}")

        b=a
        a=p        
            
        if abs(f(p))<=e1: 
            print("Parou - |f(x)|<e1")
            break

        if abs(p-pa)<=e2: 
            print("Parou - |x(i)-x(i-1)|<e2")
            break

        if abs((p-pa)/p)<=e3:
            print("Parou - |x(i)-x(i-1)|/|x(i)|<e3")
            break
        
        pa=p

    return p 

def newton(f,df,a,N,e1,e2,e3):
    print("Método de Newton:")
    pa=a
    for i in range(N):
        p=a-f(a)/df(a)
        
        print("i",i,"p",f"{p:.6}")

        a=p        
            
        if abs(f(p))<=e1: 
            print("Parou - |f(x)|<e1")
            break

        if abs(p-pa)<=e2: 
            print("Parou - |x(i)-x(i-1)|<e2")
            break

        if abs((p-pa)/p)<=e3:
            print("Parou - |x(i)-x(i-1)|/|x(i)|<e3")
            break
        
        pa=p

    return p 

