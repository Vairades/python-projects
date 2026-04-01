import time
start = time.perf_counter()
n = 999999
ans = [1,1]
while n > 1:
    i = 1
    t = n
    while t != 1:
        if t % 2 == 0:
            t = t//2
        else:
            t = 3*t+1
        i = i+1
    if i > ans[1]:
        ans = [n,i]
    n = n-1
print(ans,round(time.perf_counter()-start,2))
