'''
graph dfs - median
695.Max Area of Island
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) 
connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)
'''

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]

def maxAreaOfIsland(grid):
    cache_cnt = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                cnt = dfs(i,j,grid)
                print i, j, cnt
                cache_cnt.append(cnt)
    return max(cache_cnt)
    
def dfs(i,j,grid):
    cnt = 0
    print i,j, grid
    if i<0 or j<0 or i>len(grid)-1 or j>len(grid[0])-1 or grid[i][j] == 0:
        return 0
    else:
        grid[i][j]=0
        cnt = dfs(i-1,j,grid) + dfs(i+1,j,grid) + dfs(i,j-1,grid) + dfs(i,j+1,grid)
        cnt += 1
    return cnt

maxAreaOfIsland(grid)
