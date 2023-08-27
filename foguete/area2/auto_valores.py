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



A = np.array([[6, 4, 6,  8],
              [0, 2, 6,  0],
              [9, 0, -5, 0],
              [0, 0, 3,  4]])

def menor_auto_valor(A, N):
    primeiro_auto_valor, x = potencia_maior(A, N)

    A_descontado = A - primeiro_auto_valor * np.eye(A.shape[0])
    print('a descontado', A_descontado)
    seg_aut_val, x = potencia_maior(A_descontado, N) 

    return seg_aut_val + primeiro_auto_valor, x

def segundo_maior(A, N):
    primeiro_auto_valor, x = potencia_menor(A, N)

    A_descontado = A - primeiro_auto_valor * np.eye(A.shape[0])
    seg_aut_val, x = potencia_maior(A_descontado, N) 

    return seg_aut_val + primeiro_auto_valor, x

auto_valores, auto_vetores  = np.linalg.eig(A)

auto_valores_potencia, x = segundo_maior(A, 1000)
aut_val_pot_menor, x = potencia_menor(A, 1000)
aut_val_pot_maior, x = potencia_maior(A, 1000)
aut_val_menor, x = menor_auto_valor(A, 1000)

print(A)

print(" auto valores,    2°   pot>, pot<,  <")
print(auto_valores ,auto_valores_potencia, aut_val_pot_maior, aut_val_pot_menor, aut_val_menor)