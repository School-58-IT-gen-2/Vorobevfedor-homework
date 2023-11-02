def make_sequences(n):
    n = [[n]]
    def main(a):
        first = list(a)
        for x in range(len(a)):
            y = a[x]
            for i in range(y[0]//2):
                a.append([i+1]+y)
        l = []
        for x in a:
            if x not in l:
                l.append(x)
        if first == l:
            return len(l)
        else:
            return main(l)
    return main(n)