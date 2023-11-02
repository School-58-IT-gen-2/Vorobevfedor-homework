def min_and_max(l, d, x):
    e = []
    for i in range(l, d+1):
        v = 0
        for y in str(i):
            v += int(y)
        if v == x:
            e.append(i)
            break;
    for i in range(d, l, -1):
        v = 0
        for y in str(i):
            v += int(y)
        if v == x:
            e.append(i)
            break;
    return e