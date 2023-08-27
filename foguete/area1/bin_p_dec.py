def bin_p_dec(x: str):
    parte_inteira = int(x//1)
    parte_decimal =  (str(x).split('.')[-1])
    print(parte_decimal)

    decimal = 0
    for i, a in enumerate(str(parte_inteira)):
        decimal = decimal + int(a) * 2 ** (len(str(parte_inteira)) - i -1)
    
    for i, a in enumerate(str(parte_decimal)):

        decimal = decimal + int(a) * 2 ** (-i - 1)
    
    return decimal
    
print(bin_p_dec(float(10100)))
