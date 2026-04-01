import numpy as np
import math

a = np.array([(2*i+1)**2 for i in range(6)])
print(a)
b = np.zeros(len(a))
c = np.zeros(6*len(a)).reshape(6,len(a))
for i in range(len(a)):
    b[i] = b[i-1] + a[i]

for j in range(c.shape[1]):
    c[0,j] = b[j]
for j in range(c.shape[0]-1):
    for i in range(c.shape[1]-1):
        if i>=j:
            c[j+1,i+1] = c[j,i+1] - c[j,i]
print(c)
def f(x):
    return 8*math.comb(x,3)+16*math.comb(x,2)+9*math.comb(x,1)+1
print(f(405000//2 - 1))
