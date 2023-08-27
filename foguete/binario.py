# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def decimalparabinario(decimal):
    if decimal == 0:
        return'0'
        
    binario = ''
    while decimal>0:
        resto = decimal%2
        binario = str(resto)+binario
        decimal = decimal//2
        
    return binario

numdecimal=136
numbinario = decimalparabinario(numdecimal)
print(numbinario)






