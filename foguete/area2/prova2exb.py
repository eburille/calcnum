# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 15:58:32 2023

@author: 00325133
"""

import numpy as np
import area2 as a2

A=np.array([[11.,2. ,6. ,5. ],
            [5. ,15.,2. ,4. ],
            [5. ,7., 12.,2. ],
            [1. ,0. ,8. ,17.]])

B=np.array([[2.],
            [6.],
            [4.],
            [9.]])

C=np.linalg.inv(A)


#a=a2.gauss_jacobi(A,B,100)
#print("a",a)

#b=a2.gauss_seidel(A,B,100)
#print("b",b)

c=a2.potencia(C,24)
print(c)