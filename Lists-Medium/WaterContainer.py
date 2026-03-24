class Solution(object):
    def maxArea(self, height):
        n = len(height)
        max_area = 0

        for i in range(n-1):
            for j in range(i+1, n):

                width = j - i
                h = min(height[i], height[j])
                area = width * h

                max_area = max(max_area, area)

        return max_area


height = [1,8,6,2,5,4,8,3,7
obj = Solution()
print("Final Answer:", obj.maxArea(height))
