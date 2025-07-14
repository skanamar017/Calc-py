def bin_float_to_dec(num):
    if '.' not in num:
        return int(num, 2)

    int_part, frac_part = num.split('.')

    # Convert the integer part
    dec_int = int(int_part, 2)

    # Convert the fractional part
    dec_frac = 0
    for i, digit in enumerate(frac_part):
        dec_frac += int(digit) * (2 ** -(i + 1))

    return dec_int + dec_frac

def oct_float_to_dec(num):
    if '.' not in num:
        return int(num, 8)

    int_part, frac_part = num.split('.')

    # Convert the integer part
    dec_int = int(int_part, 8)

    # Convert the fractional part
    dec_frac = 0
    for i, digit in enumerate(frac_part):
        dec_frac += int(digit) * (8 ** -(i + 1))

    return dec_int + dec_frac

def hex_float_to_dec(num):
    if '.' not in num:
        return int(num, 16)

    int_part, frac_part = num.split('.')

    # Convert the integer part
    dec_int = int(int_part, 16)

    # Convert the fractional part
    dec_frac = 0
    for i, digit in enumerate(frac_part):
        dec_frac += int(digit) * (16 ** -(i + 1))

    return dec_int + dec_frac
