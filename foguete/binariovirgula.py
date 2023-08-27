# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 01:59:46 2023

@author: Mariana
"""

from decimal import Decimal

def decimal_para_binario(numero):
    numero_decimal = Decimal(numero)
    inteiro = int(numero_decimal)
    fracionario = numero_decimal - inteiro
    
    parte_inteira_binaria = bin(inteiro)[2:]
    
    parte_fracionaria_binaria = ""
    while fracionario > 0:
        fracionario *= 2
        bit = int(fracionario)
        parte_fracionaria_binaria += str(bit)
        fracionario -= bit
    
    binario_resultante = parte_inteira_binaria
    if parte_fracionaria_binaria:
        binario_resultante += "." + parte_fracionaria_binaria
    
    return binario_resultante

# Exemplo de uso
numero_decimal = 55.56
binario_resultante = decimal_para_binario(numero_decimal)
print(binario_resultante)