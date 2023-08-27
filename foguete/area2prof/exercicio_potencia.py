import numpy as np
import area2 as a2

A = np.array([[150, 0, 0],
              [0,  -90, 0],
              [0,  0, -12]])

# Todos Autovalores
w1, v1=np.linalg.eig(A)

# Maior Autovalor em valor absoluto
w2, v2 = a2.potencia(A,200)
print(w2,v2)

#Menor Autovalor em valor absoluto
w3,v3 = a2.potencia(np.linalg.inv(A),200)
w3 = 1/w3
print(w3)

#Menor Autovalor (oposto do maior)
w4,v4 = a2.potencia(A-w2*np.eye(3),200)
w4 = w4+w2
print(w4)

# Segundo Maior Autovalor em valor absoluto
v2.shape = (3,1)
B = A-w2*v2@np.transpose(v2)
w5,v5 = a2.potencia(B,100)

# Terceiro Maior Autovalor em valor absoluto
v5.shape = (3,1)
C = B-u5*v5@np.transpose(v5)
w6,v6 = a2.potencia(C,100)