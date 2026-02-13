class FloorCeilFinder:
    def FindFloorCeil(self,nums,x):
        left = 0
        right = len(nums)-1

        while left <= right:
            mid = (left+right)//2

            if x == nums[mid]:
                return f"The Floor and Ceil is {nums[mid]}"
             
            if nums[mid] < x:
                floor_val = nums[mid]
                left = mid+1
            else:
                ceil_val = nums[mid]
                right = mid -1

        return f"The Floor value is {floor_val} and the Ceil value is {ceil_val}"
    

a = FloorCeilFinder()
b = a.FindFloorCeil([1,3,4,6,8,9,10,12,13],11)

print(b)