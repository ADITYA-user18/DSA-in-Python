class Solution(object):
    def twoSum(self, numbers, target):
         seen = {}

         for i in range(0,len(numbers)):
            remain = target - numbers[i]

            if remain in seen:
                return [seen[remain]+1,i+1]

            seen[numbers[i]] = i

        

        