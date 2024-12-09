def remove_smallest(numbers):
    mynumbers = numbers.copy()
    if len(mynumbers) > 0:
        mynumbers.remove(min(mynumbers))
        return mynumbers
    return mynumbers