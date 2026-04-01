i = 2
n = 3
while i < 10002:
    k = 2
    while k < n:
        if n % k == 0:
            n = n+1
            break
        elif k > n**0.5:
            n = n+1
            i = i+1
            break
        k = k+1
print(n-1)
