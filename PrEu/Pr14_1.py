import time
start = time.perf_counter()
value = {1:1}
def Col(n):
    if n in value:
        return value[n]
    elif n % 2 == 0:
        value[n] = (1 + Col(n//2))
    else:
        value[n] = (2 + Col((3*n+1)//2))
    return value[n]
i = 999999
ans = [1,1]
while i > 499999:
    a = Col(i)
    if a > ans[1]:
        ans = [i,a]
    i = i-1
print(ans,round(time.perf_counter()-start,2))
