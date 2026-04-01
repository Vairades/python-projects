ans = 0
i = 999
j = 999
while i > 99:
    while (i*j//100000 != i*j%10) or (i*j//10000%10 != i*j%100//10) or (i*j//1000%10 != i*j%1000//100):
        j = j-1
    if i*j > ans:
        ans = i*j
    j = 999
    i = i-1
print(ans)
