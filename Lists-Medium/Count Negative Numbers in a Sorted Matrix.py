class Solution(object):
    def countNegatives(self, grid):

        n = len(grid)
        count = 0

        for i in range(n):
            for j in range(len(grid[i])):
                if grid[i][j] < 0:
                    count+=1


        return count

           
