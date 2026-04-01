import time
start = time.perf_counter()

#Считает сумму всех делителей всех чисел до lim
lim = 1000001
sud = [0]*lim
for i in range(1, lim//2 + 1):
    for j in range(2*i, lim, i):
        sud[j] += i

orb = {1:[1]}
seen = set()
def orbit(n):
    """находит цепочку сумм всех множителей не считая n"""
    if n in orb:
        return orb[n]
    elif n > 1000000:
        return []
    if n not in seen:
        seen.add(n)
        orb[n] = [n] + orbit(sud[n])
        return orb[n]
    else:
        return [n]
lon = 3
num = 1
for i in range(5,1000001):
    li = orbit(i)
    if (len(li) > lon) and (li[0] == li[-1]):
        lon = len(li)
        num = i
        print(num, lon, li)
print(time.perf_counter() - start)
