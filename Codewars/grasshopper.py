def summation(num):
    if num == 1:
        return num
    suum = 1
    add = 2
    for i in range(num-1):
        suum += add
        add += 1
    return suum