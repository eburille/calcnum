def dec_p_bin(x):
    parte_inteira = int(x//1)
    parte_decimal = float('0.' + (str(x).split('.')[-1]))
    nums = ''
    print(parte_decimal)
    if parte_inteira == 0:
        nums = '0'

    while parte_inteira > 0:
        if parte_inteira%2 == 1:
            nums = str(parte_inteira%2) + nums
        else:
            nums = str(0) + nums
        parte_inteira = parte_inteira//2

    nums = nums + ','
    i=0
    while parte_decimal != 0 and i < 20:
        if parte_decimal*2 >= 1:
            nums = nums + '1'
            parte_decimal = parte_decimal*2 - 1
        else:
            nums = nums + '0'
            parte_decimal = parte_decimal * 2
        i=i+1

    return nums

print(dec_p_bin(float(22.22)))