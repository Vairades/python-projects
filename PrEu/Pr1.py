n = 3
ans = 0
while n < 1000:
    if (n % 3 == 0) or (n % 5 == 0):
        ans = ans + n
    n = n+1
print(ans)
