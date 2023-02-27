"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(n, r, c):
            allSame = True
            for i in range(n):
                for j in range(n):
                    if grid[r][c] != grid[r + i][c + j]:
                        allSame = False
                        break
            if allSame:
                return Node(grid[r][c], True)
            n = n // 2
            topleft = dfs(n,r,c)
            topright = dfs(n,r,c + n)
            bottomleft = dfs(n,r + n,c)
            bottomright = dfs(n,r + n,c + n)
            return Node(0, False, topleft, topright, bottomleft, bottomright)
        return dfs(len(grid),0,0)
    
# we use dfs to solve this problem
# in this problem we return the tree nodes as an output
# we first compare all the cells in the given grid and check if theres any cell with different value if it gets then it forms the quadrants and call the recursion function untill all the quadrants are not traversed and solved
# we form the quadrants by using n//2 where n is the length of given grid
# as we used dfs it first solve the 1st quadrant/leaf and then its sub-quadrants/childs and their sub-quadrants/childs untill n becomes 1 and then it goes to next parent quadrant/leaf







