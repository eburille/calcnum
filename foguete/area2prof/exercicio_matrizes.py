import numpy as np
import area2 as a2

A=np.array([[ 1,  2,  3,  4],
            [ 5,  6,  7,  8],
            [ 9, 10, 11, 12],
            [13, 14, 15, 16]])

N1 = a2.Norm_1(A)
N2 = a2.Norm_2(A)
Ninf = a2.Norm_inf(A)

x = np.array([ 1,  2,  3,  4])
n1 = a2.norm_p(x,1)
n2 = a2.norm_p(x,2)
n3 = a2.norm_p(x,3)
ninf = a2.norm_inf(x)





