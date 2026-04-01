import time
start = time.perf_counter()
a = 2**1000
ans = 0
while a > 0:
    ans = ans + a % 10
    a = a // 10
print(ans)
