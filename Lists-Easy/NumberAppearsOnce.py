class OneElementAppearence:
    def OneElementAppearenceInArray(self,nums):
        n = len(nums)

        dict = {}

        for num in nums:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1

        for key in dict:
            if dict[key]==1:
                return key
        
        return f"No Number Appeared Once"
a = OneElementAppearence()
b = a.OneElementAppearenceInArray([1,2,2,3,3,1])

print(b)