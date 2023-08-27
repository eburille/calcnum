import numpy as np
import area2 as a2

A = np.array([[6.,-2.,4.],
              [5.,-3.,5.],
              [4.,-4.,4.]])

B = np.array([[14.],
              [14.],
              [8.]])

xs = np.linalg.solve(A,B)
x1 = a2.gauss(A,B)
x2 = a2.gauss_jacobi(A,B,100)
x3 = a2.gauss_seidel(A,B,100)

e1=np.linalg.norm(xs-x1)
e2=np.linalg.norm(xs-x2)
e3=np.linalg.norm(xs-x3)



