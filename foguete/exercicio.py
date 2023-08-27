import numpy as np
import bibliotca as bib

def f(x):
    y=2*x-2*np.exp(-2*x)
    return y

#def df(x):
    #y=1/15+np.sin(x)
    #return y

x1 = bib.bissecao(f,0.5,1,1000,0,0,0)
x2 = bib.posicao_falsa(f,0.5,5,1000,0,0,0)
x3 = bib.secante(f,1,2,1000,0,0,0)
#x4 = bib.newton(f,df,0.5,1000,0,0,0)

