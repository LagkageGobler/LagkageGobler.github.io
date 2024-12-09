def number(lines):
    length = len(lines)
    x = 1
    for i in range(length):
        add = lines[0-1+x]
        del lines[0-1+x]
        lines.insert(0-1+x, str(x)+": "+add)
        x += 1
    return lines