class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        direction = [[1,0],[0,1],[-1,0],[0,-1]]
        n = len(grid)
        q = deque()     # it creates the empty queue
        for row in range(n):
            for col in range(n):
                if grid[row][col] ==1:
                    q.append([row,col])     # it adds the (row,col) cordinates of the land in the grid in the queue

        ans = 0
        while q:
            r,c = q.popleft()         # it pops the first added cordinates in the queue and asign to the r,c
            ans = grid[r][c]         # it stores the value of that cell in the ans
            for dr,dc in direction:
                newR = r + dr           # we create the new cordinates to move to the next cell
                newC = c + dc
                if (max(newR,newC) < n and min(newR,newC) >= 0 and grid[newR][newC] == 0):
                    grid[newR][newC] = grid[r][c] + 1
                    q.append([newR,newC])       # if the next cell has value 0 i.e its not visited for once then it add the coridnates of it in the queue
                                                # it continues until all the cell in the grid is covered or visited for atleast once
        return (ans-1) if ans>1 else -1    # it returns the value of the last cell we will visit if there is no land/water in the grid it will return -1 