# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 16:19:15 2023

@author: 00325133
"""

import numpy as np
import matplotlib.pyplot as plt
import area2 as a2

A= np.array([[5, 6],
             [6, 7]])

B=np.linalg.inv(A)
print(B)

norm1 = np.linalg.norm(A, ord=np.inf)
print(norm1)

norm2 = np.linalg.norm(B, ord=np.inf)
print(norm2)