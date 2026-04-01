import time
start = time.perf_counter()

val = {(0,0):1}
def set(m,n):
    if m*n == 0:
        return 1
    if (m,n) in val:
        return val[(m,n)]
    else:
        val[(m,n)] = set(m-1,n) + set(m,n-1)
    return val[(m,n)]
    
print(set(20,20),round(time.perf_counter()-start,2))
