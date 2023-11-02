def fibs_fizz_buzz(n):
    l = 1
    k = 1
    if n == 0:
        arr = [0]
    elif n > 0 and n < 2:
        arr = [1]
    elif n >= 2:
        arr = [1, 1]
    for i in range(n-2):
        k, l = k+l, k
        if k % 3 == 0:
            if k % 5 == 0:
                arr.append('FizzBuzz')
            else:
                arr.append('Fizz')
        elif k % 5 == 0:
            arr.append('Buzz')
        else:
            arr.append(k)    
    return arr
    