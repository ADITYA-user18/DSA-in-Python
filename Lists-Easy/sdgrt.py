nums = [1,0,3,0,5]


k = 0

for i in range(len(nums)):
    if nums[i]==0:
        nums[k],nums[i] = nums[i],nums[k]
        k+=1


print(nums)
