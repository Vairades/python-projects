nums = [2,3]
ans = 5
n = 5
while n < 2000000:
    k = 1
    while k < len(nums):
        if n % nums[k] == 0:
            break
        elif nums[k] > n**0.5:
            nums.append(n)
            ans = ans+n
            break
        k = k+1
    n = n+2
    if n % 10 == 5:
        n = n+2
print(ans)
