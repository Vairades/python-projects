import math
def primes(x):
    n = 2
    ans = []
    while x != 1:
        if x % n == 0:
            ans.append(n)
            x = x//n
            n = 1
        n = n+1
    return ans
i = 2
rez = []
while i < 21:
    pr = primes(i)
    j = 0
    while j < len(rez):
        k = 0
        while k < len(pr):
            if rez[j] == pr[k]:
                del pr[k]
                break
            k = k+1
        j = j+1
    print()
    print(i,rez,pr)
    rez = sorted(rez + pr)
    i = i+1
print(sorted(rez))
print(math.prod(rez))
