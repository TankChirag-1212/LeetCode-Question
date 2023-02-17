# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        arr = []
        def traverse(node):
            if node:
                traverse(node.left)
                arr.append(node.val)
                traverse(node.right)
              
        traverse(root)
        print(arr)
        diff = float('inf')
        for i in range(1, len(arr)):
            diff = min(diff, arr[i] - arr[i-1])
        return diff
    
# ANOTHER APPROACH
    # prev, res = None, float("inf")
    # def dfs(node):
    #     if node == None:
    #         dfs(node.left)
    #         nonlocal prev, ans
    #         if prev:
    #             res = min(res, node.val - prev.val)
    #         prev = node
    #         dfs(node.right)
    # dfs(root)
    # return res
    
# First create the recursion function to traverse the tree it first traverse to the left and while shifting to the right i.e backtracking it appends the current node in the arr
# it always gives the sorted array of the values in the tree
# then we use for loop to iterrate the array find the diff between two values the minimum value will be return 
# second approach is more optimal and uses dfs