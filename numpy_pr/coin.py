import numpy as np
import time
start = time.perf_counter()

rng = np.random.default_rng()
def prob(n):
    num = 10**n
    mon = rng.integers(2,size=num)
    p = mon.mean()
    print(f"n={num:<8} p={p:.5f} error={abs(p-0.5):.5f}")
for i in range(1,8):
    prob(i)
print(time.perf_counter() - start)
