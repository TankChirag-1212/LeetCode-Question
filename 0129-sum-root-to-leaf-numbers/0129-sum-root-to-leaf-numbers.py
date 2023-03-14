# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.total  = 0
        def dfs(root, Sum):
            if root is None:
                return
            Sum = Sum * 10 + root.val
            if root.left is None and root.right is None:
                self.total += Sum
                return
            dfs(root.left, Sum)
            dfs(root.right, Sum)
        dfs(root, 0)
        return self.total
            
'''
• In this problem we have to return the value of total sum of the numbers we get by traversing the each branch of the tree.
• this problem can be solved by dfs pre-order approach on binary tree.
• in above code we use total var to store the sum of the number we get after we reach the leaf node.
• Sum var is use to store the number until we reach the leaf node when we reach the leaf node we add the number stored in Sum to the total var.
• We use recursion to do traverse the each node in pre-order traversal.
• the function stops when all the nodes in the binary tree are traversed. 
'''