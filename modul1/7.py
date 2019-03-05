import functools
import operator

def faktorPrima(n):
    n_ori = n
    pri = []
    st = True
    while st:
        for i in range(2, n+1):
            if n/i == int(n/i):
                pri.append(i)
                n = int(n/i)
                break
        if functools.reduce(operator.mul, pri, 1) == n_ori:
            st = False
    return pri

print(faktorPrima(10))
print(faktorPrima(120))
print(faktorPrima(19))
