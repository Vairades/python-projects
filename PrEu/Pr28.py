import time
start = time.perf_counter()

ans = 1
la = 1
i = 1
lim = 501
while i < lim:
    ans += 20*i + 4*la
    la += 8*i
    i += 1
print(ans)

print(time.perf_counter() - start)
