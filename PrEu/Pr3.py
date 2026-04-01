n = 2
a = 600851475143
ans = 1
while a != 1:
    while a % n != 0:
        n = n+1
    if n > ans:
        ans = n
    a = a//n
    n = 2
print(ans)
