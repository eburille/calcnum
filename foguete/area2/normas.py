import numpy as np
def calcula_norma(matriz, indice):
    r = 0
    for num in matriz:
        r = r + num**indice
    r = r**(1/indice)
    return r

# Example usage:
#matriz = np.array([[1],
#                   [2],
 #                  [3]])


#inversa= np.linalg.inv(matriz)

vetor = [1, 2, 3]

norm = np.linalg.norm(vetor, ord=5)
print('norm: ', norm)

#norma = np.linalg.norm(inversa, ord=1)
#print('norm: ', norma)

#k=norm*norma
#print("k",k)
#norma = calcula_norma(vetor, np.inf)
#print(norma)