import numpy as np
import time
start = time.perf_counter()

cap = 101
ans = (cap-2)**2
print(ans)
for a in range(2,cap):
    for b in range(2,cap):
        if a**b < cap:
            ans += 1 - ((cap-1)//b)
        else:
            break
print(ans)

print(time.perf_counter() - start)
