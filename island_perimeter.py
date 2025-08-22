from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        land_num = 0
        common_edge = 0

        if len(grid) == len(grid[0]) and len(grid) == 1:
            if grid[0][0] == 1:
                return 4
            
           
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    land_num += 1
                    if (j+1) < len(grid[i]):
                        if grid[i][j] == grid[i][j+1]:
                            common_edge += 2
        
        for col in range(len(grid[0])):
            for row in range(len(grid)):
                if (row + 1) < len(grid):
                    if grid[row][col] == 1 and grid[row][col] == grid[row+1][col]:
                        common_edge += 2
  
        # print(land_num)
        # print(common_edge)
        land_cir = 4 * land_num - common_edge
        return land_cir


# case test
# grid = [[0,1,0,0], [1,1,1,0], [0,1,0,0], [1,1,0,0]]
# grid = [[1,0]]
# grid = [[1]]
# grid = [[0, 1]]
# grid = [[1,1]]
grid = [[1,1], [0,0]]
obj = Solution()
print(obj.islandPerimeter(grid))

