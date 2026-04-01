def rec(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return 0
    if n % 5 == 0:
        return 0
    i = 1
    while ((10**i - 1) % n) != 0:
        i += 1
    return i
ans = 7
lon = 6
n = 11
while n < 1000:
    if rec(n) > lon:
        ans = n
        lon = rec(n)
    n += 2
print(ans)
