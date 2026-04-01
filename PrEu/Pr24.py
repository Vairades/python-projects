sw = {0:1,1:1}
i = 1
while sw[i] <= 1000000:
    sw[i+1] = (i+1)*sw[i]
    i += 1
print(sw)
def perm(go):
    nums = [0,1,2,3,4,5,6,7,8,9]
    ans = []
    while len(nums) > 1:
        ho = len(nums) - 1
        i = go // sw[ho]
        ans.append(nums[i])
        nums.remove(ans[-1])
        go = go%sw[ho]
    ans.append(nums[0])
    return ans
#print(perm(0),perm(1),perm(2),perm(3),perm(4),perm(5))
print(perm(999999))
