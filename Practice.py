nums = [1,5,2,5,2,8,82,3,48,5,2,48,2,45,222]


left = 0
right =len(nums)-1

while left <= right:
    nums[left],nums[right] = nums[right],nums[left]
    left+=1
    right-=1

print(nums)