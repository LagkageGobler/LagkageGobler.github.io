def find_next_square(sq):
    import math
    sqr = math.sqrt(sq)
    if int(sqr) == sqr:
        sqr += 1
        return sqr * sqr
    return -1