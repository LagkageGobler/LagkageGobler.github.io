def is_triangle(a, b, c):
    arr = [a,b,c]
    arr.sort()
    if arr[2] < arr[1]+arr[0]:
        return True
    else:
        return False