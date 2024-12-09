def fake_bin(x):
    result = ''
    for c in x:
        print(c)
        if int(c) < 5:
            result += '0'
        else:
            result += '1'
        
    return result
    #     return ''.join('0' if int(d) < 5 else '1' for d in x)
        