import time
start = time.perf_counter()
def d(n):
    """находит сумму всех множителей"""
    ans = 1
    k = 2
    while k < n**0.5:
        if n % k == 0:
            ans = ans + k + n//k
        k = k+1
    if k*k == n:
        ans = ans + k
    return ans

orb = {1:[1]}
def orbit(n):
    """находит цепочку сумм всех множителей не считая n"""
    if n in orb:
        return orb[n]
    #import pdb; pdb.set_trace()
    path = []
    x = n
    while (x not in path) and (x not in orb):
        path.append(x)
        x = d(x)
    if x in orb:
        orb[n] = path + orb[x]
    else:
        orb[n] = path
    return orb[n]

seen = set()
ans = 0
for i in range(2,10001):
    if i not in seen:
        a = d(i)
        if (a != i) and (i == d(a)):
            ans = ans+i
            seen.add(i)
            if a not in seen:
                ans = ans+a
                seen.add(a)
print(ans)

print(orbit(10))
#for i in range(1,100):
#    li = orbit(i)
#    if (len(li) == 2) and (li[-1] != 1) and (li[-1] != li[-2]):
#        print(li)
#print(ami,round(time.perf_counter()-start,2))
