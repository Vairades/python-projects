import time
start = time.perf_counter()
def f(n):
    i = 1
    a = 1
    while i <= n:
        a = a*i
        i = i+1
    return a
ans = 0
p = f(100)
while p > 0:
    ans = ans + p % 10
    p = p // 10
print(ans,round(time.perf_counter()-start,2))
