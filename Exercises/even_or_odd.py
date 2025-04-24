def even_or_odd(num):
    # My perfomed an AND operation since for a number to be odd, the least significant bit has to be set
    # as it is in the ones position.
    if num & 0x1 == 0:
        return "Even"
    else:
        return "Odd"
