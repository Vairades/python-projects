import time
start = time.perf_counter()

#Считает сумму всех делителей всех чисел до lim
lim = 30000
sud = [0]*lim
for i in range(1, lim//2 + 1):
    for j in range(2*i, lim, i):
        sud[j] += i
prof = []
for i in range(len(sud)):
    if i < sud[i]:
        prof.append(i)
up = 28123
