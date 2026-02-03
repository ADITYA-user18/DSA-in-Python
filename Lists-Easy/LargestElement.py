class Larger:
    def LargerElement(self,nums):

        larger = nums[0]
        i=1

        while i < len(nums):
            if nums[i] > larger:
                larger = nums[i]
            i+=1

        return larger
    

a = Larger()
b = a.LargerElement([21,5,7,4,1,2,5,2,5,2,2,48485,4,51,5,4684848484])

print(b)