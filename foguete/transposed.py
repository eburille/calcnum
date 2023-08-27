import numpy as np

A = np.array([[1, 0, 2],
          [4, 7, -3],
          [0, -5, 4]])

b = A@np.transpose(A)

print(b)