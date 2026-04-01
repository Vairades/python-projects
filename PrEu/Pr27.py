import time
start = time.perf_counter()
def isp(n):
    if n < 2:
        return False
    elif n < 4:
        return True
    elif n % 2 == 0:
        return False
    elif n < 9:
        return True
    elif n % 3 == 0:
        return False
    else:
        r = int(n**0.5)
        f = 5
        while f <= r:
            if n % f == 0 or n % (f + 2) == 0:
                return False
            f += 6
        return True
def qu(n, a, b):
    return n*n + a*n + b
prime = [2]
for i in range(3,1000,2):
    if isp(i):
        prime.append(i)
ab = []
for b in prime:
    for a in range(2-b,1000):
        p = 1 + a + b
        if isp(p):
            ab.append((a,b))
print(len(ab))
i = 2
while ab:
    lis = [par for par in ab if isp(qu(i, par[0], par[1]))]
    if lis:
        ab = lis
    else:
        break
    i += 1
print(ab,i)
print(ab[0][0]*ab[0][1])
print(time.perf_counter() - start)
