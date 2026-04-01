i = 1
ans = 1
while ans <= 500:
    i = i+1 
    ans = 1
    n = i*(i+1)//2
    k = 2
    while n != 1:
        if n % k == 0:
            po = 2
            n = n//k
            while n % k == 0:
                n = n//k
                po = po+1
            ans = ans * po
        k = k+1
print(i*(i+1)//2)

