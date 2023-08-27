import numpy as np

def potencia_menor(A, N):
    inversa = np.linalg.inv(A)
    l, x = potencia_maior(inversa, N)

    return 1/l, x

def potencia_maior(A, N):
    x = np.random.rand(A.shape[0])
    for i in range(N):
        v = A@x
        x = v/ np.linalg.norm(v)
    
    l = np.transpose(x)@A@x

    return l, x

A = np.array([[7, 0, 0, 1],
             [0, 3, 0, 0],
             [0, 0, 2, 0],
             [1, 1, 1, -5]])

A = np.array([[-6, 0, 0, 0],
              [0, 2, 0, 0],
              [0, 0, 5, 0],
              [0, 0, 0, 4]])



def menor_auto_valor(A, N):
    primeiro_auto_valor, x = potencia_maior(A, N)
    A_descontado = A - primeiro_auto_valor * np.eye(A.shape[0])
    seg_aut_val, x = potencia_maior(A_descontado, N) 

    return seg_aut_val + primeiro_auto_valor, x

def segundo_maior(A, N):

    menor,x = potencia_menor(A, N)
    inversa = np.linalg.inv(A)
    inv_desc = inversa - menor * np.eye(inversa.shape[0])

    seg, x = potencia_maior(inv_desc, N)
    seg = seg + menor

    return 1/seg, x

auto_valores, auto_vetores  = np.linalg.eig(A)

segundo_aut, x = segundo_maior(A, 1000)
aut_val_pot_menor, x = potencia_menor(A@A, 1000)
aut_val_pot_maior, auto_vetor = potencia_maior(A, 1000)
aut_val_menor, x = menor_auto_valor(A, 1000)

print(A)

print('auto valores', auto_valores)
print(segundo_aut)
