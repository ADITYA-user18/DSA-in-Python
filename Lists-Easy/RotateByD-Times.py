class DTimes:
    def DTimesRotater(self,nums,d):
        n = len(nums)
        d = d%n

        for _ in range(d):
            first = nums[0]
            for i in range(1,n):
                nums[i-1] = nums[i]
            nums[n-1] = first


        return nums


a = DTimes()
b = a.DTimesRotater([1,2,3,4,5,6,7,8,9],2)

print(b)