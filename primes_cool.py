def nu(n,k):
    i = 0
    while n%k == 0:
        n = n//k
        i = i+1
    return (n,i)

def primum(n):
    v = {}
    if n%2 == 0:
        n, v[2] = nu(n,2)
    k = 1
    while n > 1:
        k = k+2
        if n%k == 0:
            n, v[k] = nu(n,k)
        elif k > n**0.5:
            n, v[k] = (1,1)
    return v
