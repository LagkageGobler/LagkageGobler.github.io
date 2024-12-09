def odd_or_even(arr):
    suum = sum(arr)
    if suum % 2 == 0:
        return "even"
    elif suum % 2 == 1:
        return "odd"