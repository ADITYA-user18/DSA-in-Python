class Duplicates:
    def ArrayDuplicates(self,nums):
        n = len(nums)
        kvpair = dict()

        for i in range(0,n):
            if nums[i] not in kvpair:
                kvpair[nums[i]] = 1
            else:
                kvpair[nums[i]] +=1

        result = [num for num in nums if kvpair[num]==1]
        return result
    
a = Duplicates()
b = a.ArrayDuplicates([1,5,2,4,4,7,8,9,9,6,6,6,6,7,2])

print(b)