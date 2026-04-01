import numpy as np

f = [1,2]
while f[-1] < 4000000:
    f.append(f[-1]+f[-2])
ans = 0
i = 0
while 1 + 3*i < len(f):
    ans = ans + f[1 + 3*i]
    i = i+1
print(ans)
